# NetworkService

Internal service for connecting to Worlds.

## Properties

Inherited from [Dynamic](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic) Set

## Functions

<table data-header-hidden data-full-width="false"><thead><tr><th>Name</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>Description</td></tr><tr><td>JoinServer</td><td>Called every frame.</td></tr></tbody></table>

## Usage Example

JoinServer can only be called locally, and a user must be already connected to a server.

```lua
game.Universe.NetworkService:JoinServer(WorldId)
```
