---
title: "TerrainWater"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/TerrainWater.svg" alt="TerrainWater icon" width="72"><figcaption></figcaption></figure>

# TerrainWater

**Inherits:** [Instance](./Instance.md)

## Properties

### Enabled

**Type:** `boolean`

Documentation for this property is not yet available.

### OceanEnabled

**Type:** `boolean`

Documentation for this property is not yet available.

### Size

**Type:** `Vector2`

Documentation for this property is not yet available.

### CellSize

**Type:** `number`

Documentation for this property is not yet available.

### WaterLevel

**Type:** `number`

Documentation for this property is not yet available.

### WaveHeight

**Type:** `number`

Documentation for this property is not yet available.

### WaveLength

**Type:** `number`

Documentation for this property is not yet available.

### WaveSpeed

**Type:** `number`

Documentation for this property is not yet available.

### WaveSteepness

**Type:** `number`

Documentation for this property is not yet available.

### WaveDirection

**Type:** `Vector2`

Documentation for this property is not yet available.

### ShorelineWidth

**Type:** `number`

Documentation for this property is not yet available.

### Transparency

**Type:** `number`

Documentation for this property is not yet available.

### Roughness

**Type:** `number`

Documentation for this property is not yet available.

### RefractionStrength

**Type:** `number`

Documentation for this property is not yet available.

### NormalStrength

**Type:** `number`

Documentation for this property is not yet available.

### TextureScale

**Type:** `number`

Documentation for this property is not yet available.

### FoamAmount

**Type:** `number`

Documentation for this property is not yet available.

### ShallowColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### DeepColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### FoamColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### SerialisedVoxels

**Type:** `string`

Documentation for this property is not yet available.

### SerialisedExclusions

**Type:** `string`

Documentation for this property is not yet available.

## Methods

### SetWave(direction, height, length, speed, steepness?)

#### Parameters

- `direction`: `Vector2`
- `height`: `number`
- `length`: `number`
- `speed`: `number`
- `steepness`: `number` — optional — default: `0.3`

**Returns:** `nil`

Documentation for this method is not yet available.

### FillWaterBlock(center, size)

#### Parameters

- `center`: `Vector3`
- `size`: `Vector3`

**Returns:** `nil`

Documentation for this method is not yet available.

### DrainWaterBlock(center, size)

#### Parameters

- `center`: `Vector3`
- `size`: `Vector3`

**Returns:** `nil`

Documentation for this method is not yet available.

### FillWaterBall(center, radius)

#### Parameters

- `center`: `Vector3`
- `radius`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### DrainWaterBall(center, radius)

#### Parameters

- `center`: `Vector3`
- `radius`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### FillWaterCylinder(center, height, radius)

#### Parameters

- `center`: `Vector3`
- `height`: `number`
- `radius`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### DrainWaterCylinder(center, height, radius)

#### Parameters

- `center`: `Vector3`
- `height`: `number`
- `radius`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### ClearVoxelWater()

**Returns:** `nil`

Documentation for this method is not yet available.

### GetWaterCellCount()

**Returns:** `number`

Documentation for this method is not yet available.

### HasVoxelWater(position)

#### Parameters

- `position`: `Vector3`

**Returns:** `boolean`

Documentation for this method is not yet available.

### GetWaterHeight(p, time?)

#### Parameters

- `p`: `Vector3`
- `time`: `number` — optional — default: `-1`

**Returns:** `number`

Documentation for this method is not yet available.

### GetWaterNormal(p, time?)

#### Parameters

- `p`: `Vector3`
- `time`: `number` — optional — default: `-1`

**Returns:** `Vector3`

Documentation for this method is not yet available.

### IsSubmerged(p)

#### Parameters

- `p`: `Vector3`

**Returns:** `boolean`

Documentation for this method is not yet available.

### AddExclusionBox(center, size, padding?)

#### Parameters

- `center`: `Vector3`
- `size`: `Vector3`
- `padding`: `number` — optional — default: `0`

**Returns:** `number`

Documentation for this method is not yet available.

### RemoveExclusion(id)

#### Parameters

- `id`: `number`

**Returns:** `boolean`

Documentation for this method is not yet available.

### RemoveExclusionAt(p)

#### Parameters

- `p`: `Vector3`

**Returns:** `boolean`

Documentation for this method is not yet available.

### ClearExclusions()

**Returns:** `nil`

Documentation for this method is not yet available.

### GetExclusionCount()

**Returns:** `number`

Documentation for this method is not yet available.
