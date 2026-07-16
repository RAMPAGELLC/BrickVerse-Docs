---
title: "ConfigService"
description: ""
---

# ConfigService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Config`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Methods

### GetConfigAsync(key)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `key`: `string`

**Returns:** `any`

Documentation for this method is not yet available.

### SetConfigAsync(key, value, secret?)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `key`: `string`
- `value`: `string`
- `secret`: `boolean` — optional — default: `False`

**Returns:** `nil`

Documentation for this method is not yet available.

### DeleteConfigAsync(key)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `key`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.
