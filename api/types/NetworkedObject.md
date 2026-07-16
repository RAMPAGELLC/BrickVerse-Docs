---
title: "NetworkedObject"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/NetworkedObject.svg" alt="NetworkedObject icon" width="72"><figcaption></figcaption></figure>

# NetworkedObject

**Inherited by:** [BaseAsset](./BaseAsset.md), [Instance](./Instance.md)

{% hint style="danger" %}
**Abstract object**

This object exists as a base for other objects and cannot be created or accessed directly.
{% endhint %}

## Properties

### Name

**Type:** `string`

Documentation for this property is not yet available.

### ClassName

**Type:** `string`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### Shared

**Type:** [ScriptSharedTable](./ScriptSharedTable.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### NetworkedObjectID

**Type:** `string`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### ObjectID

**Type:** `string`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### ExistInNetwork

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### IsA(className)

#### Parameters

- `className`: `string`

**Returns:** `boolean`

Documentation for this method is not yet available.

### Clone(parent?)

#### Parameters

- `parent`: [NetworkedObject](./NetworkedObject.md) — optional

**Returns:** [NetworkedObject](./NetworkedObject.md)

Documentation for this method is not yet available.

### Destroy(time?)

#### Parameters

- `time`: `number` — optional — default: `0`

**Returns:** `nil`

Documentation for this method is not yet available.

### Delete(time?)

#### Parameters

- `time`: `number` — optional — default: `0`

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### PropertyChanged(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### Renamed(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### TreeEntered(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### TreeExited(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### Destroying(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
