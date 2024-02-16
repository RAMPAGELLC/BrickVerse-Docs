# CFrame

**CFrame**, short for **coordinate frame**, is a data type that describes a 3D position and orientation. It is made up of a **positional** component and a **rotational** component. It includes essential arithmetic operations for working with 3D data on BrickVerse.

```lua
local cf = CFrame.new(0, 5, 0) * CFrame.Angles(math.rad(45), 0, 0)
```

### Components <a href="#components" id="components"></a>

#### Positional <a href="#positional" id="positional"></a>

The positional component is available as a `Vector3` in the **Position** property. In addition, the components of a CFrame’s position are also available in the **X**, **Y** and **Z** properties like a Vector3. A CFrame placed at a specific position without any rotation can be constructed using `CFrame.new(Vector3)` or `CFrame.new(X, Y, Z)`.

#### Rotational <a href="#rotational" id="rotational"></a>

CFrame stores 3D rotation data in a 3-by-3 **rotation matrix**. These values are returned by the `CFrame:GetComponents` function after the X, Y and Z positional values. This matrix is used internally when doing [calculations involving rotations](https://en.wikipedia.org/wiki/Rotation\_matrix#Basic\_rotations). They use [radians](https://en.wikipedia.org/wiki/Radian) as their unit (for conversion to degrees, use `math.rad`/`math.deg`).

The matrix below represents the components of a CFrame’s rotation matrix and their relationship with the various vector properties available (LookVector, RightVector, etc). Although the individual components of the rotation matrix are rarely useful by themselves, the vector properties which derive from them are much more useful.



|             | **RightVector** | **UpVector** | **–LookVector†** |
| ----------- | --------------- | ------------ | ---------------- |
| **XVector** | R00             | R01          | R02              |
| **YVector** | R10             | R11          | R12              |
| **ZVector** | R20             | R21          | R22              |

### Constructors <a href="#constructors" id="constructors"></a>

| **CFrame.new** ( )               |
| -------------------------------- |
| Creates a blank identity CFrame. |

| **CFrame.new** ( Vector3 pos )                                               |
| ---------------------------------------------------------------------------- |
| Returns a CFrame with no rotation with the position of the provided Vector3. |

| **CFrame.new** ( number x, number y, number z ) |
| ----------------------------------------------- |
| Creates a CFrame from position (x, y, z).       |

| **CFrame.new** ( number x, number y, number z, number qX, number qY, number qZ, number qW ) |
| ------------------------------------------------------------------------------------------- |
| Creates a CFrame from position (x, y, z) and quaternion (qX, qY, qZ, qW).                   |

| **CFrame.new** ( number x, number y, number z, number R00, number R01, number R02, number R10, number R11, number R12, number R20, number R21, number R22 ) |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Creates a CFrame from position (x, y, z) with an orientation specified by the rotation matrix \[\[R00 R01 R02] \[R10 R11 R12] \[R20 R21 R22]].              |

| **CFrame.lookAt** ( Vector3 at, Vector3 lookAt, Vector3 up = Vector3.new(0, 1, 0) )                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Creates a new CFrame located at <code>at</code> and facing towards <code>lookAt</code>, optionally specifying the upward direction (by default, (0, 1, 0)).</p><p>This function replaces the <code>CFrame.new(Vector3, Vector3)</code> constructor (see above) which accomplished a similar task. This function allows you to specify the <code>up</code> Vector, using the same default as the old constructor.</p> |

| **CFrame.fromEulerAnglesXYZ** ( number rx, number ry, number rz )                                      |
| ------------------------------------------------------------------------------------------------------ |
| Creates a rotated CFrame using angles (rx, ry, rz) in radians. Rotations are applied in Z, Y, X order. |

| **CFrame.fromEulerAnglesYXZ** ( number rx, number ry, number rz )                                      |
| ------------------------------------------------------------------------------------------------------ |
| Creates a rotated CFrame using angles (rx, ry, rz) in radians. Rotations are applied in Y, X, Z order. |

| **CFrame.Angles** ( number rx, number ry, number rz ) |
| ----------------------------------------------------- |
| Equivalent to fromEulerAnglesXYZ.                     |

| **CFrame.fromOrientation** ( number rx, number ry, number rz ) |
| -------------------------------------------------------------- |
| Equivalent to fromEulerAnglesYXZ.                              |

| **CFrame.fromAxisAngle** ( Vector3 v, number r )                        |
| ----------------------------------------------------------------------- |
| Creates a rotated CFrame from a Unit Vector3 and a rotation in radians. |

| **CFrame.fromMatrix** ( Vector3 pos, Vector3 vX, Vector3 vY, Vector3 vZ )                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Creates a CFrame from a translation and the columns of a rotation matrix. If vz is excluded, the third column is calculated as \[vx:Cross(vy).Unit]. |

| **CFrame.Orthonormalize** ( )                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Returns an orthonormalized copy of the CFrame. The `BasePart.CFrame` property automatically applies orthonormalization, but other APIs which take CFrames do not, so this method will occasionally be necessary when when incrementally updating a CFrame and using it with them |

\
