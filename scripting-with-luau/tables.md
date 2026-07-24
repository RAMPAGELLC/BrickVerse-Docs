# Tables

Tables are BrickLua's main data structure. They can represent arrays, dictionaries, sets, records, configuration, and object-like modules.

## Arrays

An array uses sequential numeric indexes:

```lua
local maps = {
	"Forest",
	"Desert",
	"Space Station",
}

print(maps[1]) -- Forest
```

BrickLua arrays begin at index `1`.

Add and remove values:

```lua
table.insert(maps, "City")
local removed = table.remove(maps, 2)
```

Iterate with `ipairs`:

```lua
for index, mapName in ipairs(maps) do
	print(index, mapName)
end
```

## Dictionaries

A dictionary uses named keys:

```lua
local profile = {
	coins = 100,
	level = 3,
	title = "Builder",
}

print(profile.coins)
print(profile["level"])
```

Update a value:

```lua
profile.coins += 25
```

Iterate with `pairs`:

```lua
for key, value in pairs(profile) do
	print(key, value)
end
```

## Typed records

Define a reusable type:

```lua
type PlayerProfile = {
	coins: number,
	level: number,
	inventory: { string },
}

local profile: PlayerProfile = {
	coins = 0,
	level = 1,
	inventory = {},
}
```

## Sets

A set uses values as keys:

```lua
local allowedItems = {
	Sword = true,
	Medkit = true,
	Flashlight = true,
}

if allowedItems.Sword then
	print("Sword is allowed")
end
```

A set of Instances:

```lua
local activeEnemies: { [Instance]: boolean } = {}

activeEnemies[enemy] = true
activeEnemies[enemy] = nil
```

## Per-player state

Tables are useful for server-side session state:

```lua
type SessionData = {
	coins: number,
	lastPurchase: number,
}

local sessions: { [Player]: SessionData } = {}

Players.PlayerAdded:Connect(function(player)
	sessions[player] = {
		coins = 0,
		lastPurchase = 0,
	}
end)

Players.PlayerRemoved:Connect(function(player)
	sessions[player] = nil
end)
```

Always remove references when players leave.

## Copying tables

This does not create a copy:

```lua
local a = { coins = 0 }
local b = a

b.coins = 100
print(a.coins) -- 100
```

Both variables point to the same table.

Create a shallow copy:

```lua
local copy = table.clone(a)
```

For nested tables, copy each nested table too:

```lua
local function copyProfile(profile)
	return {
		coins = profile.coins,
		level = profile.level,
		inventory = table.clone(profile.inventory),
	}
end
```

## Default data

Use a function so every player receives a separate table:

```lua
local function createDefaultProfile(): PlayerProfile
	return {
		coins = 0,
		level = 1,
		inventory = {},
	}
end
```

Do not reuse one mutable default table.

## Array membership

Find a value manually:

```lua
local function contains(list: { string }, target: string): boolean
	for _, value in ipairs(list) do
		if value == target then
			return true
		end
	end

	return false
end
```

For frequent membership checks, use a set instead.

## Sorting

```lua
local scores = { 25, 100, 50, 10 }

table.sort(scores, function(a, b)
	return a > b
end)
```

Sort records:

```lua
local leaderboard = {
	{ name = "Alice", score = 150 },
	{ name = "Bob", score = 220 },
	{ name = "Casey", score = 180 },
}

table.sort(leaderboard, function(a, b)
	return a.score > b.score
end)
```

## Tables and JSON

JSON objects and arrays decode into tables. Only serializable values should be encoded:

```lua
local data = {
	version = 1,
	maps = { "Forest", "City" },
	settings = {
		friendlyFire = false,
	},
}
```

Do not include Instances, functions, event connections, or cyclic references in JSON or datastore values.

## Tables and NetMessage

`NetworkEvent` uses `NetMessage`, which provides typed fields instead of sending an unrestricted table:

```lua
local message = NetMessage.New()
message:AddString("itemId", "sword")
message:AddInt("quantity", 1)
```

Read the values on the receiving side:

```lua
local itemId = message:GetString("itemId")
local quantity = message:GetInt("quantity")
```

## Configuration table example

```lua
local ITEM_CONFIG = {
	sword = {
		displayName = "Sword",
		price = 250,
		maxStack = 1,
	},
	medkit = {
		displayName = "Medkit",
		price = 75,
		maxStack = 5,
	},
}

local function getItemConfig(itemId: string)
	return ITEM_CONFIG[itemId]
end

local sword = getItemConfig("sword")

if sword then
	print(sword.displayName, sword.price)
end
```

## Complete inventory helper

```lua
type Inventory = { [string]: number }

local function addItem(
	inventory: Inventory,
	itemId: string,
	amount: number
): number
	local current = inventory[itemId] or 0
	local nextAmount = current + amount

	inventory[itemId] = nextAmount
	return nextAmount
end

local inventory: Inventory = {}

addItem(inventory, "medkit", 2)
addItem(inventory, "medkit", 1)

print(inventory.medkit) -- 3
```
