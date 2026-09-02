---
title: "DebrisService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/DebrisService.svg" alt="DebrisService icon" width="72"><figcaption></figcaption></figure>

# DebrisService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Debris`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### Count

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### AddItem(item, lifetime?)

#### Parameters

- `item`: [Instance](./Instance.md)
- `lifetime`: `number` — optional — default: `10`

**Returns:** `nil`

Documentation for this method is not yet available.

### Cancel(item)

#### Parameters

- `item`: [Instance](./Instance.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

### IsQueued(item)

#### Parameters

- `item`: [Instance](./Instance.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

### GetRemainingLifetime(item)

#### Parameters

- `item`: [Instance](./Instance.md)

**Returns:** `number`

Documentation for this method is not yet available.

### GetQueuedItems()

**Returns:** { [Instance](./Instance.md) }

Documentation for this method is not yet available.

### Clear(destroyItems?)

#### Parameters

- `destroyItems`: `boolean` — optional — default: `False`

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### ItemAdded(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### ItemCanceled(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### ItemExpired(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
