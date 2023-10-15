# UserInputService

## Properties

Inherited from [Dynamic](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic) Set. This Class uses [Enum](https://docs.brickverse.co/bricklua-lua-references-manual/classes/enum).

## Functions

| Name       | Type | Description             |
| ---------- | ---- | ----------------------- |
| InputBegan | Void | Fires when input begins |
| InputEnded | Void | Fires when input ended  |

## Example

```lua
Universe:GetService("UserInputService").InputBegan(function(input)
    if input.UserInputType == Enum.UserInputType.Keyboard then
        if input.KeyCode == Enum.KeyCode.A then
            print(input.Player.Name.." has pressed 'A'");
        end
    end
end)
```

