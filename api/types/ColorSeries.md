---
title: "ColorSeries"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/ColorSeries.svg" alt="ColorSeries icon" width="72"><figcaption></figcaption></figure>

# ColorSeries

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### PointCount

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### New()

**Attributes:** Static

**Returns:** [ColorSeries](./ColorSeries.md)

Documentation for this method is not yet available.

### New(min, max)

**Attributes:** Static

#### Parameters

- `min`: [Color](./Color.md)
- `max`: [Color](./Color.md)

**Returns:** [ColorSeries](./ColorSeries.md)

Documentation for this method is not yet available.

### Clear()

**Returns:** `nil`

Documentation for this method is not yet available.

### SetColor(point, color)

#### Parameters

- `point`: `number`
- `color`: [Color](./Color.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### RemovePoint(point)

#### Parameters

- `point`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetOffsets()

**Returns:** `{ number }`

Documentation for this method is not yet available.

### GetColors()

**Returns:** { [Color](./Color.md) }

Documentation for this method is not yet available.

### SetOffset(point, offset)

#### Parameters

- `point`: `number`
- `offset`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetColor(point)

#### Parameters

- `point`: `number`

**Returns:** [Color](./Color.md)

Documentation for this method is not yet available.

### GetOffset(point)

#### Parameters

- `point`: `number`

**Returns:** `number`

Documentation for this method is not yet available.

### AddPoint(offset, color)

#### Parameters

- `offset`: `number`
- `color`: [Color](./Color.md)

**Returns:** `number`

Documentation for this method is not yet available.

### Lerp(t)

#### Parameters

- `t`: `number`

**Returns:** [Color](./Color.md)

Documentation for this method is not yet available.
