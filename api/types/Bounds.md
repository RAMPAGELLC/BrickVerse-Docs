---
title: "Bounds"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/Bounds.svg" alt="Bounds icon" width="72"><figcaption></figcaption></figure>

# Bounds

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### Center

**Type:** [Vector3](./Vector3.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### Size

**Type:** [Vector3](./Vector3.md)

Documentation for this property is not yet available.

### Extents

**Type:** [Vector3](./Vector3.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### Start

**Type:** [Vector3](./Vector3.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### End

**Type:** [Vector3](./Vector3.md)

Documentation for this property is not yet available.

### Volume

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

**Returns:** [Bounds](./Bounds.md)

Documentation for this method is not yet available.

### New(position, size)

**Attributes:** Static

#### Parameters

- `position`: [Vector3](./Vector3.md)
- `size`: [Vector3](./Vector3.md)

**Returns:** [Bounds](./Bounds.md)

Documentation for this method is not yet available.

### ClosestPoint(bounds, point)

**Attributes:** Static · Semi-static

#### Parameters

- `bounds`: [Bounds](./Bounds.md)
- `point`: [Vector3](./Vector3.md)

**Returns:** [Vector3](./Vector3.md)

Documentation for this method is not yet available.

### Contains(bounds, point)

**Attributes:** Static · Semi-static

#### Parameters

- `bounds`: [Bounds](./Bounds.md)
- `point`: [Vector3](./Vector3.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

### Encapsulate(bounds, point)

**Attributes:** Static · Semi-static

#### Parameters

- `bounds`: [Bounds](./Bounds.md)
- `point`: [Vector3](./Vector3.md)

**Returns:** [Bounds](./Bounds.md)

Documentation for this method is not yet available.

### Expand(bounds, amount)

**Attributes:** Static · Semi-static

#### Parameters

- `bounds`: [Bounds](./Bounds.md)
- `amount`: `number`

**Returns:** [Bounds](./Bounds.md)

Documentation for this method is not yet available.

### Intersects(bounds, other)

**Attributes:** Static · Semi-static

#### Parameters

- `bounds`: [Bounds](./Bounds.md)
- `other`: [Bounds](./Bounds.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

### SetMinMax(bounds, min, max)

**Attributes:** Static · Semi-static

#### Parameters

- `bounds`: [Bounds](./Bounds.md)
- `min`: [Vector3](./Vector3.md)
- `max`: [Vector3](./Vector3.md)

**Returns:** [Bounds](./Bounds.md)

Documentation for this method is not yet available.

### Distance(bounds, point)

**Attributes:** Static · Semi-static

#### Parameters

- `bounds`: [Bounds](./Bounds.md)
- `point`: [Vector3](./Vector3.md)

**Returns:** `number`

Documentation for this method is not yet available.

### SqrDistance(bounds, point)

**Attributes:** Static · Semi-static

#### Parameters

- `bounds`: [Bounds](./Bounds.md)
- `point`: [Vector3](./Vector3.md)

**Returns:** `number`

Documentation for this method is not yet available.
