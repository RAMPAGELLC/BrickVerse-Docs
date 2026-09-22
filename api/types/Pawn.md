---
title: "Pawn"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/Pawn.svg" alt="Pawn icon" width="72"><figcaption></figcaption></figure>

# Pawn

**Inherits:** [CharacterModel](./CharacterModel.md)

## Properties

### CollisionShapeType

**Type:** [PawnCollisionShape](../enums/PawnCollisionShape.md)

Documentation for this property is not yet available.

### CollisionSize

**Type:** `Vector3`

Documentation for this property is not yet available.

### CollisionOffset

**Type:** `Vector3`

Documentation for this property is not yet available.

### Controller

**Type:** [Player](./Player.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsLocallyControlled

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### Velocity

**Type:** `Vector3`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### Health

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsOnGround

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### InputVector

**Type:** `Vector2`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### JumpPressed

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### SprintPressed

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### ControlMode

**Type:** [PlayerMovementMode](../enums/PlayerMovementMode.md)

Documentation for this property is not yet available.

### CameraAttachment

**Type:** [Dynamic](./Dynamic.md)

Documentation for this property is not yet available.

### ToolAttachment

**Type:** [Dynamic](./Dynamic.md)

Documentation for this property is not yet available.

## Methods

### GetAttachment(attachmentEnum)

#### Parameters

- `attachmentEnum`: [CharacterAttachment](../enums/CharacterAttachment.md)

**Returns:** [Dynamic](./Dynamic.md)

Documentation for this method is not yet available.

### Possess(player)

#### Parameters

- `player`: [Player](./Player.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### Unpossess()

**Returns:** `nil`

Documentation for this method is not yet available.

### Move(velocity)

#### Parameters

- `velocity`: `Vector3`

**Returns:** `nil`

Documentation for this method is not yet available.

### Jump()

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### Possessed(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### Unpossessed(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### ControlTick(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
