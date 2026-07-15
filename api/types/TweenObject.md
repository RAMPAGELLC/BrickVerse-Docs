---
title: "TweenObject"
description: ""
---

# TweenObject

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### Looped

**Type:** `boolean`

Documentation for this property is not yet available.

### Parallel

**Type:** `boolean`

Documentation for this property is not yet available.

### SpeedScale

**Type:** `number`

Documentation for this property is not yet available.

### Direction

**Type:** [TweenDirection](../enums/TweenDirection.md)

Documentation for this property is not yet available.

### Transition

**Type:** [TweenTransition](../enums/TweenTransition.md)

Documentation for this property is not yet available.

### IsRunning

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### ElapsedTime

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### SetDirection(dir)

#### Parameters

- `dir`: [TweenDirection](../enums/TweenDirection.md)

**Returns:** [TweenObject](./TweenObject.md)

Documentation for this method is not yet available.

### SetTrans(trans)

#### Parameters

- `trans`: [TweenTransition](../enums/TweenTransition.md)

**Returns:** [TweenObject](./TweenObject.md)

Documentation for this method is not yet available.

### TweenPosition(target, destination, time)

#### Parameters

- `target`: [Dynamic](./Dynamic.md)
- `destination`: [Vector3](./Vector3.md)
- `time`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### TweenRotation(target, destination, time)

#### Parameters

- `target`: [Dynamic](./Dynamic.md)
- `destination`: [Vector3](./Vector3.md)
- `time`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### TweenSize(target, destination, time)

#### Parameters

- `target`: [Dynamic](./Dynamic.md)
- `destination`: [Vector3](./Vector3.md)
- `time`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### TweenColor(from, to, time, callback)

#### Parameters

- `from`: [Color](./Color.md)
- `to`: [Color](./Color.md)
- `time`: `number`
- `callback`: `() -> ()`

**Returns:** `nil`

Documentation for this method is not yet available.

### TweenNumber(from, to, time, callback)

#### Parameters

- `from`: `number`
- `to`: `number`
- `time`: `number`
- `callback`: `() -> ()`

**Returns:** `nil`

Documentation for this method is not yet available.

### TweenVector2(from, to, time, callback)

#### Parameters

- `from`: [Vector2](./Vector2.md)
- `to`: [Vector2](./Vector2.md)
- `time`: `number`
- `callback`: `() -> ()`

**Returns:** `nil`

Documentation for this method is not yet available.

### TweenVector3(from, to, time, callback)

#### Parameters

- `from`: [Vector3](./Vector3.md)
- `to`: [Vector3](./Vector3.md)
- `time`: `number`
- `callback`: `() -> ()`

**Returns:** `nil`

Documentation for this method is not yet available.

### TweenQuaternion(from, to, time, callback)

#### Parameters

- `from`: [Quaternion](./Quaternion.md)
- `to`: [Quaternion](./Quaternion.md)
- `time`: `number`
- `callback`: `() -> ()`

**Returns:** `nil`

Documentation for this method is not yet available.

### Play()

**Returns:** `nil`

Documentation for this method is not yet available.

### Pause()

**Returns:** `nil`

Documentation for this method is not yet available.

### Stop()

**Returns:** `nil`

Documentation for this method is not yet available.

### Interval(sec)

#### Parameters

- `sec`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### Chain()

**Returns:** [TweenObject](./TweenObject.md)

Documentation for this method is not yet available.

### Cancel(callFinished?)

#### Parameters

- `callFinished`: `boolean` — optional — default: `False`

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### Finished(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### Canceled(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
