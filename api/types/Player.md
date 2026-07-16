---
title: "Player"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/Player.svg" alt="Player icon" width="72"><figcaption></figcaption></figure>

# Player

**Inherits:** [NPC](./NPC.md)

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### UserID

**Type:** `string`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### CanMove

**Type:** `boolean`

Documentation for this property is not yet available.

### SprintSpeed

**Type:** `number`

Documentation for this property is not yet available.

### Stamina

**Type:** `number`

Documentation for this property is not yet available.

### MaxStamina

**Type:** `number`

Documentation for this property is not yet available.

### UseStamina

**Type:** `boolean`

Documentation for this property is not yet available.

### StaminaRegen

**Type:** `number`

Documentation for this property is not yet available.

### StaminaBurn

**Type:** `number`

Documentation for this property is not yet available.

### RespawnTime

**Type:** `number`

Documentation for this property is not yet available.

### UseHeadTurning

**Type:** `boolean`

Documentation for this property is not yet available.

### UseBubbleChat

**Type:** `boolean`

Documentation for this property is not yet available.

### AutoLoadAppearance

**Type:** `boolean`

Documentation for this property is not yet available.

### AllowAnimationWhileMoving

**Type:** `boolean`

Documentation for this property is not yet available.

### Team

**Type:** [Team](./Team.md)

Documentation for this property is not yet available.

### MovementMode

**Type:** [PlayerMovementMode](../enums/PlayerMovementMode.md)

Documentation for this property is not yet available.

### NetworkPing

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsAdmin

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsStarCreator

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### HasVerifiedBadge

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsCreator

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### UserRoleClass

**Type:** `string`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### ChatColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### IsLocal

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsClimbing

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### ClimbingTruss

**Type:** [Truss](./Truss.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### UserPlatform

**Type:** [ClientPlatform](../enums/ClientPlatform.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### Inventory

**Type:** [Inventory](./Inventory.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### Jump()

**Returns:** `nil`

Documentation for this method is not yet available.

### Kick(reason)

#### Parameters

- `reason`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### UnequipTool()

**Returns:** `nil`

Documentation for this method is not yet available.

### Respawn()

**Returns:** `nil`

Documentation for this method is not yet available.

### ResetAppearance()

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### Chatted(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### StatChanged(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### TeamChanged(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### Respawned(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
