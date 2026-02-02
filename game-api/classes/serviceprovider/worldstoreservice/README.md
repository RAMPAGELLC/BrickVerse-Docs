# WorldStoreService

`WorldStoreService` is a useful services for saving data persistently like player inventories, player currency, etc.

## Examples

### Using WorldStoreService to load & save player inventory

```luau
local WorldStoreService = game:GetService("WorldStoreService")
local PlayerService = game:GetService("PlayerService")
local WebService = game:GetService("WebService")
local Store = WorldStoreService:GetStore("PlayerData")

local Inventories = {}

PlayerService.OnPlayerJoin:Connect(function(Player)
    -- Load their player data if it exists.
    local result = Store:GetAsync(Player.UserId)
    Inventories[Player.UserId] = result or {}
end)

PlayerService.OnPlayerLeave:Connect(function(Player)
    -- Save their player data.
    if Inventories[Player.UserId] then
        Store:SetAsync(Player.UserId, WebService:JSONEncode(Inventories[Player.UserId]), player.UserId)
    end
    
    Inventories[Player.UserId] = nil;
end)
```

## Properties

Inherited from [Dynamic](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic) Set

## Functions

|                                                              |
| ------------------------------------------------------------ |
| [`WorldStore`](worldstore.md) GetStore(**String** storeName) |
| Returns a new [`WorldStore`](worldstore.md) Instance         |
| `void` DeleteStore(**String** storeName)                     |
| Deletes a WorldStore on the Cloud                            |
