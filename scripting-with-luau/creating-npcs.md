# Creating NPCs

An `NPC` is a physical character controller with health, movement, navigation, appearance, tools, and character state.

## Create an NPC

```lua
local npc = Instance.New("NPC", world)
npc.Name = "Guard"
npc.Position = Vector3.New(0, 3, 10)
npc.DisplayName = "Guard"
```

## Configure movement and health

```lua
npc.MaxHealth = 100
npc.Health = 100
npc.WalkSpeed = 8
npc.JumpPower = 7
npc.UseNametag = true
npc.NametagVisibleRadius = 30
```

## Appearance

```lua
npc.HeadColor = Color.FromRGB(240, 200, 170)
npc.TorsoColor = Color.FromRGB(1, 135, 248)
npc.LeftArmColor = Color.FromRGB(240, 200, 170)
npc.RightArmColor = Color.FromRGB(240, 200, 170)
npc.LeftLegColor = Color.FromRGB(40, 50, 65)
npc.RightLegColor = Color.FromRGB(40, 50, 65)
```

Load an existing user's appearance:

```lua
npc:LoadAppearance("123456")
```

Clear it:

```lua
npc:ClearAppearance()
```

## Direct movement

```lua
npc:Move(Vector3.New(0, 0, 1))
```

Stop:

```lua
npc:Move(Vector3.Zero)
```

Jump:

```lua
if npc.IsOnGround then
	npc:Jump()
end
```

## Navigation

Set a destination:

```lua
npc:SetNavDestination(Vector3.New(20, 0, 20))
```

Check status:

```lua
print(npc.NavDestinationValid)
print(npc.NavDestinationDistance)
print(npc.NavDestinationReached)
```

Listen for completion:

```lua
npc.NavFinished:Connect(function()
	print(npc.Name, "finished navigating")
end)
```

## Patrol route

Create Parts tagged `PatrolPoint` and name them in route order:

```lua
local points = world:GetDescendantsWithTag("PatrolPoint")

table.sort(points, function(a, b)
	return a.Name < b.Name
end)
```

Patrol:

```lua
local index = 1

local function moveToNextPoint()
	if #points == 0 or npc.IsDead then
		return
	end

	local point = points[index]
	index = index % #points + 1

	npc:SetNavDestination(point.Position)
end

npc.NavFinished:Connect(moveToNextPoint)
moveToNextPoint()
```

## Health

Damage:

```lua
npc:TakeDamage(20)
```

Heal:

```lua
npc:Heal(15)
```

Kill:

```lua
npc:Kill()
```

Death event:

```lua
npc.Died:Connect(function()
	print(npc.Name, "died")
end)
```

## Respawn

```lua
npc:Respawn()
```

A simple respawn:

```lua
local spawnPosition = npc.Position

npc.Died:Connect(function()
	task.delay(5, function()
		npc.Position = spawnPosition
		npc:Respawn()
	end)
end)
```

## Equip a Tool

```lua
local swordTemplate = serverTools:WaitChild("GuardSword")
local sword = swordTemplate:Clone()

npc:EquipTool(sword)
```

Drop it:

```lua
npc:DropTool()
```

## Move target

```lua
npc.MoveTarget = targetPart
```

Use navigation for pathfinding and `MoveTarget` where the intended behavior matches the current API.

## Interaction prompt

Create a prompt under or near the NPC:

```lua
local prompt = Instance.New("InteractionPrompt", npc)
prompt.Name = "TalkPrompt"
prompt.Title = "Guard"
prompt.Subtitle = "Talk"
prompt.MaxDistance = 8
prompt.ActivationTime = 0
prompt.RequireFacing = true

prompt.Interacted:Connect(function(player)
	print(player.Name, "talked to", npc.Name)
end)
```

The server should validate the conversation state and rewards.

## Basic enemy AI

```lua
local DETECTION_RADIUS = 30
local ATTACK_RANGE = 4
local DAMAGE = 15
local ATTACK_COOLDOWN = 1.2

local lastAttack = 0

local function getClosestPlayer(): Player?
	local closest = nil
	local closestDistance = DETECTION_RADIUS

	for _, player in ipairs(Players:GetPlayers()) do
		if player.IsDead then
			continue
		end

		local distance = Vector3.Distance(
			npc.Position,
			player.Position
		)

		if distance < closestDistance then
			closest = player
			closestDistance = distance
		end
	end

	return closest
end

task.spawn(function()
	while not npc.IsDead do
		local target = getClosestPlayer()

		if not target then
			task.wait(0.25)
			continue
		end

		local distance = Vector3.Distance(
			npc.Position,
			target.Position
		)

		if distance > ATTACK_RANGE then
			npc:SetNavDestination(target.Position)
		else
			local now = os.clock()

			if now - lastAttack >= ATTACK_COOLDOWN then
				lastAttack = now
				target:TakeDamage(DAMAGE)
			end
		end

		task.wait(0.1)
	end
end)
```

{% hint style="warning" %}
For large numbers of NPCs, avoid running a separate tight loop for every NPC. Use a centralized update system and lower-frequency decisions.
{% endhint %}

## Cleanup

```lua
npc.Destroying:Connect(function()
	-- Disconnect external listeners and remove cached references.
end)
```

Remove NPC references from manager tables after destruction.
