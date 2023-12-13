# UserInputService



{% hint style="warning" %}
OnUserInput may act non-functional due to service revamp.
{% endhint %}

## Properties

Inherited from [Dynamic](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic) Set.

## Functions

| Name         | Type    | Description                 |
| ------------ | ------- | --------------------------- |
| OnUserInput  | Void    | Fires when input is pressed |
| IsKeyDown    | Boolean | Is current key down         |

## Example

```lua
game.Universe.UserInputService.OnUserInput(function(Input)
    if input == Enum.UserInput.A then
    end
end)
```

