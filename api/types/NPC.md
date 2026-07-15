---
title: "NPC"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/NPC.svg" alt="NPC icon" width="72"><figcaption></figcaption></figure>

# NPC

**Inherits:** [Physical](./Physical.md)
**Inherited by:** [Player](./Player.md)

## Properties

### Velocity

**Type:** [Vector3](./Vector3.md)

Documentation for this property is not yet available.

### SeatOffset

**Type:** [Vector3](./Vector3.md)

Documentation for this property is not yet available.

### Health

**Type:** `number`

Documentation for this property is not yet available.

### MaxHealth

**Type:** `number`

Documentation for this property is not yet available.

### JumpPower

**Type:** `number`

Documentation for this property is not yet available.

### WalkSpeed

**Type:** `number`

Documentation for this property is not yet available.

### UseNametag

**Type:** `boolean`

Documentation for this property is not yet available.

### NametagOffset

**Type:** [Vector3](./Vector3.md)

Documentation for this property is not yet available.

### NametagVisibleRadius

**Type:** `number`

Documentation for this property is not yet available.

### DisplayName

**Type:** `string`

Documentation for this property is not yet available.

### JumpSound

**Type:** [Sound](./Sound.md)

Documentation for this property is not yet available.

### IsSitting

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsDead

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### HoldingTool

**Type:** [Tool](./Tool.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### SittingIn

**Type:** [Seat](./Seat.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### Character

**Type:** [CharacterModel](./CharacterModel.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### MoveTarget

**Type:** [Dynamic](./Dynamic.md)

Documentation for this property is not yet available.

### IsOnGround

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsOnCeiling

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### NavDestinationDistance

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### NavDestinationReached

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### NavDestinationValid

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### Move(velo)

#### Parameters

- `velo`: [Vector3](./Vector3.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### Kill()

**Returns:** `nil`

Documentation for this method is not yet available.

### TryStepUp()

**Returns:** `boolean`

Documentation for this method is not yet available.

### Jump()

**Returns:** `nil`

Documentation for this method is not yet available.

### Sit(seat)

#### Parameters

- `seat`: [Seat](./Seat.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### Unsit(addForce?)

#### Parameters

- `addForce`: `boolean` — optional — default: `True`

**Returns:** `nil`

Documentation for this method is not yet available.

### EquipTool(tool)

#### Parameters

- `tool`: [Tool](./Tool.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### DropTool()

**Returns:** `nil`

Documentation for this method is not yet available.

### LoadAppearance(userID)

#### Parameters

- `userID`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### ClearAppearance()

**Returns:** `nil`

Documentation for this method is not yet available.

### SetNavDestination(pos)

#### Parameters

- `pos`: [Vector3](./Vector3.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### Respawn()

**Returns:** `nil`

Documentation for this method is not yet available.

### TakeDamage(dmg)

#### Parameters

- `dmg`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### Heal(amount)

#### Parameters

- `amount`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### Died(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### Landed(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### NavFinished(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
