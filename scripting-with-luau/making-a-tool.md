# Making a Tool

A `Tool` is an item that an NPC or Player can hold, equip, activate, deactivate, and drop.

This tutorial creates a simple healing tool.

## Tool structure

```text
Tool
├── Part
├── ServerScript
└── ClientScript
```

The exact visual hierarchy depends on the item. The Tool itself inherits physical properties and can be positioned in the World.

## Create a Tool

```lua
local tool = Instance.New("Tool")
tool.Name = "Medkit"
tool.Droppable = true
tool.DropEquipCooldown = 1
```

Add a visible Part:

```lua
local body = Instance.New("Part", tool)
body.Name = "Body"
body.Size = Vector3.New(1.5, 0.5, 1.5)
body.Material = PartMaterial.SmoothPlastic
body.Color = Color.FromRGB(230, 235, 240)
body.CanCollide = false
```

## Give the Tool to a player

A Player exposes `Backpack` and `Inventory` hierarchies.

```lua
local function giveTool(player: Player, sourceTool: Tool)
	local copy = sourceTool:Clone()
	copy.Parent = player.Backpack
end
```

Keep the template in a server-only location.

## Equip and unequip events

```lua
tool.Equipped:Connect(function()
	print(tool.Name, "was equipped")
end)

tool.Unequipped:Connect(function()
	print(tool.Name, "was unequipped")
end)
```

`Holder` identifies the NPC or Player currently holding it:

```lua
local holder = tool.Holder

if holder then
	print("Held by", holder.Name)
end
```

## Activation

```lua
tool.Activated:Connect(function()
	print(tool.Name, "was activated")
end)

tool.Deactivated:Connect(function()
	print(tool.Name, "was deactivated")
end)
```

The server should decide the gameplay outcome.

## Server-authoritative medkit

Place a `ServerScript` under the Tool:

```lua
local tool = script.Parent
local HEAL_AMOUNT = 35
local COOLDOWN = 5

local lastUsed = 0

tool.Activated:Connect(function()
	local holder = tool.Holder

	if not holder then
		return
	end

	if not holder:IsA("NPC") then
		return
	end

	if holder.IsDead then
		return
	end

	local now = os.clock()

	if now - lastUsed < COOLDOWN then
		return
	end

	if holder.Health >= holder.MaxHealth then
		return
	end

	lastUsed = now
	holder:Heal(HEAL_AMOUNT)

	print(holder.Name, "used a medkit")
end)
```

This logic runs on the server and uses the actual Holder instead of trusting a client-supplied player.

## Limited-use tool

Use a value to track charges:

```lua
local charges = Instance.New("IntValue", tool)
charges.Name = "Charges"
charges.Value = 3
```

Consume a charge:

```lua
tool.Activated:Connect(function()
	if charges.Value <= 0 then
		return
	end

	local holder = tool.Holder

	if not holder or holder.IsDead then
		return
	end

	charges.Value -= 1
	holder:Heal(25)

	if charges.Value <= 0 then
		tool:Destroy()
	end
end)
```

## Play a Tool animation

```lua
tool:PlayAnimation("Use")
```

The animation name must exist for the Tool and character setup.

## Force equip

An NPC or Player can equip a Tool:

```lua
player:EquipTool(tool)
```

Drop the current Tool:

```lua
player:DropTool()
```

For Players, you can also use:

```lua
player:UnequipTool()
```

## Tool pickup Part

Create a World pickup that gives a copy:

```lua
local pickup = Instance.New("Part", world)
pickup.Name = "MedkitPickup"
pickup.Position = Vector3.New(0, 2, 0)
pickup.Size = Vector3.New(2, 1, 2)
pickup.Anchored = true
pickup.Material = PartMaterial.Neon
pickup.Color = Color.FromRGB(0, 220, 120)

local available = true

pickup.Clicked:Connect(function(player)
	if not available then
		return
	end

	available = false

	local copy = tool:Clone()
	copy.Parent = player.Backpack

	pickup.Visible = false
	pickup.CanCollide = false

	task.delay(10, function()
		available = true
		pickup.Visible = true
		pickup.CanCollide = true
	end)
end)
```

## Security rules

The client may request a Tool action, but the server should validate:

- the player owns or holds the Tool;
- the Tool is equipped;
- the cooldown has elapsed;
- the target is valid;
- the target is in range;
- the amount is within server-defined limits;
- and the action is allowed in the current game state.

## Complete flashlight behavior

```lua
local tool = script.Parent
local light = tool:FindDescendant("Body/SpotLight")
local enabled = false

tool.Activated:Connect(function()
	local holder = tool.Holder

	if not holder then
		return
	end

	enabled = not enabled

	if light then
		light.Enabled = enabled
	end
end)

tool.Unequipped:Connect(function()
	enabled = false

	if light then
		light.Enabled = false
	end
end)
```
