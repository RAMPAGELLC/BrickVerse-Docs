# ScriptDynamic

## Properties

Inherited from [Dynamic ](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic)Set

| `string` LuaSource                                  | Script source. Can only be modified by same authority level, or higher. |
| --------------------------------------------------- | ----------------------------------------------------------------------- |
| `bool` `readonly` `internalonly` ScriptName         | Internal Dynamic Script Name                                            |
| `bool` `readonly` `internalonly` scriptThreadActive | Internal status if script is actively running.                          |
| `bool` `internalonly` timeSince                     | Delta time of the script been operating.                                |
| `bool` `readonly` Local                             | if it's a local script.                                                 |
| `bool` `readonly` CoreScript                        | If it's a core script.                                                  |

