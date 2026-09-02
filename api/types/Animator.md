---
title: "Animator"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/Animator.svg" alt="Animator icon" width="72"><figcaption></figcaption></figure>

# Animator

**Inherits:** [Instance](./Instance.md)

## Properties

### IsPlaying

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### CurrentTrack

**Type:** [AnimationTrack](./AnimationTrack.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### CurrentAnimation

**Type:** `string`

Documentation for this property is not yet available.

## Methods

### LoadAnimation(track)

#### Parameters

- `track`: [AnimationTrack](./AnimationTrack.md)

**Returns:** [AnimationTrack](./AnimationTrack.md)

Documentation for this method is not yet available.

### IsAnimationLoaded(track)

#### Parameters

- `track`: [AnimationTrack](./AnimationTrack.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

### UnloadAnimation(track)

#### Parameters

- `track`: [AnimationTrack](./AnimationTrack.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### PlayAnimationTrack(track)

#### Parameters

- `track`: [AnimationTrack](./AnimationTrack.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### StopAnimationTrack(track)

#### Parameters

- `track`: [AnimationTrack](./AnimationTrack.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### PlayAnimation(animationKey)

#### Parameters

- `animationKey`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### PlayOneShotAnimation(animationKey)

#### Parameters

- `animationKey`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### StopAnimation()

**Returns:** `nil`

Documentation for this method is not yet available.

### StopOneShotAnimation()

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### AnimationPlayed(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### AnimationStopped(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
