# RunService

## Properties

Inherited from [Dynamic](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic) Set

## Functions

<table data-header-hidden data-full-width="false"><thead><tr><th>Name</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Description</td></tr><tr><td>OnFrame</td><td>Called every frame.</td></tr><tr><td>OnPhysics</td><td>Called every physic step.</td></tr></tbody></table>

## Usage example

```lua
game.Universe.RunService.OnFrame:Connect(function(delta)

end)

game.Universe.RunService.OnPhysics:Connect(function(delta)

end)
```
