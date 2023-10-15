# Vector3

**Vector3** describes a [vector](https://en.wikipedia.org/wiki/Vector\_\(mathematics\_and\_physics\)) in 3D space, typically usually used as a point in 3D space or the dimensions of a rectangular prism. Vector3 supports basic component-based arithmetic operators: sum, difference, product, and quotient. These operations can be applied on the left or right hand side to either another Vector3 or a number. It also features functions for commonly used vector operations, such as cross and dot products.

Some example usages of Vector3 are the `Position`, `Rotation` and `Size` of `parts`. Learning to set these properties are among the first things many developers will learn:



```
local part = workspace.Partpart.Position = part.Position + Vector3.new(5, 20, 100) -- Moves a part by this much
```

Vector3 is commonly used when constructing other more complex 3D data types, namely `CFrame` and `Ray`. Many of these data types’ functions will use a Vector3 within their parameters, such as `CFrame:PointToObjectSpace` or `Ray:ClosestPoint`. CFrame arithmetic also supports Vector3 for addition/subtraction.
