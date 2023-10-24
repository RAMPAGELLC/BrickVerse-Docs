---
description: >-
  Here is a example how to create a event for listening when a client connects
  to your universe.
---

# Player Event

## Creating the event

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
    Character = -- Character
    Avatar = -- BrickThumb render
}
```

