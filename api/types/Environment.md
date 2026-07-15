---
title: "Environment"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/Environment.svg" alt="Environment icon" width="72"><figcaption></figcaption></figure>

# Environment

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Environment`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### CurrentCamera

**Type:** [Camera](./Camera.md)

Documentation for this property is not yet available.

### Gravity

**Type:** [Vector3](./Vector3.md)

Documentation for this property is not yet available.

### PartDestroyHeight

**Type:** `number`

Documentation for this property is not yet available.

### AutoGenerateNavMesh

**Type:** `boolean`

Documentation for this property is not yet available.

## Methods

### Raycast(origin, direction, maxDistance?, ignoreList?)

#### Parameters

- `origin`: [Vector3](./Vector3.md)
- `direction`: [Vector3](./Vector3.md)
- `maxDistance`: `number` — optional — default: `10000`
- `ignoreList`: { [Instance](./Instance.md) } — optional

**Returns:** [RayResult](./RayResult.md)

Documentation for this method is not yet available.

### RaycastAll(origin, direction, maxDistance?, ignoreList?)

#### Parameters

- `origin`: [Vector3](./Vector3.md)
- `direction`: [Vector3](./Vector3.md)
- `maxDistance`: `number` — optional — default: `1000`
- `ignoreList`: { [Instance](./Instance.md) } — optional

**Returns:** { [RayResult](./RayResult.md) }

Documentation for this method is not yet available.

### OverlapSphere(origin, radius, ignoreList?)

#### Parameters

- `origin`: [Vector3](./Vector3.md)
- `radius`: `number`
- `ignoreList`: { [Instance](./Instance.md) } — optional

**Returns:** { [Instance](./Instance.md) }

Documentation for this method is not yet available.

### OverlapBox(pos, size, rot, ignoreList?)

#### Parameters

- `pos`: [Vector3](./Vector3.md)
- `size`: [Vector3](./Vector3.md)
- `rot`: [Vector3](./Vector3.md)
- `ignoreList`: { [Instance](./Instance.md) } — optional

**Returns:** { [Instance](./Instance.md) }

Documentation for this method is not yet available.

### RebuildNavMesh()

**Returns:** `nil`

Documentation for this method is not yet available.

### GetPointOnNavMesh(toPoint)

#### Parameters

- `toPoint`: [Vector3](./Vector3.md)

**Returns:** [Vector3](./Vector3.md)

Documentation for this method is not yet available.
