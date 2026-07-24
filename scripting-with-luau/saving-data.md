# Saving Data

Use the global `Datastore` service to save data between sessions. Datastores are available only from server scripts.

{% hint style="danger" %}
Never load or save authoritative player data from a ClientScript.
{% endhint %}

## Open a datastore

```lua
local Profiles = Datastore:GetDatastore("Profiles")
```

The datastore name identifies a collection of keys. Keep names short, stable, and specific.

## Choose a key

Use a stable identifier such as the player's user ID:

```lua
local function getPlayerKey(player: Player): string
	return "player:" .. player.UserID
end
```

Do not use a display name as the primary key because names may change.

## Save a value

```lua
Profiles:SetAsync("player:123", {
	coins = 100,
	level = 3,
})
```

Supported datastore values should be composed of serializable data:

- `nil`
- booleans
- finite numbers
- strings
- tables containing supported values

Do not store Instances, functions, event connections, or cyclic tables.

## Load a value

```lua
local data = Profiles:GetAsync("player:123")

if data then
	print(data.coins)
else
	print("No saved profile")
end
```

## Remove a value

```lua
Profiles:RemoveAsync("player:123")
```

Use removal carefully. A deleted key may not be recoverable.

## Handle failures

Storage calls can fail. Wrap them with `pcall`:

```lua
local success, result = pcall(function()
	return Profiles:GetAsync("player:123")
end)

if success then
	print("Loaded", result)
else
	warn("Load failed:", result)
end
```

## Default profile

```lua
type Profile = {
	version: number,
	coins: number,
	level: number,
	inventory: { [string]: number },
}

local function createDefaultProfile(): Profile
	return {
		version = 1,
		coins = 0,
		level = 1,
		inventory = {},
	}
end
```

Validate loaded data before using it:

```lua
local function sanitizeProfile(value: any): Profile
	local profile = createDefaultProfile()

	if type(value) ~= "table" then
		return profile
	end

	if type(value.coins) == "number" then
		profile.coins = math.max(0, math.floor(value.coins))
	end

	if type(value.level) == "number" then
		profile.level = math.max(1, math.floor(value.level))
	end

	if type(value.inventory) == "table" then
		for itemId, amount in pairs(value.inventory) do
			if type(itemId) == "string" and type(amount) == "number" then
				profile.inventory[itemId] = math.max(0, math.floor(amount))
			end
		end
	end

	return profile
end
```

## Load players

```lua
local Profiles = Datastore:GetDatastore("Profiles")
local sessions: { [Player]: Profile } = {}

local function loadPlayer(player: Player)
	local key = "player:" .. player.UserID

	local success, stored = pcall(function()
		return Profiles:GetAsync(key)
	end)

	if not success then
		warn("Could not load " .. player.Name .. ": " .. tostring(stored))
		player:Kick("Your data could not be loaded. Please rejoin.")
		return
	end

	sessions[player] = sanitizeProfile(stored)
end
```

Kicking on load failure prevents a blank profile from overwriting valid data later.

## Save players

```lua
local function savePlayer(player: Player): boolean
	local profile = sessions[player]

	if not profile then
		return true
	end

	local key = "player:" .. player.UserID

	local success, reason = pcall(function()
		Profiles:SetAsync(key, profile)
	end)

	if not success then
		warn("Could not save " .. player.Name .. ": " .. tostring(reason))
		return false
	end

	return true
end
```

## Join and leave lifecycle

```lua
for _, player in ipairs(Players:GetPlayers()) do
	task.spawn(loadPlayer, player)
end

Players.PlayerAdded:Connect(function(player)
	task.spawn(loadPlayer, player)
end)

Players.PlayerRemoved:Connect(function(player)
	savePlayer(player)
	sessions[player] = nil
end)
```

## Avoid saving too often

Do not call `SetAsync` for every coin pickup or every frame. Update server memory and save at controlled points:

- player leaves;
- major checkpoint;
- timed autosave;
- server shutdown flow;
- important purchase completion.

## Autosave

```lua
local AUTOSAVE_INTERVAL = 120

task.spawn(function()
	while true do
		task.wait(AUTOSAVE_INTERVAL)

		for _, player in ipairs(Players:GetPlayers()) do
			task.spawn(savePlayer, player)
		end
	end
end)
```

Avoid starting overlapping saves for the same player. A production system should track whether a save is already active.

## Prevent invalid numeric values

JSON-compatible storage cannot safely represent NaN or infinity:

```lua
local function isFinite(value: number): boolean
	return value == value
		and value ~= math.huge
		and value ~= -math.huge
end
```

Validate before saving.

## Profile versioning

Add a version number:

```lua
local function migrateProfile(profile: table): Profile
	local version = profile.version or 0

	if version < 1 then
		profile.inventory = profile.inventory or {}
		profile.version = 1
	end

	return sanitizeProfile(profile)
end
```

## Full server example

```lua
local Profiles = Datastore:GetDatastore("Profiles")

type Profile = {
	version: number,
	coins: number,
	level: number,
	inventory: { [string]: number },
}

local profiles: { [Player]: Profile } = {}

local function defaultProfile(): Profile
	return {
		version = 1,
		coins = 0,
		level = 1,
		inventory = {},
	}
end

local function load(player: Player)
	local success, value = pcall(function()
		return Profiles:GetAsync("player:" .. player.UserID)
	end)

	if not success then
		warn(value)
		player:Kick("Unable to load your profile.")
		return
	end

	profiles[player] = type(value) == "table" and value or defaultProfile()
end

local function save(player: Player)
	local profile = profiles[player]

	if not profile then
		return
	end

	local success, reason = pcall(function()
		Profiles:SetAsync("player:" .. player.UserID, profile)
	end)

	if not success then
		warn("Save failed:", reason)
	end
end

for _, player in ipairs(Players:GetPlayers()) do
	task.spawn(load, player)
end

Players.PlayerAdded:Connect(function(player)
	task.spawn(load, player)
end)

Players.PlayerRemoved:Connect(function(player)
	save(player)
	profiles[player] = nil
end)
```
