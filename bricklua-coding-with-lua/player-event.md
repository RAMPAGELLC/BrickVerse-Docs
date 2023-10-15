---
description: >-
  Here is a example how to create a event for listening when a client connects
  to your universe.
---

# Player Event

## Creating the event

{% embed url="https://docs.brickverse.co/bricklua-lua-references-manual/workplace/players" %}

We will use the PlayerConnected Event to listen when a player connects.

```lua
Universe.Players.PlayerConnected:Connect(function(Player)
    print(Player.Name.." says Hello World");
end)
```

Here this code will now execute when a player connects and prints.

## What's returned in player?

```lua
{
Name =  "BrickVerse", -- Username
UserId = 1, -- UserId
Character = Universe.Players:GetPlayerCharacterByUserId(self.UserId) -- Returns in-game character model
Avatar = Universe.Players:RenderPlayer(self.UserId) -- Returns render of player
Age = "13+" -- Returns if 13+ or <13.
}
```

