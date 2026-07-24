# Working with Players

The global `Players` service manages connected players.

## Get all players

```lua
for _, player in ipairs(Players:GetPlayers()) do
	print(player.Name, player.UserID)
end
```

`PlayersCount` reports the number of connected players:

```lua
print("Players online:", Players.PlayersCount)
print("Server capacity:", Players.MaxPlayers)
```

## Player join and leave events

```lua
Players.PlayerAdded:Connect(function(player)
	print(player.Name, "joined")
end)

Players.PlayerRemoved:Connect(function(player)
	print(player.Name, "left")
end)
```

Handle players who are already connected when a script starts:

```lua
local function setupPlayer(player: Player)
	print("Setting up", player.Name)
end

for _, player in ipairs(Players:GetPlayers()) do
	setupPlayer(player)
end

Players.PlayerAdded:Connect(setupPlayer)
```

## Find a player

By username:

```lua
local player = Players:GetPlayer("Builder")
```

By user ID:

```lua
local player = Players:GetPlayerByID("123456")
```

Check the result:

```lua
if player then
	print(player.Name)
end
```

## The local player

A `ClientScript` can access:

```lua
local player = Players.LocalPlayer
print("Running for", player.Name)
```

Do not use `Players.LocalPlayer` as server logic.

## Player properties

Useful player properties include:

```lua
print(player.UserID)
print(player.NetworkPing)
print(player.UserPlatform)
print(player.IsAdmin)
print(player.IsCreator)
print(player.HasVerifiedBadge)
```

Movement properties can be configured by the server:

```lua
player.WalkSpeed = 10
player.SprintSpeed = 18
player.JumpPower = 8
player.CanMove = true
```

Stamina:

```lua
player.UseStamina = true
player.MaxStamina = 100
player.Stamina = 100
player.StaminaRegen = 10
player.StaminaBurn = 15
```

## Health and damage

`Player` inherits NPC health behavior:

```lua
player.MaxHealth = 100
player.Health = 100
```

Apply server-authoritative damage:

```lua
local function applyDamage(player: Player, amount: number)
	if amount <= 0 or player.IsDead then
		return
	end

	player:TakeDamage(math.clamp(amount, 0, 100))
end
```

Heal:

```lua
player:Heal(25)
```

Kill:

```lua
player:Kill()
```

## Respawning

```lua
player.RespawnTime = 5
player:Respawn()
```

Listen for a respawn:

```lua
player.Respawned:Connect(function()
	print(player.Name, "respawned")
end)
```

## Chat

```lua
player.Chatted:Connect(function(message)
	print(player.Name .. ":", message)
end)
```

Do not use raw chat text for public UI without applying the platform's filtering and moderation requirements.

## Kicking

```lua
player:Kick("You were removed from this server.")
```

Only kick from trusted server logic.

## Teams

```lua
player.TeamChanged:Connect(function(team)
	if team then
		print(player.Name, "joined", team.Name)
	end
end)
```

Assigning a Team depends on the Team objects configured in the World:

```lua
local redTeam = Teams:FindChild("Red")

if redTeam then
	player.Team = redTeam
end
```

## Character and appearance

A Player inherits character-related behavior:

```lua
player:LoadAppearance(player.UserID)
player:ClearAppearance()
player:ResetAppearance()
```

The current character model is available through:

```lua
local character = player.Character

if character then
	print(character.Name)
end
```

The character may be replaced when the player respawns. Do not permanently cache it without updating the reference.

## Tools

```lua
local tool = Instance.New("Tool")
tool.Name = "Flashlight"
tool.Parent = player.Backpack
```

Equip:

```lua
player:EquipTool(tool)
```

Unequip:

```lua
player:UnequipTool()
```

## Session data

Store temporary server state in a table:

```lua
type Session = {
	coins: number,
	level: number,
	joinedAt: number,
}

local sessions: { [Player]: Session } = {}

local function setupPlayer(player: Player)
	sessions[player] = {
		coins = 0,
		level = 1,
		joinedAt = os.time(),
	}
end

local function removePlayer(player: Player)
	local session = sessions[player]

	if session then
		print(player.Name, "left with", session.coins, "coins")
	end

	sessions[player] = nil
end

for _, player in ipairs(Players:GetPlayers()) do
	setupPlayer(player)
end

Players.PlayerAdded:Connect(setupPlayer)
Players.PlayerRemoved:Connect(removePlayer)
```

## Player-specific cooldowns

```lua
local lastAction: { [Player]: number } = {}
local COOLDOWN = 2

local function canAct(player: Player): boolean
	local now = os.clock()
	local previous = lastAction[player] or 0

	if now - previous < COOLDOWN then
		return false
	end

	lastAction[player] = now
	return true
end

Players.PlayerRemoved:Connect(function(player)
	lastAction[player] = nil
end)
```

## Complete welcome setup

```lua
local function setupPlayer(player: Player)
	player.MaxHealth = 100
	player.Health = 100
	player.WalkSpeed = 10
	player.SprintSpeed = 18
	player.UseStamina = true
	player.MaxStamina = 100
	player.Stamina = 100

	player.Chatted:Connect(function(message)
		print(string.format("[%s] %s", player.Name, message))
	end)

	player.Respawned:Connect(function()
		player.Health = player.MaxHealth
		print(player.Name, "is ready")
	end)

	print("Welcome", player.Name)
end

for _, player in ipairs(Players:GetPlayers()) do
	setupPlayer(player)
end

Players.PlayerAdded:Connect(setupPlayer)
```
