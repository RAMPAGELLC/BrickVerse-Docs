---
title: "InputService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/InputService.svg" alt="InputService icon" width="72"><figcaption></figcaption></figure>

# InputService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Input`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### IsWindowFocused

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsTouchscreen

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsGameFocused

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsInputFocused

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsGamepadConnected

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IsMenuOpened

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### CursorLocked

**Type:** `boolean`

Documentation for this property is not yet available.

### CursorVisible

**Type:** `boolean`

Documentation for this property is not yet available.

### MouseDelta

**Type:** [Vector2](./Vector2.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### MousePosition

**Type:** [Vector2](./Vector2.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### ScreenWidth

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### ScreenHeight

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### StartGamepadVibration(weakMagnitude, strongMagnitude, duration)

#### Parameters

- `weakMagnitude`: `number`
- `strongMagnitude`: `number`
- `duration`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### StopGamepadVibration()

**Returns:** `nil`

Documentation for this method is not yet available.

### GetMouseWorldPosition(ignoreList?)

#### Parameters

- `ignoreList`: { [Instance](./Instance.md) } — optional

**Returns:** [Vector3](./Vector3.md)

Documentation for this method is not yet available.

### GetVector2(actionName)

#### Parameters

- `actionName`: `string`

**Returns:** [InputActionVector2](./InputActionVector2.md)

Documentation for this method is not yet available.

### GetButton(actionName)

#### Parameters

- `actionName`: `string`

**Returns:** [InputActionButton](./InputActionButton.md)

Documentation for this method is not yet available.

### GetAxis(actionName)

#### Parameters

- `actionName`: `string`

**Returns:** [InputActionAxis](./InputActionAxis.md)

Documentation for this method is not yet available.

### BindButton(name)

#### Parameters

- `name`: `string`

**Returns:** [InputActionButton](./InputActionButton.md)

Documentation for this method is not yet available.

### BindAxis(name)

#### Parameters

- `name`: `string`

**Returns:** [InputActionAxis](./InputActionAxis.md)

Documentation for this method is not yet available.

### BindVector2(name)

#### Parameters

- `name`: `string`

**Returns:** [InputActionVector2](./InputActionVector2.md)

Documentation for this method is not yet available.

## Events

### MouseMoved(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### GameFocused(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### GameUnfocused(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### GamepadConnected(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### GamepadDisconnected(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### KeyDown(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### KeyUp(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### AxisValueChanged(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
