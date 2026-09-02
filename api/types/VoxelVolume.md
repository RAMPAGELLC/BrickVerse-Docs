---
title: "VoxelVolume"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/VoxelVolume.svg" alt="VoxelVolume icon" width="72"><figcaption></figcaption></figure>

# VoxelVolume

**Inherits:** [Entity](./Entity.md)

## Properties

### Dimensions

**Type:** `Vector3I`

Documentation for this property is not yet available.

### CellSize

**Type:** `number`

Documentation for this property is not yet available.

### AutoRebuild

**Type:** `boolean`

Documentation for this property is not yet available.

### CollisionEnabled

**Type:** `boolean`

Documentation for this property is not yet available.

### VoxelData

**Type:** `buffer`

Documentation for this property is not yet available.

### PaletteData

**Type:** `buffer`

Documentation for this property is not yet available.

### FilledCellCount

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### TriangleCount

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### Color

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### CastShadows

**Type:** `boolean`

Documentation for this property is not yet available.

## Methods

### GetVoxel(x, y, z)

#### Parameters

- `x`: `number`
- `y`: `number`
- `z`: `number`

**Returns:** `number`

Documentation for this method is not yet available.

### SetVoxel(x, y, z, paletteIndex)

#### Parameters

- `x`: `number`
- `y`: `number`
- `z`: `number`
- `paletteIndex`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### FillBox(position, size, paletteIndex)

#### Parameters

- `position`: `Vector3I`
- `size`: `Vector3I`
- `paletteIndex`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### FillSphere(center, radius, paletteIndex)

#### Parameters

- `center`: `Vector3`
- `radius`: `number`
- `paletteIndex`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### Clear()

**Returns:** `nil`

Documentation for this method is not yet available.

### GetPaletteColor(paletteIndex)

#### Parameters

- `paletteIndex`: `number`

**Returns:** [Color](./Color.md)

Documentation for this method is not yet available.

### SetPaletteColor(paletteIndex, color)

#### Parameters

- `paletteIndex`: `number`
- `color`: [Color](./Color.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### BeginEdit()

**Returns:** `nil`

Documentation for this method is not yet available.

### EndEdit()

**Returns:** `nil`

Documentation for this method is not yet available.

### Commit()

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### Changed(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### Rebuilt(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
