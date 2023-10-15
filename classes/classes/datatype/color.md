---
description: Creates a new color, used for UI & Bricks. This is a function.
---

# Color

## Example

```
local MyPart = World.Brick
MyPart.Color = Color.new(255, 255, 255)
```

Inherited from [Dynamic](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic) Set

### Constructors <a href="#constructors" id="constructors"></a>

| **Color.new**( number red = 0, number green = 0, number blue = 0 )                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------- |
| Creates a Color with the given red, green, and blue components. The parameters for this function should be on the range \[0, 255]. |

| **Color.fromHex** ( string hex )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <p>Returns a new Color from a six- or three-character <a href="https://en.wikipedia.org/wiki/Hexadecimal">hexadecimal</a> format. A preceding octothorpe (#) is ignored, if present. This function interprets the given string as a typical web hex color in the format RRGGBB or RGB (shorthand for RRGGBB). For example, #FFAA00 produces an orange color, and is the same as #FA0.</p><p>The color returned can be converted back into hex using <code>Color:toHex</code>, although it is not guaranteed to return the exact same string as passed to this function.</p><p></p><pre><code>print(Color.fromHex("#FF0000")) --> 1, 0, 0
</code></pre> |

### Functions <a href="#functions" id="functions"></a>

| string **Color:ToHex** ( )                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <p>Converts the color to a six-character hexadecimal string representing the color in the format RRGGBB. It is not prefixed with an octothorpe (#), although this can be concatenated easily.</p><p>The returned string can be provided to <code>Color.fromHex</code> to produce the original color.</p><p></p><pre><code>print(Color.new(255,255,255):ToHex()) --> "FFFFFF"
</code></pre> |

### Properties <a href="#properties" id="properties"></a>

| number **Color.R**          |
| --------------------------- |
| The red value of the color. |

| number **Color.G**            |
| ----------------------------- |
| The green value of the color. |

| number **Color.B**           |
| ---------------------------- |
| The blue value of the color. |
