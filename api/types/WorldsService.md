---
title: "WorldsService"
description: ""
---

# WorldsService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Worlds`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Methods

### NewServerAsync(worldPath)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `worldPath`: `string`

**Returns:** `string`

Documentation for this method is not yet available.

### NewServerAsync(data)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `data`: [NewServerRequestData](./NewServerRequestData.md)

**Returns:** `string`

Documentation for this method is not yet available.

### JoinWorldAsync(plr, to)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `plr`: [Player](./Player.md)
- `to`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### JoinWorldPartyAsync(plrs, to)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `plrs`: { [Player](./Player.md) }
- `to`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### JoinPrivateAsync(plr, accessID)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `plr`: [Player](./Player.md)
- `accessID`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### JoinPrivatePartyAsync(players, accessID)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `players`: { [Player](./Player.md) }
- `accessID`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.
