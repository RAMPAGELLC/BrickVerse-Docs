---
title: "Camera"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/Camera.svg" alt="Camera icon" width="72"><figcaption></figcaption></figure>

# Camera

**Inherits:** [Dynamic](./Dynamic.md)

## Properties

### Forward

**Type:** `Vector3`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### Mode

**Type:** [CameraMode](../enums/CameraMode.md)

Documentation for this property is not yet available.

### FOV

**Type:** `number`

Documentation for this property is not yet available.

### ClipThroughWalls

**Type:** `boolean`

Documentation for this property is not yet available.

### MinDistance

**Type:** `number`

Documentation for this property is not yet available.

### MaxDistance

**Type:** `number`

Documentation for this property is not yet available.

### Distance

**Type:** `number`

Documentation for this property is not yet available.

### ScrollSensitivity

**Type:** `number`

Documentation for this property is not yet available.

### Orthographic

**Type:** `boolean`

Documentation for this property is not yet available.

### FollowLerp

**Type:** `boolean`

Documentation for this property is not yet available.

### LerpSpeed

**Type:** `number`

Documentation for this property is not yet available.

### OrthographicSize

**Type:** `number`

Documentation for this property is not yet available.

### Near

**Type:** `number`

Documentation for this property is not yet available.

### Far

**Type:** `number`

Documentation for this property is not yet available.

### PositionOffset

**Type:** `Vector3`

Documentation for this property is not yet available.

### RotationOffset

**Type:** `Vector3`

Documentation for this property is not yet available.

### IsFirstPerson

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### CanLock

**Type:** `boolean`

Documentation for this property is not yet available.

### SensitivityMultiplier

**Type:** `number`

Documentation for this property is not yet available.

### Sensitivity

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### HorizontalSpeed

**Type:** `number`

Documentation for this property is not yet available.

### VerticalSpeed

**Type:** `number`

Documentation for this property is not yet available.

### ScrollLerpSpeed

**Type:** `number`

Documentation for this property is not yet available.

### CtrlLocked

**Type:** `boolean`

Documentation for this property is not yet available.

### AlwaysLocked

**Type:** `boolean`

Documentation for this property is not yet available.

### Target

**Type:** [Dynamic](./Dynamic.md)

Documentation for this property is not yet available.

## Methods

### IsPositionInView(pos)

#### Parameters

- `pos`: `Vector3`

**Returns:** `boolean`

Documentation for this method is not yet available.

### IsPositionBehind(pos)

#### Parameters

- `pos`: `Vector3`

**Returns:** `boolean`

Documentation for this method is not yet available.

### ViewportPointToRay(pos, ignoreList?, maxDistance?)

#### Parameters

- `pos`: `Vector2`
- `ignoreList`: { [Instance](./Instance.md) } — optional
- `maxDistance`: `number` — optional — default: `10000`

**Returns:** [RayResult](./RayResult.md)

Documentation for this method is not yet available.

### ScreenPointToRay(pos, ignoreList?, maxDistance?)

#### Parameters

- `pos`: `Vector2`
- `ignoreList`: { [Instance](./Instance.md) } — optional
- `maxDistance`: `number` — optional — default: `10000`

**Returns:** [RayResult](./RayResult.md)

Documentation for this method is not yet available.

### ViewportToScreenPoint(pos)

#### Parameters

- `pos`: `Vector2`

**Returns:** `Vector2`

Documentation for this method is not yet available.

### ViewportToWorldPoint(pos)

#### Parameters

- `pos`: `Vector2`

**Returns:** `Vector3`

Documentation for this method is not yet available.

### WorldToViewportPoint(pos)

#### Parameters

- `pos`: `Vector3`

**Returns:** `Vector2`

Documentation for this method is not yet available.

### WorldToScreenPoint(pos)

#### Parameters

- `pos`: `Vector3`

**Returns:** `Vector2`

Documentation for this method is not yet available.

### ScreenToViewportPoint(pos)

#### Parameters

- `pos`: `Vector2`

**Returns:** `Vector2`

Documentation for this method is not yet available.

### ScreenToWorldPoint(pos)

#### Parameters

- `pos`: `Vector2`

**Returns:** `Vector3`

Documentation for this method is not yet available.

## Events

### FirstPersonEntered(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### FirstPersonExited(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
