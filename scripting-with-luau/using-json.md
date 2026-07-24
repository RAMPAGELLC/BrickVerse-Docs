# Using JSON

JSON is a text format for structured data. BrickLua's built-in `json` object converts between JSON strings and BrickLua values.

Use:

- `json.serialize(value)` to create a JSON string;
- `json.parse(text)` to parse JSON into BrickLua values.

## Serialize a table

```lua
local profile = {
	username = "Builder",
	coins = 250,
	level = 5,
}

local encoded = json.serialize(profile)
print(encoded)
```

The result is a string similar to:

```json
{"username":"Builder","coins":250,"level":5}
```

## Parse JSON

```lua
local encoded = [[
{
	"username": "Builder",
	"coins": 250,
	"level": 5
}
]]

local profile = json.parse(encoded)

print(profile.username)
print(profile.coins)
```

## Supported values

JSON supports:

- objects;
- arrays;
- strings;
- numbers;
- booleans;
- null.

BrickLua maps objects and arrays to tables.

```lua
local data = {
	enabled = true,
	multiplier = 1.5,
	maps = {
		"Forest",
		"City",
	},
}
```

## Unsupported values

JSON cannot directly represent:

- Instances;
- functions;
- event connections;
- userdata without a JSON conversion;
- NaN;
- infinity;
- cyclic tables.

Convert BrickVerse values to simple tables:

```lua
local position = Vector3.New(10, 5, 20)

local encoded = json.serialize({
	x = position.X,
	y = position.Y,
	z = position.Z,
})
```

Reconstruct it:

```lua
local decoded = json.parse(encoded)
local position = Vector3.New(decoded.x, decoded.y, decoded.z)
```

## Error handling

Malformed JSON can throw an error:

```lua
local success, result = pcall(function()
	return json.parse('{"missing": true')
end)

if success then
	print(result)
else
	warn("Invalid JSON:", result)
end
```

Serialization can also fail:

```lua
local success, encoded = pcall(function()
	return json.serialize({
		instance = world,
	})
end)

if not success then
	warn("Could not serialize:", encoded)
end
```

## JSON arrays and objects

A sequential table is encoded as an array:

```lua
local maps = {
	"Forest",
	"Desert",
	"City",
}

print(json.serialize(maps))
```

A keyed table is encoded as an object:

```lua
local settings = {
	music = true,
	volume = 0.75,
}

print(json.serialize(settings))
```

Avoid mixing array indexes and named keys in the same table when producing JSON.

## Sending JSON with HTTP

```lua
local payload = json.serialize({
	serverId = world.ServerID,
	worldId = world.WorldID,
	players = world.PlayersConnected,
})

local headers = {
	["Content-Type"] = "application/json",
}

local success, response = pcall(function()
	return Http:PostAsync(
		"https://example.invalid/status",
		payload,
		headers
	)
end)

if not success then
	warn("Request failed:", response)
end
```

## Parsing an HTTP response

```lua
local success, body = pcall(function()
	return Http:GetAsync("https://example.invalid/config")
end)

if not success then
	warn("Request failed:", body)
	return
end

local parsedSuccess, data = pcall(function()
	return json.parse(body)
end)

if not parsedSuccess then
	warn("Server returned invalid JSON:", data)
	return
end

print(data.message)
```

## Store structured data

Datastores can save supported tables directly. You do not usually need to manually encode a table before calling `SetAsync`.

```lua
local Profiles = Datastore:GetDatastore("Profiles")

Profiles:SetAsync("player:123", {
	coins = 100,
	level = 2,
})
```

Manual JSON is useful when:

- sending an HTTP body;
- storing a single string format intentionally;
- debugging serialization;
- importing configuration;
- or interoperating with another system.

## Validate decoded data

Never assume external JSON has the expected shape:

```lua
local function parseItemDefinition(body: string)
	local success, value = pcall(function()
		return json.parse(body)
	end)

	if not success or type(value) ~= "table" then
		return nil
	end

	if type(value.id) ~= "string" then
		return nil
	end

	if type(value.price) ~= "number" then
		return nil
	end

	return {
		id = value.id,
		price = math.max(0, math.floor(value.price)),
		displayName = type(value.displayName) == "string"
			and value.displayName
			or value.id,
	}
end
```

## Pretty debugging

The serializer may produce compact output. For debugging, print important fields rather than depending on formatting:

```lua
local data = json.parse(body)

for key, value in pairs(data) do
	print(key, value)
end
```

## Complete configuration example

```lua
local DEFAULT_CONFIG = {
	roundDuration = 180,
	minPlayers = 2,
	maps = { "Forest" },
}

local function decodeConfig(body: string)
	local success, value = pcall(function()
		return json.parse(body)
	end)

	if not success or type(value) ~= "table" then
		return table.clone(DEFAULT_CONFIG)
	end

	return {
		roundDuration = type(value.roundDuration) == "number"
			and math.clamp(value.roundDuration, 30, 1800)
			or DEFAULT_CONFIG.roundDuration,

		minPlayers = type(value.minPlayers) == "number"
			and math.clamp(math.floor(value.minPlayers), 1, 100)
			or DEFAULT_CONFIG.minPlayers,

		maps = type(value.maps) == "table"
			and value.maps
			or table.clone(DEFAULT_CONFIG.maps),
	}
end
```
