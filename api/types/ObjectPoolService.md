---
title: "ObjectPoolService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/ObjectPoolService.svg" alt="ObjectPoolService icon" width="72"><figcaption></figcaption></figure>

# ObjectPoolService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `ObjectPool`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Methods

### CreatePool(name, template, prewarmCount?, maximumSize?)

#### Parameters

- `name`: `string`
- `template`: [Instance](./Instance.md)
- `prewarmCount`: `number` — optional — default: `0`
- `maximumSize`: `number` — optional — default: `100`

**Returns:** `nil`

Documentation for this method is not yet available.

### Acquire(name, parent?)

#### Parameters

- `name`: `string`
- `parent`: [Instance](./Instance.md) — optional

**Returns:** [Instance](./Instance.md)

Documentation for this method is not yet available.

### Release(name, item)

#### Parameters

- `name`: `string`
- `item`: [Instance](./Instance.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

### Prewarm(name, count)

#### Parameters

- `name`: `string`
- `count`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetAvailableCount(name)

#### Parameters

- `name`: `string`

**Returns:** `number`

Documentation for this method is not yet available.

### GetActiveCount(name)

#### Parameters

- `name`: `string`

**Returns:** `number`

Documentation for this method is not yet available.

### GetPoolNames()

**Returns:** `{ string }`

Documentation for this method is not yet available.

### DestroyPool(name, destroyActive?)

#### Parameters

- `name`: `string`
- `destroyActive`: `boolean` — optional — default: `False`

**Returns:** `boolean`

Documentation for this method is not yet available.

## Events

### Acquired(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### Released(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### PoolCreated(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### PoolDestroyed(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
