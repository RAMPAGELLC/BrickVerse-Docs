---
title: "Physical"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/Physical.svg" alt="Physical icon" width="72"><figcaption></figcaption></figure>

# Physical

**Inherits:** [Dynamic](./Dynamic.md)
**Inherited by:** [InteractionPrompt](./InteractionPrompt.md), [NPC](./NPC.md), [RigidBody](./RigidBody.md)

{% hint style="danger" %}
**Abstract object**

This object exists as a base for other objects and cannot be created or accessed directly.
{% endhint %}

## Properties

### Anchored

**Type:** `boolean`

Documentation for this property is not yet available.

### CanCollide

**Type:** `boolean`

Documentation for this property is not yet available.

### CollisionLayers

**Type:** `number`

Documentation for this property is not yet available.

### CollisionMask

**Type:** `number`

Documentation for this property is not yet available.

### Velocity

**Type:** [Vector3](./Vector3.md)

Documentation for this property is not yet available.

### AngularVelocity

**Type:** [Vector3](./Vector3.md)

Documentation for this property is not yet available.

## Methods

### SetNetworkAuthority(plr)

#### Parameters

- `plr`: [Player](./Player.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### SetCollisionLayer(layer, value)

#### Parameters

- `layer`: `number`
- `value`: `boolean`

**Returns:** `nil`

Documentation for this method is not yet available.

### SetCollisionMask(layer, value)

#### Parameters

- `layer`: `number`
- `value`: `boolean`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetCollisionLayer(layer)

#### Parameters

- `layer`: `number`

**Returns:** `boolean`

Documentation for this method is not yet available.

### GetCollisionMask(layer)

#### Parameters

- `layer`: `number`

**Returns:** `boolean`

Documentation for this method is not yet available.

### GetTouching()

**Returns:** { [Physical](./Physical.md) }

Documentation for this method is not yet available.

### MovePosition(position)

#### Parameters

- `position`: [Vector3](./Vector3.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### MoveRotation(rotation)

#### Parameters

- `rotation`: [Vector3](./Vector3.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### AddForce(force, mode?)

#### Parameters

- `force`: [Vector3](./Vector3.md)
- `mode`: [ForceMode](../enums/ForceMode.md) — optional — default: `Force`

**Returns:** `nil`

Documentation for this method is not yet available.

### AddTorque(force, mode?)

#### Parameters

- `force`: [Vector3](./Vector3.md)
- `mode`: [ForceMode](../enums/ForceMode.md) — optional — default: `Force`

**Returns:** `nil`

Documentation for this method is not yet available.

### AddForceAtPosition(force, position, mode?)

#### Parameters

- `force`: [Vector3](./Vector3.md)
- `position`: [Vector3](./Vector3.md)
- `mode`: [ForceMode](../enums/ForceMode.md) — optional — default: `Force`

**Returns:** `nil`

Documentation for this method is not yet available.

### AddRelativeForce(force, mode?)

#### Parameters

- `force`: [Vector3](./Vector3.md)
- `mode`: [ForceMode](../enums/ForceMode.md) — optional — default: `Force`

**Returns:** `nil`

Documentation for this method is not yet available.

### AddRelativeTorque(torque, mode?)

#### Parameters

- `torque`: [Vector3](./Vector3.md)
- `mode`: [ForceMode](../enums/ForceMode.md) — optional — default: `Force`

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### Touched(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### TouchEnded(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### MouseEnter(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### MouseExit(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### Clicked(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
