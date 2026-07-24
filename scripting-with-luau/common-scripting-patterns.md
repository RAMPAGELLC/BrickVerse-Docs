# Common Scripting Patterns

These patterns help keep BrickLua systems reliable, secure, and maintainable.

## Guard clauses

Reject invalid state early:

```lua
local function healPlayer(player: Player, amount: number)
	if player.IsDead then
		return
	end

	if type(amount) ~= "number" or amount <= 0 then
		return
	end

	player:Heal(math.clamp(amount, 0, 100))
end
```

## Debounce

Use a boolean for one object-wide action:

```lua
local busy = false

button.Clicked:Connect(function()
	if busy then
		return
	end

	busy = true

	task.delay(1, function()
		busy = false
	end)
end)
```

## Per-player cooldown

```lua
local lastUse: { [Player]: number } = {}
local COOLDOWN = 2

local function canUse(player: Player): boolean
	local now = os.clock()
	local previous = lastUse[player] or 0

	if now - previous < COOLDOWN then
		return false
	end

	lastUse[player] = now
	return true
end

Players.PlayerRemoved:Connect(function(player)
	lastUse[player] = nil
end)
```

## Rate-limit buckets

For actions that allow bursts:

```lua
type Bucket = {
	tokens: number,
	updatedAt: number,
}

local buckets: { [Player]: Bucket } = {}
local MAX_TOKENS = 5
local REFILL_PER_SECOND = 1

local function consume(player: Player): boolean
	local now = os.clock()
	local bucket = buckets[player]

	if not bucket then
		bucket = {
			tokens = MAX_TOKENS,
			updatedAt = now,
		}
		buckets[player] = bucket
	end

	local elapsed = now - bucket.updatedAt
	bucket.updatedAt = now
	bucket.tokens = math.min(
		MAX_TOKENS,
		bucket.tokens + elapsed * REFILL_PER_SECOND
	)

	if bucket.tokens < 1 then
		return false
	end

	bucket.tokens -= 1
	return true
end
```

## Safe async call

```lua
local function tryAsync<T>(callback: () -> T): (boolean, T?)
	local success, result = pcall(callback)

	if not success then
		warn(result)
		return false, nil
	end

	return true, result
end
```

Use:

```lua
local success, data = tryAsync(function()
	return Profiles:GetAsync(key)
end)
```

## Retry with backoff

```lua
local function retry<T>(
	attempts: number,
	callback: () -> T
): (boolean, T?)
	local lastError = nil

	for attempt = 1, attempts do
		local success, result = pcall(callback)

		if success then
			return true, result
		end

		lastError = result

		if attempt < attempts then
			task.wait(2 ^ (attempt - 1))
		end
	end

	warn("Operation failed:", lastError)
	return false, nil
end
```

Use retries carefully for non-idempotent writes.

## Cleanup container

Track event connections:

```lua
local connections = {}

local function connect(signal, callback)
	local connection = signal:Connect(callback)
	table.insert(connections, connection)
	return connection
end

local function cleanup()
	for _, connection in ipairs(connections) do
		connection:Disconnect()
	end

	table.clear(connections)
end
```

## Object lifecycle cleanup

```lua
part.Destroying:Connect(function()
	cleanup()
end)
```

Remove cached references as objects leave the hierarchy.

## State machine

```lua
type RoundState = "Waiting" | "Starting" | "Playing" | "Ending"

local state: RoundState = "Waiting"

local ALLOWED = {
	Waiting = { Starting = true },
	Starting = { Playing = true, Waiting = true },
	Playing = { Ending = true },
	Ending = { Waiting = true },
}

local function setState(nextState: RoundState): boolean
	if not ALLOWED[state][nextState] then
		warn("Invalid transition", state, nextState)
		return false
	end

	print(state, "->", nextState)
	state = nextState
	return true
end
```

## Configuration module

Keep tunable values together:

```lua
local CONFIG = table.freeze({
	ROUND_DURATION = 180,
	MIN_PLAYERS = 2,
	RESPAWN_TIME = 5,
	MAX_INVENTORY_SLOTS = 20,
})
```

## Factory function

```lua
local function createPart(options)
	local part = Instance.New("Part", options.parent or world)
	part.Name = options.name or "Part"
	part.Position = options.position or Vector3.Zero
	part.Size = options.size or Vector3.One
	part.Color = options.color or Color.FromRGB(255, 255, 255)
	part.Anchored = options.anchored ~= false

	return part
end
```

## Service module

```lua
local PlayerProfiles = {}

local profiles = {}

function PlayerProfiles.Set(player, profile)
	profiles[player] = profile
end

function PlayerProfiles.Get(player)
	return profiles[player]
end

function PlayerProfiles.Remove(player)
	local profile = profiles[player]
	profiles[player] = nil
	return profile
end

return PlayerProfiles
```

## Tag-driven behavior

```lua
local function setupInteractable(instance: Instance)
	if not instance:IsA("Physical") then
		return
	end

	instance.Clicked:Connect(function(player)
		print(player.Name, "used", instance.Name)
	end)
end

for _, instance in ipairs(
	world:GetDescendantsWithTag("Interactable")
) do
	setupInteractable(instance)
end
```

## Server validation pipeline

```lua
local function handlePurchase(player: Player, message: NetMessage)
	if not consume(player) then
		return
	end

	local itemId = message:GetString("itemId")
	local definition = ITEMS[itemId]

	if not definition then
		return
	end

	local profile = Profiles.Get(player)

	if not profile then
		return
	end

	if profile.coins < definition.price then
		return
	end

	if not Inventory.CanAdd(player, itemId, 1) then
		return
	end

	profile.coins -= definition.price
	Inventory.Add(player, itemId, 1)
end
```

Keep each validation step explicit.

## Avoid deeply nested code

Hard to read:

```lua
if player then
	if profile then
		if item then
			if profile.coins >= item.price then
				-- Purchase
			end
		end
	end
end
```

Use guards:

```lua
if not player then return end
if not profile then return end
if not item then return end
if profile.coins < item.price then return end

-- Purchase
```

## Avoid polling

Instead of:

```lua
while true do
	if part.Color ~= previousColor then
		-- React
	end
	task.wait()
end
```

Use:

```lua
part.PropertyChanged:Connect(function(propertyName)
	if propertyName == "Color" then
		-- React
	end
end)
```

## Immutable shared definitions

```lua
local ITEMS = table.freeze({
	sword = table.freeze({
		price = 250,
		maxStack = 1,
	}),
})
```

Do not expose mutable authoritative definitions to client code.

## Logging with context

```lua
local function logPurchase(player: Player, itemId: string, amount: number)
	print(string.format(
		"[Purchase] user=%s id=%s item=%s amount=%d",
		player.Name,
		player.UserID,
		itemId,
		amount
	))
end
```

Do not log secrets or private credentials.

## Final architecture example

```text
Server
├── PlayerData
├── InventoryService
├── PurchaseService
├── RoundService
└── NetworkHandlers

Shared
├── ItemDefinitions
├── Types
└── NetworkEvents

Client
├── HUDController
├── InventoryController
└── InputController
```

Keep server authority, shared definitions, and client presentation clearly separated.
