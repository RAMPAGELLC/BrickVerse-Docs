# ViewportFrame

A **ViewportFrame** is a type of [`UI`](broken-reference) that can render 3D objects inside its bounds. This is a great way to display 3D objects/models in a 2D GUI space like a [`ScreenUI`](screenui.md). At the moment, no shadow or post effects are available. Neon and Glass `materials` will be rendered on lowest quality.

### Properties <a href="#properties-1" id="properties-1"></a>

| [`Color`](https://developer.roblox.com/en-us/api-reference/datatype/Color3) Ambient | The lighting hue applied to the area within the [`ViewportFrame`](viewportframe.md) |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |

| [`Camera`](broken-reference)  CurrentCamera | [`Camera`](broken-reference) that is used to render children objects |
| ------------------------------------------- | -------------------------------------------------------------------- |

| [`Color`](https://developer.roblox.com/en-us/api-reference/datatype/Color3) ImageColor | Determines how a rendered image will be colorized |
| -------------------------------------------------------------------------------------- | ------------------------------------------------- |

| [`float`](../../../../bricklua-coding-with-lua/learn-lua/numbers.md) ImageTransparency | Determines the transparency of the rendered image |
| -------------------------------------------------------------------------------------- | ------------------------------------------------- |

| [`Color`](../../datatype/color.md) LightColor | The color of the emitted light |
| --------------------------------------------- | ------------------------------ |

| [`Vector3`](../../datatype/vector3.md) LightDirection | A [`Vector3`](../../datatype/vector3.md) representing the direction of the light source from the position 0, 0, 0 |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |

Inherited from [Dynamic](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic) Set

Inherited from [UIObject ](broken-reference)Set
