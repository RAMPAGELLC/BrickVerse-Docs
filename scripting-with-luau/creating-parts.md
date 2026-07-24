# Creating Parts

`Part` is a basic physical building object. It inherits hierarchy, transform, physics, and appearance behavior.

## Create a Part

```lua
local part = Instance.New("Part", world)
part.Name = "Platform"
```

## Position and size

```lua
part.Position = Vector3.New(0, 5, 0)
part.Size = Vector3.New(10, 1, 10)
part.Rotation = Vector3.New(0, 45, 0)
```

`Position`, `Size`, and `Rotation` come from the `Dynamic` base class.

## Anchor the Part

An anchored Part is not moved by physics:

```lua
part.Anchored = true
```

A dynamic Part can use gravity and forces:

```lua
part.Anchored = false
part.UseGravity = true
part.Mass = 5
```

## Collision

```lua
part.CanCollide = true
```

Collision layers and masks allow more precise rules:

```lua
part:SetCollisionLayer(1, true)
part:SetCollisionMask(1, true)
```

Check a layer:

```lua
if part:GetCollisionLayer(1) then
	print("Part is on collision layer 1")
end
```

## Shape

```lua
part.Shape = PartShape.Brick
```

Available shapes include Brick, Sphere, Cylinder, Cone, Wedge, Corner, Truss, Frame, Torus, and others.

Example:

```lua
local ball = Instance.New("Part", world)
ball.Shape = PartShape.Sphere
ball.Size = Vector3.New(3, 3, 3)
ball.Position = Vector3.New(0, 10, 0)
```

## Material and color

```lua
part.Material = PartMaterial.Metal
part.Color = Color.FromRGB(90, 100, 115)
```

Materials include SmoothPlastic, Brick, Concrete, Grass, Ice, Marble, Metal, Neon, Plastic, Sand, Stone, Wood, and others.

## Shadows

```lua
part.CastShadows = true
```

Disable shadows on small decorative objects when appropriate.

## Forces

A non-anchored Part can receive force:

```lua
part:AddForce(Vector3.Up * 50, ForceMode.Impulse)
```

Other methods include:

```lua
part:AddTorque(Vector3.New(0, 25, 0), ForceMode.Force)
part:AddForceAtPosition(
	Vector3.Up * 30,
	part.Position,
	ForceMode.Impulse
)
```

## Movement methods

For controlled physical movement:

```lua
part:MovePosition(Vector3.New(0, 5, 10))
part:MoveRotation(Vector3.New(0, 90, 0))
```

For direct transform changes:

```lua
part:Translate(Vector3.New(0, 0, 5))
part:Rotate(Vector3.New(0, 45, 0))
part:LookAt(Vector3.New(0, 3, 20))
```

## Touch detection

```lua
part.Touched:Connect(function(other)
	print("Touched by", other.Name)
end)

part.TouchEnded:Connect(function(other)
	print(other.Name, "left the Part")
end)
```

Get all currently touching Physical objects:

```lua
for _, touching in ipairs(part:GetTouching()) do
	print(touching.Name)
end
```

## Click interaction

```lua
part.Clicked:Connect(function(player)
	print(player.Name, "clicked", part.Name)
end)
```

Add a per-player cooldown for actions with value:

```lua
local lastClick = {}
local CLICK_COOLDOWN = 1

part.Clicked:Connect(function(player)
	local now = os.clock()
	local previous = lastClick[player] or 0

	if now - previous < CLICK_COOLDOWN then
		return
	end

	lastClick[player] = now
	print(player.Name, "activated the Part")
end)

Players.PlayerRemoved:Connect(function(player)
	lastClick[player] = nil
end)
```

## Clone a Part

```lua
local clone = part:Clone(world)
clone.Name = "PlatformCopy"
clone.Position = part.Position + Vector3.New(0, 0, 12)
```

Only archivable objects can be cloned:

```lua
part.Archivable = true
```

## Destroy a Part

```lua
part:Destroy()
```

Schedule destruction:

```lua
part:Destroy(5)
```

## Reusable platform function

```lua
local function createPlatform(
	name: string,
	position: Vector3,
	size: Vector3,
	color: Color
): Instance
	local platform = Instance.New("Part", world)
	platform.Name = name
	platform.Position = position
	platform.Size = size
	platform.Color = color
	platform.Anchored = true
	platform.CanCollide = true
	platform.Shape = PartShape.Brick
	platform.Material = PartMaterial.SmoothPlastic

	return platform
end

for index = 1, 5 do
	createPlatform(
		"Platform" .. index,
		Vector3.New(0, 2 + index * 2, index * 8),
		Vector3.New(8, 1, 8),
		Color.FromRGB(1, 135, 248)
	)
end
```

## Launch pad example

```lua
local launchPad = Instance.New("Part", world)
launchPad.Name = "LaunchPad"
launchPad.Position = Vector3.New(0, 1, 0)
launchPad.Size = Vector3.New(8, 1, 8)
launchPad.Anchored = true
launchPad.Material = PartMaterial.Neon
launchPad.Color = Color.FromRGB(0, 220, 150)

launchPad.Touched:Connect(function(other)
	if not other:IsA("Physical") then
		return
	end

	other:AddForce(Vector3.Up * 20, ForceMode.VelocityChange)
end)
```
