---
title: "VRService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/VRService.svg" alt="VRService icon" width="72"><figcaption></figcaption></figure>

# VRService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `VRService`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### VREnabled

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### VRAvailable

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### DeviceName

**Type:** `string`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### ThirdPersonFollowCamEnabled

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### GuiInputUserCFrame

**Type:** [UserCFrame](../enums/UserCFrame.md)

Documentation for this property is not yet available.

### AutomaticScaling

**Type:** [VRScaling](../enums/VRScaling.md)

Documentation for this property is not yet available.

### ControllerModels

**Type:** [VRControllerModelMode](../enums/VRControllerModelMode.md)

Documentation for this property is not yet available.

### LaserPointer

**Type:** [VRLaserPointerMode](../enums/VRLaserPointerMode.md)

Documentation for this property is not yet available.

### FadeOutViewOnCollision

**Type:** `boolean`

Documentation for this property is not yet available.

### AvatarGestures

**Type:** `boolean`

Documentation for this property is not yet available.

## Methods

### GetUserCFrame(type)

#### Parameters

- `type`: [UserCFrame](../enums/UserCFrame.md)

**Returns:** `Transform3D`

Documentation for this method is not yet available.

### GetUserCFrameEnabled(type)

#### Parameters

- `type`: [UserCFrame](../enums/UserCFrame.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

### RecenterUserHeadCFrame()

**Returns:** `nil`

Documentation for this method is not yet available.

### GetTouchpadMode(pad)

#### Parameters

- `pad`: [VRTouchpad](../enums/VRTouchpad.md)

**Returns:** [VRTouchpadMode](../enums/VRTouchpadMode.md)

Documentation for this method is not yet available.

### SetTouchpadMode(pad, mode)

#### Parameters

- `pad`: [VRTouchpad](../enums/VRTouchpad.md)
- `mode`: [VRTouchpadMode](../enums/VRTouchpadMode.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### RequestNavigation(cframe, inputUserCFrame?)

#### Parameters

- `cframe`: `Transform3D`
- `inputUserCFrame`: [UserCFrame](../enums/UserCFrame.md) — optional — default: `Head`

**Returns:** `nil`

Documentation for this method is not yet available.

### PulseController(controller, amplitude?, durationSeconds?, frequency?)

#### Parameters

- `controller`: [UserCFrame](../enums/UserCFrame.md)
- `amplitude`: `number` — optional — default: `0.5`
- `durationSeconds`: `number` — optional — default: `0.1`
- `frequency`: `number` — optional — default: `0`

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### UserCFrameChanged(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### UserCFrameEnabled(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### NavigationRequested(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### VREnabledChanged(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### TouchpadModeChanged(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
