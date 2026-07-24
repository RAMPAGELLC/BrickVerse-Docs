# Using Tags

Tags attach searchable labels to Instances. They are useful when objects share a role but are stored in different parts of the hierarchy.

Examples:

- `Collectible`
- `Checkpoint`
- `EnemySpawn`
- `DamageZone`
- `Interactable`
- `Saveable`

## Add a tag

```lua
local part = Instance.New("Part", world)
part:AddTag("Collectible")
```

## Check a tag

```lua
if part:HasTag("Collectible") then
	print(part.Name, "is collectible")
end
```

## Remove a tag

```lua
part:RemoveTag("Collectible")
```

## Read all tags

```lua
for _, tag in ipairs(part.Tags) do
	print(tag)
end
```

Prefer `AddTag` and `RemoveTag` for individual changes.

## Find a direct child with a tag

```lua
local collectible = world:FindChildWithTag("Collectible")

if collectible then
	print(collectible.Name)
end
```

## Get direct children with a tag

```lua
for _, checkpoint in ipairs(world:GetChildrenWithTag("Checkpoint")) do
	print(checkpoint.Name)
end
```

## Get tagged descendants

```lua
for _, collectible in ipairs(world:GetDescendantsWithTag("Collectible")) do
	print(collectible.Name)
end
```

This searches the entire descendant hierarchy.

## Tag-driven setup

```lua
local function setupCollectible(part: Instance)
	if not part:IsA("Part") then
		return
	end

	local collected = false

	part.Clicked:Connect(function(player)
		if collected then
			return
		end

		collected = true
		print(player.Name, "collected", part.Name)
		part:Destroy()
	end)
end

for _, instance in ipairs(world:GetDescendantsWithTag("Collectible")) do
	setupCollectible(instance)
end
```

## Detect newly added tagged objects

A simple approach is to watch hierarchy changes:

```lua
world.ChildAdded:Connect(function(child)
	if child:HasTag("Collectible") then
		setupCollectible(child)
	end
end)
```

For nested objects, watch the appropriate parent folders. Avoid rescanning every frame.

## Multiple tags

One Instance can have multiple tags:

```lua
part:AddTag("Interactable")
part:AddTag("Shop")
part:AddTag("SafeZone")
```

Check combinations:

```lua
if part:HasTag("Interactable") and part:HasTag("Shop") then
	print("This is an interactive shop")
end
```

## Tags versus names

Names identify an object:

```lua
local lobbySpawn = world:FindChild("LobbySpawn")
```

Tags identify a category:

```lua
local spawns = world:GetDescendantsWithTag("Spawn")
```

Use names for unique objects and tags for groups.

## Tags versus folders

Folders express hierarchy and ownership. Tags express behavior.

A checkpoint may be stored under a map Model while still being found through the `Checkpoint` tag.

```text
World
└── Map
    ├── Buildings
    └── Route
        ├── Checkpoint1 [Checkpoint]
        └── Checkpoint2 [Checkpoint]
```

## Damage zone example

```lua
local active: { [Instance]: boolean } = {}

local function setupDamageZone(zone: Instance)
	if not zone:IsA("Physical") then
		return
	end

	zone.Touched:Connect(function(other)
		local npc = other:FindAncestorByClass("NPC")

		if not npc or active[npc] then
			return
		end

		active[npc] = true
		npc:TakeDamage(10)

		task.delay(1, function()
			active[npc] = nil
		end)
	end)
end

for _, zone in ipairs(world:GetDescendantsWithTag("DamageZone")) do
	setupDamageZone(zone)
end
```

## Checkpoint example

```lua
local reached: { [Player]: { [string]: boolean } } = {}

local function setupCheckpoint(checkpoint: Instance)
	if not checkpoint:IsA("Part") then
		return
	end

	checkpoint.Clicked:Connect(function(player)
		reached[player] = reached[player] or {}

		if reached[player][checkpoint.Name] then
			return
		end

		reached[player][checkpoint.Name] = true
		print(player.Name, "reached", checkpoint.Name)
	end)
end

for _, checkpoint in ipairs(
	world:GetDescendantsWithTag("Checkpoint")
) do
	setupCheckpoint(checkpoint)
end

Players.PlayerRemoved:Connect(function(player)
	reached[player] = nil
end)
```

## Performance

Do not run a full descendant tag search every frame:

```lua
-- Avoid:
-- while true do
--     local objects = world:GetDescendantsWithTag("Enemy")
-- end
```

Discover objects during initialization and update your cached collection when the relevant hierarchy changes.

## Tag naming

Use consistent names:

```text
Collectible
Enemy
EnemySpawn
Checkpoint
DamageZone
Interactable
```

Avoid inconsistent variants such as `enemy`, `Enemies`, and `EnemyObject`.
