# Modules

A `ModuleScript` contains reusable BrickLua code. Modules reduce duplication and make larger games easier to organize.

A module returns a value when it is loaded with `require`. Most modules return a table of functions.

## Create a module

Create a `ModuleScript` named `MathHelpers`:

```lua
local MathHelpers = {}

function MathHelpers.ClampCoins(value: number): number
	return math.max(0, math.floor(value))
end

function MathHelpers.CalculateReward(level: number): number
	return 50 + level * 20
end

return MathHelpers
```

Load it from another script:

```lua
local MathHelpers = require(script.Parent:WaitChild("MathHelpers"))

local reward = MathHelpers.CalculateReward(5)
print(reward)
```

## Module locations

Where a module is stored determines who can access it.

| Location | Recommended use |
| --- | --- |
| Shared hierarchy | Types, constants, and code used by server and client. |
| Server-only hierarchy | Persistence, rewards, moderation, secrets, and validation. |
| Client hierarchy | UI controllers, camera behavior, and local effects. |

{% hint style="danger" %}
Putting validation code in a shared module does not make client execution trusted. The server must call the validation before changing authoritative state.
{% endhint %}

## Configuration module

```lua
local GameConfig = {
	ROUND_DURATION = 180,
	MIN_PLAYERS = 2,
	STARTING_COINS = 100,

	Items = {
		sword = {
			price = 250,
			maxStack = 1,
		},
		medkit = {
			price = 75,
			maxStack = 5,
		},
	},
}

return table.freeze(GameConfig)
```

`table.freeze` prevents accidental changes to the top-level table.

## Stateful module

Modules are cached after their first `require`. This means module-local state is shared by all scripts requiring that module on the same execution side.

```lua
local Counter = {}

local value = 0

function Counter.Increment(): number
	value += 1
	return value
end

function Counter.Get(): number
	return value
end

return Counter
```

Use shared module state intentionally. Do not use it as persistent storage.

## Constructor pattern

A module can create independent objects:

```lua
local Cooldown = {}
Cooldown.__index = Cooldown

function Cooldown.new(duration: number)
	return setmetatable({
		duration = duration,
		lastUsed = {},
	}, Cooldown)
end

function Cooldown:CanUse(key: any): boolean
	local now = os.clock()
	local previous = self.lastUsed[key] or 0

	if now - previous < self.duration then
		return false
	end

	self.lastUsed[key] = now
	return true
end

function Cooldown:Remove(key: any)
	self.lastUsed[key] = nil
end

return Cooldown
```

Use it:

```lua
local Cooldown = require(script.Parent:WaitChild("Cooldown"))
local purchaseCooldown = Cooldown.new(1)

if purchaseCooldown:CanUse(player) then
	print("Purchase allowed")
end
```

## Service-style module

```lua
local PlayerData = {}

local profiles = {}

function PlayerData.Add(player: Player, profile: table)
	profiles[player] = profile
end

function PlayerData.Get(player: Player): table?
	return profiles[player]
end

function PlayerData.Remove(player: Player): table?
	local profile = profiles[player]
	profiles[player] = nil
	return profile
end

return PlayerData
```

A server script can own the lifecycle:

```lua
local PlayerData = require(script.Parent:WaitChild("PlayerData"))

Players.PlayerAdded:Connect(function(player)
	PlayerData.Add(player, {
		coins = 0,
		level = 1,
	})
end)

Players.PlayerRemoved:Connect(function(player)
	PlayerData.Remove(player)
end)
```

## Avoid circular dependencies

This is a circular dependency:

```text
Inventory requires Shop
Shop requires Inventory
```

Move shared behavior into a third module:

```text
Inventory ─┐
           ├── requires ItemConfig
Shop ──────┘
```

## Type exports

A module can export a type:

```lua
export type ItemDefinition = {
	displayName: string,
	price: number,
	maxStack: number,
}

local Items: { [string]: ItemDefinition } = {
	sword = {
		displayName = "Sword",
		price = 250,
		maxStack = 1,
	},
}

return Items
```

## Error boundaries

Do not silently swallow module errors. Add context:

```lua
local success, result = pcall(function()
	return require(script.Parent:WaitChild("ItemConfig"))
end)

if not success then
	error("Could not load ItemConfig: " .. tostring(result))
end

local ItemConfig = result
```

## Complete reusable Part factory

`PartFactory` module:

```lua
local PartFactory = {}

function PartFactory.CreatePlatform(
	parent: Instance,
	name: string,
	position: Vector3,
	size: Vector3,
	color: Color
): Instance
	local part = Instance.New("Part", parent)
	part.Name = name
	part.Position = position
	part.Size = size
	part.Color = color
	part.Anchored = true
	part.CanCollide = true
	part.Shape = PartShape.Brick
	part.Material = PartMaterial.SmoothPlastic

	return part
end

return PartFactory
```

Server script:

```lua
local PartFactory = require(script.Parent:WaitChild("PartFactory"))

PartFactory.CreatePlatform(
	world,
	"StartPlatform",
	Vector3.New(0, 2, 0),
	Vector3.New(12, 1, 12),
	Color.FromRGB(1, 135, 248)
)
```
