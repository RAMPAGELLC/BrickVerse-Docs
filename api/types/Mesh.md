---
title: "Mesh"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/Mesh.svg" alt="Mesh icon" width="72"><figcaption></figcaption></figure>

# Mesh

**Inherits:** [Entity](./Entity.md)

## Properties

### Asset

**Type:** [MeshAsset](./MeshAsset.md)

Documentation for this property is not yet available.

### IncludeOffset

**Type:** `boolean`

Documentation for this property is not yet available.

### CollisionType

**Type:** [MeshCollisionType](../enums/MeshCollisionType.md)

Documentation for this property is not yet available.

### TextureFilter

**Type:** [TextureFilter](../enums/TextureFilter.md)

Documentation for this property is not yet available.

### PlayAnimationOnStart

**Type:** `boolean`

Documentation for this property is not yet available.

### UsePartColor

**Type:** `boolean`

Documentation for this property is not yet available.

### Color

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### CastShadows

**Type:** `boolean`

Documentation for this property is not yet available.

### CurrentAnimation

**Type:** `string`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsAnimationPlaying

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### Loading

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### PlayAnimation(animationName, speed?, loop?)

#### Parameters

- `animationName`: `string`
- `speed`: `number` — optional — default: `1`
- `loop`: `boolean` — optional — default: `True`

**Returns:** `nil`

Documentation for this method is not yet available.

### StopAnimation(animationName?)

#### Parameters

- `animationName`: `string` — optional

**Returns:** `nil`

Documentation for this method is not yet available.

### GetAnimations()

**Returns:** `{ string }`

Documentation for this method is not yet available.

### GetAnimationInfo()

**Returns:** { [MeshAnimationInfo](./MeshAnimationInfo.md) }

Documentation for this method is not yet available.

## Events

### Loaded(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
