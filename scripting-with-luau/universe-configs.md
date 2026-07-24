# Universe Configs

Universe Configs provide live configuration values for a Universe. They are useful for values that may need to change without publishing a new build.

Use them for:

- feature flags;
- seasonal events;
- reward multipliers;
- promotional codes;
- balancing values;
- maintenance messages;
- service endpoints;
- and server-only secrets.

## Read a config

Configs can be read from server or client scripts:

```lua
local activeEvent = ConfigService:GetConfigAsync("ACTIVE_EVENT")
print(activeEvent)
```

A normal config may be returned to clients.

## Secret configs

A config can be marked as secret. Secret values:

- cannot be viewed after they are stored;
- cannot be fetched by clients;
- should only be read by a server script;
- and return a forbidden response when requested from a client.

Use secret configs for credentials and private server settings.

```lua
-- ServerScript only
local apiSecret = ConfigService:GetConfigAsync("MATCH_API_SECRET")
```

{% hint style="danger" %}
Do not copy a secret into ReplicatedStorage, PlayerGUI, a ClientScript, a NetworkEvent, or any other client-visible location.
{% endhint %}

## Set a config

Only server scripts can set Universe Config values:

```lua
ConfigService:SetConfigAsync("ACTIVE_EVENT", "SUMMER")
```

Values can be strings or JSON-compatible data:

```lua
ConfigService:SetConfigAsync("REWARD_CONFIG", {
	daily = 100,
	weekly = 750,
	multiplier = 1.25,
})
```

## Handle missing values

```lua
local function getConfigOrDefault(key: string, defaultValue: any): any
	local success, value = pcall(function()
		return ConfigService:GetConfigAsync(key)
	end)

	if not success then
		warn("Could not fetch config " .. key .. ": " .. tostring(value))
		return defaultValue
	end

	if value == nil then
		return defaultValue
	end

	return value
end
```

Use it:

```lua
local xpMultiplier = getConfigOrDefault("XP_MULTIPLIER", 1)
```

## Validate remote values

Configs are live data. Validate them before use:

```lua
local function getRewardMultiplier(): number
	local value = getConfigOrDefault("REWARD_MULTIPLIER", 1)

	if type(value) ~= "number" then
		return 1
	end

	return math.clamp(value, 0, 10)
end
```

## Feature flag

```lua
local tradingEnabled = getConfigOrDefault("TRADING_ENABLED", false)

if tradingEnabled == true then
	print("Trading is enabled")
else
	print("Trading is disabled")
end
```

## Seasonal event

```lua
local eventName = getConfigOrDefault("ACTIVE_EVENT", "NONE")

local EVENTS = {
	NONE = {
		rewardMultiplier = 1,
	},
	SUMMER = {
		rewardMultiplier = 1.5,
	},
	HALLOWEEN = {
		rewardMultiplier = 2,
	},
}

local eventConfig = EVENTS[eventName] or EVENTS.NONE
print("Reward multiplier:", eventConfig.rewardMultiplier)
```

## Promotional codes

Store non-secret code definitions as structured config:

```lua
local promoCodes = getConfigOrDefault("PROMO_CODES", {})

local function redeemCode(code: string)
	local definition = promoCodes[string.upper(code)]

	if not definition then
		return false, "Invalid code"
	end

	if definition.enabled ~= true then
		return false, "Code disabled"
	end

	return true, definition.reward
end
```

The server must still track whether each player already redeemed a code.

## Cache configs

Do not request the same config for every frame or every minor action. Cache values:

```lua
local Config = {
	rewardMultiplier = 1,
	tradingEnabled = false,
}

local function refreshConfig()
	Config.rewardMultiplier = getRewardMultiplier()
	Config.tradingEnabled =
		getConfigOrDefault("TRADING_ENABLED", false) == true
end

refreshConfig()
```

Refresh on a reasonable schedule:

```lua
task.spawn(function()
	while true do
		task.wait(60)
		refreshConfig()
	end
end)
```

## Separate config from saved player data

Use Universe Configs for operator-controlled settings.

Use Datastores for player progression and persistent game state.

| Data | Use |
| --- | --- |
| XP multiplier | Universe Config |
| Active event | Universe Config |
| Secret API token | Secret Universe Config |
| Player coins | Datastore |
| Player inventory | Datastore |
| Player settings | Datastore |

## Complete event configuration example

```lua
local DEFAULT_EVENT = {
	name = "NONE",
	rewardMultiplier = 1,
	bannerText = "",
}

local function loadEventConfig()
	local success, value = pcall(function()
		return ConfigService:GetConfigAsync("EVENT_CONFIG")
	end)

	if not success or type(value) ~= "table" then
		return table.clone(DEFAULT_EVENT)
	end

	return {
		name = type(value.name) == "string"
			and value.name
			or DEFAULT_EVENT.name,

		rewardMultiplier = type(value.rewardMultiplier) == "number"
			and math.clamp(value.rewardMultiplier, 0, 10)
			or DEFAULT_EVENT.rewardMultiplier,

		bannerText = type(value.bannerText) == "string"
			and value.bannerText
			or DEFAULT_EVENT.bannerText,
	}
end

local EventConfig = loadEventConfig()

print("Event:", EventConfig.name)
print("Multiplier:", EventConfig.rewardMultiplier)
```
