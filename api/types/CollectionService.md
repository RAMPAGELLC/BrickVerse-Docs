---
title: "CollectionService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/CollectionService.svg" alt="CollectionService icon" width="72"><figcaption></figcaption></figure>

# CollectionService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `CollectionService`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Methods

### GetTagged(tag)

#### Parameters

- `tag`: `string`

**Returns:** { [Instance](./Instance.md) }

Documentation for this method is not yet available.

### GetAllTags()

**Returns:** `{ string }`

Documentation for this method is not yet available.

### AddTag(instance, tag)

#### Parameters

- `instance`: [Instance](./Instance.md)
- `tag`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### RemoveTag(instance, tag)

#### Parameters

- `instance`: [Instance](./Instance.md)
- `tag`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### HasTag(instance, tag)

#### Parameters

- `instance`: [Instance](./Instance.md)
- `tag`: `string`

**Returns:** `boolean`

Documentation for this method is not yet available.

### GetTags(instance)

#### Parameters

- `instance`: [Instance](./Instance.md)

**Returns:** `{ string }`

Documentation for this method is not yet available.

## Events

### TagAdded(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### TagRemoved(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### TaggedInstanceEntered(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### TaggedInstanceExiting(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
