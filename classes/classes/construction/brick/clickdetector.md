---
description: This is a class you can insert to Bricks, Unique to it only.
---

# ClickDetector

## Properties

| Name    | Type    | Description        |
| ------- | ------- | ------------------ |
| Enabled | Boolean | If enabled or not. |

Inherited from [Dynamic](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic) Set

## Functions

| Name    | Type     | Description                                        |
| ------- | -------- | -------------------------------------------------- |
| OnClick | Function | Fires when player clicks and returns Player Object |

### Example

```lua
Universe.Workplace.Brick.ClickDetector.OnClick:Connect(function(Player)
    print(Player.Name.." Pressed the button")
end)
```

For full list of options under player seek to [https://developers.brickverse.co/bricklua-lua-references-manual/workplace/players](https://docs.brickverse.co/bricklua-lua-references-manual/workplace/players)
