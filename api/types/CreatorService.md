---
title: "CreatorService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/CreatorService.svg" alt="CreatorService icon" width="72"><figcaption></figcaption></figure>

# CreatorService

{% hint style="info" %}
**Static class**

Access this class using `Creator`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### Interface

**Type:** [CreatorInterface](./CreatorInterface.md)

**Attributes:** Static · Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### CurrentGame

**Type:** [World](./World.md)

**Attributes:** Static · Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### LocalTestActive

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Events

### LocalTestStarted(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### LocalTestStopped(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
