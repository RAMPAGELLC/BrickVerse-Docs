---
title: "AudioPlayer"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/AudioPlayer.svg" alt="AudioPlayer icon" width="72"><figcaption></figcaption></figure>

# AudioPlayer

**Inherits:** [AudioNode](./AudioNode.md)

## Properties

### Audio

**Type:** [AudioAsset](./AudioAsset.md)

Documentation for this property is not yet available.

### AutoLoad

**Type:** `boolean`

Documentation for this property is not yet available.

### AutoPlay

**Type:** `boolean`

Documentation for this property is not yet available.

### Looping

**Type:** `boolean`

Documentation for this property is not yet available.

### Volume

**Type:** `number`

Documentation for this property is not yet available.

### PlaybackSpeed

**Type:** `number`

Documentation for this property is not yet available.

### LoopRegion

**Type:** [NumberRange](./NumberRange.md)

Documentation for this property is not yet available.

### PlaybackRegion

**Type:** [NumberRange](./NumberRange.md)

Documentation for this property is not yet available.

### IsReady

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsPlaying

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### TimeLength

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### TimePosition

**Type:** `number`

Documentation for this property is not yet available.

## Methods

### Play(atTime?)

#### Parameters

- `atTime`: `number` — optional — default: `-1`

**Returns:** `nil`

Documentation for this method is not yet available.

### Pause()

**Returns:** `nil`

Documentation for this method is not yet available.

### Resume()

**Returns:** `nil`

Documentation for this method is not yet available.

### Stop()

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### Ended(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### Looped(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
