---
title: "SchedulerService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/SchedulerService.svg" alt="SchedulerService icon" width="72"><figcaption></figcaption></figure>

# SchedulerService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Scheduler`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### ActiveTaskCount

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### Delay(seconds, callback)

#### Parameters

- `seconds`: `number`
- `callback`: `() -> ()`

**Returns:** `number`

Documentation for this method is not yet available.

### Repeat(interval, callback, repetitions?)

#### Parameters

- `interval`: `number`
- `callback`: `() -> ()`
- `repetitions`: `number` — optional — default: `-1`

**Returns:** `number`

Documentation for this method is not yet available.

### NextFrame(callback)

#### Parameters

- `callback`: `() -> ()`

**Returns:** `number`

Documentation for this method is not yet available.

### Cancel(handle)

#### Parameters

- `handle`: `number`

**Returns:** `boolean`

Documentation for this method is not yet available.

### IsScheduled(handle)

#### Parameters

- `handle`: `number`

**Returns:** `boolean`

Documentation for this method is not yet available.

### GetTimeRemaining(handle)

#### Parameters

- `handle`: `number`

**Returns:** `number`

Documentation for this method is not yet available.

### CancelAll()

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### TaskCompleted(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### TaskCanceled(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
