---
title: "AddonObject"
description: ""
---

# AddonObject

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### Identifier

**Type:** `string`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### AddonName

**Type:** `string`

Documentation for this property is not yet available.

### AddonIcon

**Type:** [BVImageAsset](./BVImageAsset.md)

Documentation for this property is not yet available.

## Methods

### RequestPermissions(perms)

**Attributes:** Static · Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `perms`: { [AddonPermission](../enums/AddonPermission.md) }

**Returns:** `nil`

Documentation for this method is not yet available.

### CreateToolItem(txt)

#### Parameters

- `txt`: `string`

**Returns:** [AddonToolItem](./AddonToolItem.md)

Documentation for this method is not yet available.

## Events

### CleanupReceived(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
