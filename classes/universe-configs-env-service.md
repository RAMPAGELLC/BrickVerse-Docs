# Universe Configs / ENV Service

Universe Configs provide a simple way to store and retrieve configuration values for your experience without hardcoding them into your game. They are ideal for live configuration, feature flags, promo codes, event settings, balancing values, API endpoints, and other data that may need to change over time.

Unlike hardcoded constants, configs can be updated through the Creator Portal without publishing a new version of your experience.

***

## Creating Configs

Each universe can have **up to 100 configuration values**.

Configs are managed from the **Creator Portal** under your universe settings.

Some common uses include:

* Active promo codes
* Event configuration
* Feature flags
* XP or currency multipliers
* Shop rotations
* Seasonal settings
* Remote service endpoints

***

## Secret Configs

A config can optionally be marked as a **Secret**.

Secret configs behave similarly to environment variables:

* Their values are **never visible** in the Creator Portal after creation.
* They **cannot be fetched by clients**.
* They are only accessible from **server scripts**.

This makes them suitable for storing:

* API keys
* Webhook secrets
* Authentication tokens
* Private service credentials
* Internal server configuration

If a client attempts to access a secret config, the request will fail with a **403 Forbidden** error.

***

## Reading a Config

Both client and server scripts can retrieve standard configs using `ConfigService:GetConfigAsync()`.

```lua
local value = ConfigService:GetConfigAsync("PromoCode")
print(value)
```

Function signature:

```lua
ConfigService:GetConfigAsync(key: string)
```

If the requested config does not exist, the function will return an error.

***

## Reading Secret Configs

Server scripts can access secret configs exactly the same way:

```lua
local apiKey = ConfigService:GetConfigAsync("DiscordWebhook")
```

Attempting to do this from a client script will result in:

```
403 Forbidden
```

***

## Setting Config Values

Only **server scripts** are permitted to create or update configuration values at runtime.

```lua
ConfigService:SetConfigAsync("CurrentSeason", "Summer")
```

You may also store JSON data:

```lua
ConfigService:SetConfigAsync("GameSettings", {
    doubleXP = true,
    maxPlayers = 50,
    event = "Summer Festival"
})
```

Function signature:

```lua
ConfigService:SetConfigAsync(key: string, value: string | json)
```

Clients cannot call this API.

***

## Example: Promo Codes

```lua
local activeCode = ConfigService:GetConfigAsync("ActivePromoCode")

if playerInput == activeCode then
    -- Award the player
end
```

Updating the promo code in the Creator Portal immediately changes the value your game receives without requiring a new publish.

***

## Example: Feature Flags

```lua
local enabled = ConfigService:GetConfigAsync("HalloweenEvent")

if enabled then
    EnableHalloweenContent()
end
```

Feature flags make it easy to enable or disable content across all running servers.

***

## Limits

* Maximum of **100 configs** per universe.
* Config values may be strings or JSON.
* Secret configs are only readable by server scripts.
* Only server scripts may modify config values.

***

## Best Practices

* Store frequently changing game settings as configs instead of hardcoding them.
* Use Secret configs for any sensitive information.
* Keep config names descriptive (for example, `ActivePromoCode` instead of `Code1`).
* Group related settings into a single JSON config when appropriate to reduce the total number of configs used.
* Avoid exposing secrets to clients by proxying any required server functionality through secure Remote Events or server APIs.
