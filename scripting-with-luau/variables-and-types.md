# Variables and Types

Variables store values that your script can reuse and change. BrickLua supports Luau's gradual type system, so you can write scripts with or without explicit type annotations.

## Local variables

Use `local` for variables:

```lua
local score = 0
local username = "Builder"
local isAlive = true
```

Variables should normally be local. A local variable is limited to the current scope and does not accidentally overwrite another script's state.

```lua
local coins = 25
coins = coins + 10

print(coins) -- 35
```

## Basic types

| Type | Example |
| --- | --- |
| `nil` | `nil` |
| `boolean` | `true` |
| `number` | `42`, `3.5` |
| `string` | `"BrickVerse"` |
| `table` | `{ coins = 100 }` |
| `function` | `function() end` |
| `Instance` | A Part, Player, UI object, or other hierarchy object |
| BrickVerse value type | `Vector3`, `Color`, `Quaternion`, and others |

Check a normal Luau type with `type`:

```lua
print(type(100))          -- number
print(type("BrickVerse")) -- string
print(type({}))           -- table
```

Use `typeof` when you also need to identify BrickVerse value types and Instances:

```lua
local position = Vector3.New(0, 5, 0)
local part = Instance.New("Part")

print(typeof(position))
print(typeof(part))
```

## Type annotations

Type annotations document intent and allow the analyzer to catch mistakes.

```lua
local score: number = 0
local displayName: string = "Builder"
local isRoundActive: boolean = false
```

Function parameters and return values can also be typed:

```lua
local function addCoins(current: number, amount: number): number
	return current + amount
end
```

## Optional values

A value that may be absent can use `?`:

```lua
local target: Instance? = world:FindChild("Target")
```

Always check an optional value before using it:

```lua
if target then
	print(target.Name)
end
```

## Strings

Use `..` to concatenate strings:

```lua
local playerName = "Builder"
local message = "Welcome, " .. playerName .. "!"
print(message)
```

Use `string.format` for more complex messages:

```lua
local coins = 250
local message = string.format("%s has %d coins", playerName, coins)
print(message)
```

## Numbers

BrickLua uses numbers for integers and decimals:

```lua
local health = 100
local speed = 12.5

health -= 20
speed *= 1.25
```

Useful math functions include:

```lua
local clamped = math.clamp(150, 0, 100)
local roundedDown = math.floor(9.8)
local randomReward = math.random(10, 25)
```

## Vector2

`Vector2` stores two-dimensional values, commonly used by UI and input.

```lua
local position = Vector2.New(20, 40)
local scale = Vector2.New(1, 1)

print(position.X, position.Y)
```

Useful predefined values include:

```lua
Vector2.Zero
Vector2.One
Vector2.Up
Vector2.Down
Vector2.Left
Vector2.Right
```

## Vector3

`Vector3` stores positions, directions, sizes, and velocities:

```lua
local spawnPosition = Vector3.New(0, 5, 0)
local partSize = Vector3.New(4, 1, 4)
local upwardForce = Vector3.Up * 20
```

Vector math works directly:

```lua
local start = Vector3.New(0, 0, 0)
local finish = Vector3.New(10, 0, 0)
local offset = finish - start
local distance = offset.Magnitude
```

## Colors

Create colors from normalized values:

```lua
local color = Color.New(0.2, 0.6, 1, 1)
```

Or use RGB values:

```lua
local brickVerseBlue = Color.FromRGB(1, 135, 248)
```

Hex colors are also supported:

```lua
local darkBackground = Color.FromHex("#1A2433")
```

Use them on objects:

```lua
local part = Instance.New("Part", world)
part.Color = brickVerseBlue
```

## Instances

An Instance is a reference to an object in the hierarchy:

```lua
local part: Instance = Instance.New("Part", world)
```

Check inheritance with `IsA`:

```lua
if part:IsA("Physical") then
	print("This object supports physics")
end
```

Check for a specific class:

```lua
if part:IsA("Part") then
	part.Anchored = true
end
```

## Enums

Enums restrict a property to a known set of options:

```lua
part.Shape = PartShape.Brick
part.Material = PartMaterial.Metal
```

Using enums is safer than magic strings:

```lua
-- Avoid guessing a string:
-- part.Material = "Metal"

-- Use the enum:
part.Material = PartMaterial.Metal
```

## Constants

BrickLua does not require a separate constant keyword. Use uppercase names for values that should not change:

```lua
local MAX_HEALTH = 100
local RESPAWN_DELAY = 5
```

## Avoiding shared accidental state

This table is created once:

```lua
local DEFAULT_PROFILE = {
	coins = 0,
	level = 1,
}
```

Do not assign the same mutable table to every player. Create a new table:

```lua
local function createDefaultProfile()
	return {
		coins = 0,
		level = 1,
	}
end
```

## Complete example

```lua
local PART_NAME: string = "TypedPlatform"
local PART_COLOR: Color = Color.FromRGB(1, 135, 248)
local PART_POSITION: Vector3 = Vector3.New(0, 3, 0)
local PART_SIZE: Vector3 = Vector3.New(8, 1, 8)

local platform: Instance = Instance.New("Part", world)
platform.Name = PART_NAME
platform.Position = PART_POSITION
platform.Size = PART_SIZE
platform.Color = PART_COLOR
platform.Anchored = true

print(string.format(
	"Created %s at %s",
	platform.Name,
	tostring(platform.Position)
))
```
