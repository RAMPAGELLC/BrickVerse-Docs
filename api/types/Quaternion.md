---
title: "Quaternion"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/Quaternion.svg" alt="Quaternion icon" width="72"><figcaption></figcaption></figure>

# Quaternion

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### X

**Type:** `number`

Documentation for this property is not yet available.

### Y

**Type:** `number`

Documentation for this property is not yet available.

### Z

**Type:** `number`

Documentation for this property is not yet available.

### W

**Type:** `number`

Documentation for this property is not yet available.

### Identity

**Type:** [Quaternion](./Quaternion.md)

**Attributes:** Static · Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### New()

**Attributes:** Static

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### New(x, y, z, w)

**Attributes:** Static

#### Parameters

- `x`: `number`
- `y`: `number`
- `z`: `number`
- `w`: `number`

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### Angle(a, b)

**Attributes:** Static · Semi-static

#### Parameters

- `a`: [Quaternion](./Quaternion.md)
- `b`: [Quaternion](./Quaternion.md)

**Returns:** `number`

Documentation for this method is not yet available.

### AngleAxis(angle, axis)

**Attributes:** Static

#### Parameters

- `angle`: `number`
- `axis`: [Vector3](./Vector3.md)

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### Dot(a, b)

**Attributes:** Static · Semi-static

#### Parameters

- `a`: [Quaternion](./Quaternion.md)
- `b`: [Quaternion](./Quaternion.md)

**Returns:** `number`

Documentation for this method is not yet available.

### Euler(x, y, z)

**Attributes:** Static

#### Parameters

- `x`: `number`
- `y`: `number`
- `z`: `number`

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### Euler(euler)

**Attributes:** Static

#### Parameters

- `euler`: [Vector3](./Vector3.md)

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### ToEuler(euler)

**Attributes:** Static · Semi-static

#### Parameters

- `euler`: [Quaternion](./Quaternion.md)

**Returns:** [Vector3](./Vector3.md)

Documentation for this method is not yet available.

### FromToRotation(fromDirection, toDirection)

**Attributes:** Static

#### Parameters

- `fromDirection`: [Vector3](./Vector3.md)
- `toDirection`: [Vector3](./Vector3.md)

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### Inverse(rotation)

**Attributes:** Static · Semi-static

#### Parameters

- `rotation`: [Quaternion](./Quaternion.md)

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### Lerp(a, b, t)

**Attributes:** Static · Semi-static

#### Parameters

- `a`: [Quaternion](./Quaternion.md)
- `b`: [Quaternion](./Quaternion.md)
- `t`: `number`

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### LerpUnclamped(a, b, t)

**Attributes:** Static · Semi-static

#### Parameters

- `a`: [Quaternion](./Quaternion.md)
- `b`: [Quaternion](./Quaternion.md)
- `t`: `number`

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### LookRotation(forward)

**Attributes:** Static

#### Parameters

- `forward`: [Vector3](./Vector3.md)

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### LookRotation(forward, upwards)

**Attributes:** Static

#### Parameters

- `forward`: [Vector3](./Vector3.md)
- `upwards`: [Vector3](./Vector3.md)

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### Normalize(quaternion)

**Attributes:** Static · Semi-static

#### Parameters

- `quaternion`: [Quaternion](./Quaternion.md)

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### RotateTowards(from, to, maxDegreesDelta)

**Attributes:** Static · Semi-static

#### Parameters

- `from`: [Quaternion](./Quaternion.md)
- `to`: [Quaternion](./Quaternion.md)
- `maxDegreesDelta`: `number`

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### Slerp(a, b, t)

**Attributes:** Static · Semi-static

#### Parameters

- `a`: [Quaternion](./Quaternion.md)
- `b`: [Quaternion](./Quaternion.md)
- `t`: `number`

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.

### SlerpUnclamped(a, b, t)

**Attributes:** Static · Semi-static

#### Parameters

- `a`: [Quaternion](./Quaternion.md)
- `b`: [Quaternion](./Quaternion.md)
- `t`: `number`

**Returns:** [Quaternion](./Quaternion.md)

Documentation for this method is not yet available.
