---
title: "CreatorSelections"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/CreatorSelections.svg" alt="CreatorSelections icon" width="72"><figcaption></figcaption></figure>

# CreatorSelections

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Selections`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Methods

### Select(instance)

#### Parameters

- `instance`: [Instance](./Instance.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### SelectChild(instance)

#### Parameters

- `instance`: [Instance](./Instance.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### GetSelected()

**Returns:** { [Instance](./Instance.md) }

Documentation for this method is not yet available.

### Deselect(instance)

#### Parameters

- `instance`: [Instance](./Instance.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### SelectOnly(instance)

#### Parameters

- `instance`: [Instance](./Instance.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### DeselectAll()

**Returns:** `nil`

Documentation for this method is not yet available.

### HasSelected(instance)

#### Parameters

- `instance`: [Instance](./Instance.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

## Events

### Selected(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### Deselected(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
