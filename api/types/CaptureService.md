---
title: "CaptureService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/CaptureService.svg" alt="CaptureService icon" width="72"><figcaption></figcaption></figure>

# CaptureService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Capture`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### OnCooldown

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### CanCapture

**Type:** `boolean`

Documentation for this property is not yet available.

### DefaultCaptureOverlay

**Type:** [UIField](./UIField.md)

Documentation for this property is not yet available.

### SpectatorAttach

**Type:** [Dynamic](./Dynamic.md)

Documentation for this property is not yet available.

## Methods

### TakePhotoAtDynamic(dyn, photoSize?, overlay?)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `dyn`: [Dynamic](./Dynamic.md)
- `photoSize`: `Vector2` — optional
- `overlay`: [UIField](./UIField.md) — optional

**Returns:** `nil`

Documentation for this method is not yet available.

### TakePhotoAt(pos, rot, photoSize?, overlay?)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `pos`: `Vector3`
- `rot`: `Vector3`
- `photoSize`: `Vector2` — optional
- `overlay`: [UIField](./UIField.md) — optional

**Returns:** `nil`

Documentation for this method is not yet available.
