# Your First Script

A script is a piece of BrickLua code that runs inside a World. BrickVerse provides three script types:

| Script type | Purpose |
| --- | --- |
| `ServerScript` | Runs on the authoritative server. |
| `ClientScript` | Runs for an individual player on their client. |
| `ModuleScript` | Contains reusable code loaded with `require`. |

This tutorial creates a simple server script, reads information from the World, and creates a Part.

## Create a ServerScript

In Creator, insert a `ServerScript` into the World and rename it to `WelcomeServer`.

Add the following code:

```lua
print("WelcomeServer started")
print("World:", world.WorldName)
print("Universe:", world.UniverseName)
```

When the server starts, the messages appear in the output console.

The global `world` object represents the current running World. It also contains useful read-only information such as:

- `WorldID`
- `UniverseID`
- `WorldName`
- `UniverseName`
- `ServerID`
- `UpTime`
- `PlayersConnected`

## Create your first Instance

BrickVerse objects are called Instances. Use `Instance.New` to create one.

```lua
local platform = Instance.New("Part")
platform.Name = "WelcomePlatform"
platform.Parent = world
```

The second argument can set the parent immediately:

```lua
local platform = Instance.New("Part", world)
platform.Name = "WelcomePlatform"
```

Parenting the Part to `world` places it in the active hierarchy.

## Configure the Part

A Part inherits positioning and physics properties from its base classes:

```lua
local platform = Instance.New("Part", world)

platform.Name = "WelcomePlatform"
platform.Position = Vector3.New(0, 2, 0)
platform.Size = Vector3.New(12, 1, 12)
platform.Anchored = true
platform.CanCollide = true
platform.Shape = PartShape.Brick
platform.Material = PartMaterial.SmoothPlastic
platform.Color = Color.FromRGB(1, 135, 248)
```

`Vector3.New` creates a three-dimensional value. `Color.FromRGB` creates a color from red, green, and blue values between 0 and 255.

## Read a property

Properties are accessed with a period:

```lua
print(platform.Name)
print(platform.Position)
print(platform.ClassName)
```

`ClassName` is read-only and reports the Instance's class.

## Call a method

Methods use a colon:

```lua
local copy = platform:Clone(world)
copy.Name = "SecondPlatform"
copy.Position = Vector3.New(0, 2, 15)
```

The colon passes the object as the method's first argument.

## Find Instances

Use hierarchy methods to locate existing objects:

```lua
local platform = world:FindChild("WelcomePlatform")

if platform then
	print("Found", platform.Name)
else
	warn("WelcomePlatform was not found")
end
```

`FindChild` returns immediately. It may return `nil` when the object does not exist.

Use `WaitChild` when an object may replicate or be created shortly after the script starts:

```lua
local platform = world:WaitChild("WelcomePlatform", 10)

if not platform then
	error("WelcomePlatform did not appear within 10 seconds")
end
```

## React to an event

Parts expose a `Touched` event:

```lua
platform.Touched:Connect(function(other)
	print(platform.Name, "was touched by", other.Name)
end)
```

The callback runs each time another Physical object begins touching the Part.

## A complete first script

```lua
print("Starting WelcomeServer")

local platform = Instance.New("Part", world)
platform.Name = "WelcomePlatform"
platform.Position = Vector3.New(0, 2, 0)
platform.Size = Vector3.New(12, 1, 12)
platform.Anchored = true
platform.CanCollide = true
platform.Shape = PartShape.Brick
platform.Material = PartMaterial.SmoothPlastic
platform.Color = Color.FromRGB(1, 135, 248)

platform.Touched:Connect(function(other)
	print(other.Name, "touched the welcome platform")
end)

print("WelcomePlatform created successfully")
```

## Common mistakes

### Using `Instance.new`

BrickVerse uses `Instance.New` with a capital `N`.

```lua
local part = Instance.New("Part")
```

### Forgetting to parent the object

An unparented Instance is not part of the active World hierarchy.

### Using a ClientScript for server-owned state

The client can be modified by the player. Create important World objects and authoritative game state from server scripts.

## Next step

Continue with **Variables and Types** to learn how BrickLua stores values and how BrickVerse types such as `Vector3` and `Color` work.
