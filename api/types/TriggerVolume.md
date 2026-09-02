---
title: "TriggerVolume"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/TriggerVolume.svg" alt="TriggerVolume icon" width="72"><figcaption></figcaption></figure>

# TriggerVolume

**Inherits:** [Dynamic](./Dynamic.md)
**Inherited by:** [DamageVolume](./DamageVolume.md), [ForceVolume](./ForceVolume.md)

## Properties

### Enabled

**Type:** `boolean`

Documentation for this property is not yet available.

### CollisionMask

**Type:** `number`

Documentation for this property is not yet available.

### DetectPlayers

**Type:** `boolean`

Documentation for this property is not yet available.

### DetectNPCs

**Type:** `boolean`

Documentation for this property is not yet available.

### DetectEntities

**Type:** `boolean`

Documentation for this property is not yet available.

### OccupantCount

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### GetOccupants()

**Returns:** { [Physical](./Physical.md) }

Documentation for this method is not yet available.

### Contains(physical)

#### Parameters

- `physical`: [Physical](./Physical.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

## Events

### Entered(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### Exited(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
