# Inventory Systems

An inventory system tracks which items a player owns and how many of each item they have.

BrickVerse Players expose `Inventory` and `Backpack` hierarchies. Use them for runtime item Instances, while a server-side data model stores authoritative ownership.

## Separate definitions from ownership

Item definitions describe all available items:

```lua
type ItemDefinition = {
	displayName: string,
	maxStack: number,
	price: number,
	toolTemplate: string?,
}

local ITEMS: { [string]: ItemDefinition } = {
	sword = {
		displayName = "Sword",
		maxStack = 1,
		price = 250,
		toolTemplate = "SwordTool",
	},
	medkit = {
		displayName = "Medkit",
		maxStack = 5,
		price = 75,
		toolTemplate = "MedkitTool",
	},
}
```

Player ownership stores amounts:

```lua
type InventoryData = { [string]: number }

local inventories: { [Player]: InventoryData } = {}
```

## Initialize inventory

```lua
local function setupPlayer(player: Player)
	inventories[player] = {}
end

Players.PlayerAdded:Connect(setupPlayer)

Players.PlayerRemoved:Connect(function(player)
	inventories[player] = nil
end)
```

## Validate item IDs

```lua
local function getDefinition(itemId: string): ItemDefinition?
	return ITEMS[itemId]
end
```

Never accept arbitrary item definitions from the client.

## Add an item

```lua
local function addItem(
	player: Player,
	itemId: string,
	amount: number
): (boolean, string?)
	local definition = getDefinition(itemId)
	local inventory = inventories[player]

	if not definition or not inventory then
		return false, "Invalid item"
	end

	amount = math.floor(amount)

	if amount <= 0 then
		return false, "Invalid amount"
	end

	local current = inventory[itemId] or 0
	local available = definition.maxStack - current

	if available <= 0 then
		return false, "Inventory stack is full"
	end

	local added = math.min(amount, available)
	inventory[itemId] = current + added

	return true, nil
end
```

## Remove an item

```lua
local function removeItem(
	player: Player,
	itemId: string,
	amount: number
): boolean
	local inventory = inventories[player]

	if not inventory then
		return false
	end

	amount = math.floor(amount)

	if amount <= 0 then
		return false
	end

	local current = inventory[itemId] or 0

	if current < amount then
		return false
	end

	local remaining = current - amount

	if remaining == 0 then
		inventory[itemId] = nil
	else
		inventory[itemId] = remaining
	end

	return true
end
```

## Check ownership

```lua
local function hasItem(
	player: Player,
	itemId: string,
	amount: number?
): boolean
	local inventory = inventories[player]

	if not inventory then
		return false
	end

	return (inventory[itemId] or 0) >= (amount or 1)
end
```

## Give a Tool

When an owned item has a Tool template:

```lua
local function giveTool(player: Player, itemId: string): boolean
	local definition = ITEMS[itemId]

	if not definition or not definition.toolTemplate then
		return false
	end

	if not hasItem(player, itemId) then
		return false
	end

	local template = serverTools:FindChild(definition.toolTemplate)

	if not template or not template:IsA("Tool") then
		return false
	end

	local tool = template:Clone()
	tool.Parent = player.Backpack

	return true
end
```

Keep the source templates in a server-only hierarchy.

## Prevent duplicate tools

```lua
local function hasRuntimeTool(player: Player, toolName: string): boolean
	return player.Backpack:FindChild(toolName) ~= nil
		or player.Inventory:FindChild(toolName) ~= nil
		or (
			player.HoldingTool ~= nil
			and player.HoldingTool.Name == toolName
		)
end
```

## Networked purchase

Client sends only the item ID:

```lua
local request = NetMessage.New()
request:AddString("itemId", "sword")

purchaseEvent:InvokeServer(request)
```

Server:

```lua
purchaseEvent.InvokedServer:Connect(function(player, message)
	local itemId = message:GetString("itemId")
	local definition = ITEMS[itemId]

	if not definition then
		return
	end

	local profile = getProfile(player)

	if not profile then
		return
	end

	if profile.coins < definition.price then
		sendPurchaseResult(player, false, "Not enough coins")
		return
	end

	local added = addItem(player, itemId, 1)

	if not added then
		sendPurchaseResult(player, false, "Inventory is full")
		return
	end

	profile.coins -= definition.price
	sendPurchaseResult(player, true, "")
end)
```

The server owns the price and reward.

## Save inventory

Include the inventory table in the profile:

```lua
type Profile = {
	coins: number,
	inventory: InventoryData,
}
```

Save:

```lua
Profiles:SetAsync("player:" .. player.UserID, {
	coins = profile.coins,
	inventory = profile.inventory,
})
```

Validate loaded item IDs:

```lua
local function sanitizeInventory(value: any): InventoryData
	local inventory: InventoryData = {}

	if type(value) ~= "table" then
		return inventory
	end

	for itemId, amount in pairs(value) do
		local definition = ITEMS[itemId]

		if definition and type(amount) == "number" then
			inventory[itemId] = math.clamp(
				math.floor(amount),
				0,
				definition.maxStack
			)
		end
	end

	return inventory
end
```

## Send inventory to UI

Use a focused message per item:

```lua
local message = NetMessage.New()
message:AddString("itemId", itemId)
message:AddInt("amount", inventory[itemId] or 0)

inventoryChanged:InvokeClient(message, player)
```

The client updates its UI, but the server remains authoritative.

## Equip request

```lua
equipEvent.InvokedServer:Connect(function(player, message)
	local itemId = message:GetString("itemId")

	if not hasItem(player, itemId) then
		return
	end

	if hasRuntimeTool(player, itemId) then
		return
	end

	giveTool(player, itemId)
end)
```

Add cooldown and game-state checks.

## Complete inventory module

```lua
local InventoryService = {}

local data: { [Player]: { [string]: number } } = {}

function InventoryService.Create(player: Player)
	data[player] = {}
end

function InventoryService.Destroy(player: Player)
	data[player] = nil
end

function InventoryService.Get(player: Player)
	return data[player]
end

function InventoryService.Has(
	player: Player,
	itemId: string,
	amount: number?
): boolean
	local inventory = data[player]

	if not inventory then
		return false
	end

	return (inventory[itemId] or 0) >= (amount or 1)
end

function InventoryService.Add(
	player: Player,
	itemId: string,
	amount: number
): boolean
	local inventory = data[player]
	local definition = ITEMS[itemId]

	if not inventory or not definition then
		return false
	end

	local current = inventory[itemId] or 0
	local nextAmount = math.clamp(
		current + math.floor(amount),
		0,
		definition.maxStack
	)

	if nextAmount == current then
		return false
	end

	inventory[itemId] = nextAmount
	return true
end

return InventoryService
```
