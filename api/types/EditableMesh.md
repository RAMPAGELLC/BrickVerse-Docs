---
title: "EditableMesh"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/EditableMesh.svg" alt="EditableMesh icon" width="72"><figcaption></figcaption></figure>

# EditableMesh

**Inherits:** `RefCounted`

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### FixedSize

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### AutoCommit

**Type:** `boolean`

Documentation for this property is not yet available.

### Version

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### VertexCount

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### FaceCount

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### BoneCount

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### AddVertex(position)

#### Parameters

- `position`: `Vector3`

**Returns:** `number`

Documentation for this method is not yet available.

### AddTriangle(vertexId0, vertexId1, vertexId2)

#### Parameters

- `vertexId0`: `number`
- `vertexId1`: `number`
- `vertexId2`: `number`

**Returns:** `number`

Documentation for this method is not yet available.

### AddNormal(normal)

#### Parameters

- `normal`: `Vector3`

**Returns:** `number`

Documentation for this method is not yet available.

### AddAutomaticNormal()

**Returns:** `number`

Documentation for this method is not yet available.

### AddUV(uv)

#### Parameters

- `uv`: `Vector2`

**Returns:** `number`

Documentation for this method is not yet available.

### AddColor(color, alpha?)

#### Parameters

- `color`: [Color](./Color.md)
- `alpha`: `number` — optional — default: `1`

**Returns:** `number`

Documentation for this method is not yet available.

### AddBone(name, parentId?, transform?, isVirtual?)

#### Parameters

- `name`: `string`
- `parentId`: `number` — optional — default: `0`
- `transform`: `Transform3D` — optional
- `isVirtual`: `boolean` — optional — default: `False`

**Returns:** `number`

Documentation for this method is not yet available.

### RemoveFace(faceId)

#### Parameters

- `faceId`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### RemoveBone(boneId)

#### Parameters

- `boneId`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### SetPosition(vertexId, position)

#### Parameters

- `vertexId`: `number`
- `position`: `Vector3`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetPosition(vertexId)

#### Parameters

- `vertexId`: `number`

**Returns:** `Vector3`

Documentation for this method is not yet available.

### SetNormal(normalId, normal)

#### Parameters

- `normalId`: `number`
- `normal`: `Vector3`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetNormal(normalId)

#### Parameters

- `normalId`: `number`

**Returns:** `Vector3`

Documentation for this method is not yet available.

### ResetNormal(normalId)

#### Parameters

- `normalId`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### SetUV(uvId, uv)

#### Parameters

- `uvId`: `number`
- `uv`: `Vector2`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetUV(uvId)

#### Parameters

- `uvId`: `number`

**Returns:** `Vector2`

Documentation for this method is not yet available.

### SetColor(colorId, color)

#### Parameters

- `colorId`: `number`
- `color`: [Color](./Color.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### GetColor(colorId)

#### Parameters

- `colorId`: `number`

**Returns:** [Color](./Color.md)

Documentation for this method is not yet available.

### SetColorAlpha(colorId, alpha)

#### Parameters

- `colorId`: `number`
- `alpha`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetColorAlpha(colorId)

#### Parameters

- `colorId`: `number`

**Returns:** `number`

Documentation for this method is not yet available.

### GetVertices()

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetFaces()

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetNormals()

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetUVs()

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetColors()

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetBones()

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetFaceVertices(faceId)

#### Parameters

- `faceId`: `number`

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetFaceNormals(faceId)

#### Parameters

- `faceId`: `number`

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetFaceUVs(faceId)

#### Parameters

- `faceId`: `number`

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetFaceColors(faceId)

#### Parameters

- `faceId`: `number`

**Returns:** `{ number }`

Documentation for this method is not yet available.

### SetFaceVertices(faceId, vertexIds)

#### Parameters

- `faceId`: `number`
- `vertexIds`: `{ number }`

**Returns:** `nil`

Documentation for this method is not yet available.

### SetFaceNormals(faceId, normalIds)

#### Parameters

- `faceId`: `number`
- `normalIds`: `{ number }`

**Returns:** `nil`

Documentation for this method is not yet available.

### SetFaceUVs(faceId, uvIds)

#### Parameters

- `faceId`: `number`
- `uvIds`: `{ number }`

**Returns:** `nil`

Documentation for this method is not yet available.

### SetFaceColors(faceId, colorIds)

#### Parameters

- `faceId`: `number`
- `colorIds`: `{ number }`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetVertexFaceNormal(vertexId, faceId)

#### Parameters

- `vertexId`: `number`
- `faceId`: `number`

**Returns:** `number`

Documentation for this method is not yet available.

### GetVertexFaceUV(vertexId, faceId)

#### Parameters

- `vertexId`: `number`
- `faceId`: `number`

**Returns:** `number`

Documentation for this method is not yet available.

### GetVertexFaceColor(vertexId, faceId)

#### Parameters

- `vertexId`: `number`
- `faceId`: `number`

**Returns:** `number`

Documentation for this method is not yet available.

### SetVertexFaceNormal(vertexId, faceId, normalId)

#### Parameters

- `vertexId`: `number`
- `faceId`: `number`
- `normalId`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### SetVertexFaceUV(vertexId, faceId, uvId)

#### Parameters

- `vertexId`: `number`
- `faceId`: `number`
- `uvId`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### SetVertexFaceColor(vertexId, faceId, colorId)

#### Parameters

- `vertexId`: `number`
- `faceId`: `number`
- `colorId`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetVertexFaces(vertexId)

#### Parameters

- `vertexId`: `number`

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetAdjacentVertices(vertexId)

#### Parameters

- `vertexId`: `number`

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetAdjacentFaces(faceId)

#### Parameters

- `faceId`: `number`

**Returns:** `{ number }`

Documentation for this method is not yet available.

### FindClosestVertex(point)

#### Parameters

- `point`: `Vector3`

**Returns:** `number`

Documentation for this method is not yet available.

### FindVerticesWithinSphere(center, radius)

#### Parameters

- `center`: `Vector3`
- `radius`: `number`

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetCenter()

**Returns:** `Vector3`

Documentation for this method is not yet available.

### GetSize()

**Returns:** `Vector3`

Documentation for this method is not yet available.

### SetVertexBones(vertexId, boneIds)

#### Parameters

- `vertexId`: `number`
- `boneIds`: `{ number }`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetVertexBones(vertexId)

#### Parameters

- `vertexId`: `number`

**Returns:** `{ number }`

Documentation for this method is not yet available.

### SetVertexBoneWeights(vertexId, weights)

#### Parameters

- `vertexId`: `number`
- `weights`: `{ number }`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetVertexBoneWeights(vertexId)

#### Parameters

- `vertexId`: `number`

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetBoneName(boneId)

#### Parameters

- `boneId`: `number`

**Returns:** `string`

Documentation for this method is not yet available.

### SetBoneName(boneId, name)

#### Parameters

- `boneId`: `number`
- `name`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetBoneByName(name)

#### Parameters

- `name`: `string`

**Returns:** `number`

Documentation for this method is not yet available.

### GetBoneParent(boneId)

#### Parameters

- `boneId`: `number`

**Returns:** `number`

Documentation for this method is not yet available.

### SetBoneParent(boneId, parentBoneId)

#### Parameters

- `boneId`: `number`
- `parentBoneId`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetBoneTransform(boneId)

#### Parameters

- `boneId`: `number`

**Returns:** `Transform3D`

Documentation for this method is not yet available.

### SetBoneTransform(boneId, transform)

#### Parameters

- `boneId`: `number`
- `transform`: `Transform3D`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetBoneIsVirtual(boneId)

#### Parameters

- `boneId`: `number`

**Returns:** `boolean`

Documentation for this method is not yet available.

### SetBoneIsVirtual(boneId, isVirtual)

#### Parameters

- `boneId`: `number`
- `isVirtual`: `boolean`

**Returns:** `nil`

Documentation for this method is not yet available.

### MergeVertices(mergeTolerance)

#### Parameters

- `mergeTolerance`: `number`

**Returns:** `{ number }`

Documentation for this method is not yet available.

### RemoveUnused()

**Returns:** `{ number }`

Documentation for this method is not yet available.

### Triangulate()

**Returns:** `nil`

Documentation for this method is not yet available.

### IdDebugString(id)

#### Parameters

- `id`: `number`

**Returns:** `string`

Documentation for this method is not yet available.

### Destroy()

**Returns:** `nil`

Documentation for this method is not yet available.
