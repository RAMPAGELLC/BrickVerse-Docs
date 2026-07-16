---
title: "Terrain"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/Terrain.svg" alt="Terrain icon" width="72"><figcaption></figcaption></figure>

# Terrain

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Terrain`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### SerialisedTerrain

**Type:** `string`

Documentation for this property is not yet available.

### AutoSerialise

**Type:** `boolean`

Documentation for this property is not yet available.

### GenerateCollisions

**Type:** `boolean`

Documentation for this property is not yet available.

### DefaultSdfStrength

**Type:** `number`

Documentation for this property is not yet available.

### DefaultSdfScale

**Type:** `number`

Documentation for this property is not yet available.

### ViewDistance

**Type:** `number`

Documentation for this property is not yet available.

### BaseColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### GrassColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### StoneColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### SandColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### DirtColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### SnowColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### ConcreteColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### BrickColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

## Methods

### FillBall(center, radius, material?)

#### Parameters

- `center`: `Vector3`
- `radius`: `number`
- `material`: `number` — optional — default: `0`

**Returns:** `nil`

Documentation for this method is not yet available.

### DigBall(center, radius)

#### Parameters

- `center`: `Vector3`
- `radius`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### FillBlock(center, size, material?)

#### Parameters

- `center`: `Vector3`
- `size`: `Vector3`
- `material`: `number` — optional — default: `0`

**Returns:** `nil`

Documentation for this method is not yet available.

### DigBlock(center, size)

#### Parameters

- `center`: `Vector3`
- `size`: `Vector3`

**Returns:** `nil`

Documentation for this method is not yet available.

### FillCylinder(center, height, radius, material?)

#### Parameters

- `center`: `Vector3`
- `height`: `number`
- `radius`: `number`
- `material`: `number` — optional — default: `0`

**Returns:** `nil`

Documentation for this method is not yet available.

### DigCylinder(center, height, radius)

#### Parameters

- `center`: `Vector3`
- `height`: `number`
- `radius`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### PaintBall(center, radius, material, opacity?)

#### Parameters

- `center`: `Vector3`
- `radius`: `number`
- `material`: `number`
- `opacity`: `number` — optional — default: `1`

**Returns:** `nil`

Documentation for this method is not yet available.

### SmoothBall(center, radius, blurRadius?)

#### Parameters

- `center`: `Vector3`
- `radius`: `number`
- `blurRadius`: `number` — optional — default: `2`

**Returns:** `nil`

Documentation for this method is not yet available.

### GrowBall(center, radius, strength?)

#### Parameters

- `center`: `Vector3`
- `radius`: `number`
- `strength`: `number` — optional — default: `1`

**Returns:** `nil`

Documentation for this method is not yet available.

### ErodeBall(center, radius, strength?)

#### Parameters

- `center`: `Vector3`
- `radius`: `number`
- `strength`: `number` — optional — default: `1`

**Returns:** `nil`

Documentation for this method is not yet available.

### SetVoxelSdf(position, sdf)

#### Parameters

- `position`: `Vector3`
- `sdf`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetVoxelSdf(position)

#### Parameters

- `position`: `Vector3`

**Returns:** `number`

Documentation for this method is not yet available.

### SetVoxelMaterial(position, material)

#### Parameters

- `position`: `Vector3`
- `material`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetVoxelMaterial(position)

#### Parameters

- `position`: `Vector3`

**Returns:** `number`

Documentation for this method is not yet available.

### SetVoxelMetadata(position, metadata)

#### Parameters

- `position`: `Vector3`
- `metadata`: `Variant`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetVoxelMetadata(position)

#### Parameters

- `position`: `Vector3`

**Returns:** `Variant`

Documentation for this method is not yet available.

### IsAreaEditable(minimum, maximum)

#### Parameters

- `minimum`: `Vector3`
- `maximum`: `Vector3`

**Returns:** `boolean`

Documentation for this method is not yet available.

### CountOperations()

**Returns:** `number`

Documentation for this method is not yet available.

### SaveTerrain()

**Returns:** `string`

Documentation for this method is not yet available.

### LoadSerialisedTerrain()

**Returns:** `nil`

Documentation for this method is not yet available.

### Clear()

**Returns:** `nil`

Documentation for this method is not yet available.
