---
description: The base class for a physical object
---

# Brick

## Properties

| Name         | Type    | Description                                                                                 |
| ------------ | ------- | ------------------------------------------------------------------------------------------- |
| Anchored     | Boolean | When true, the part does not react to gravity                                               |
| Mass         | Int     | The mass of the part                                                                        |
| Spawn        | Boolean | When true, players can spawn on top of this part when they connect or respawn to the world. |
| Transparency | Int     | The transparency of the part represented as a byte. (0 = opaque, 1= invisible)              |
| Color        | Color3  | RGB Color of the brick                                                                      |
| Model        | Mesh    | The 3D model that the brick will be                                                         |

Inherited from [Dynamic](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic) Set

Inherited from [BasePart](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic) Set\
