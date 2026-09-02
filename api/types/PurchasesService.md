---
title: "PurchasesService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/PurchasesService.svg" alt="PurchasesService icon" width="72"><figcaption></figcaption></figure>

# PurchasesService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Purchases`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Methods

### PromptAsync(player, entitlementID)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `player`: [Player](./Player.md)
- `entitlementID`: `number`

**Returns:** `boolean`

Documentation for this method is not yet available.

### OwnsItemAsync(player, entitlementID)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `player`: [Player](./Player.md)
- `entitlementID`: `number`

**Returns:** `boolean`

Documentation for this method is not yet available.

### IsTrialAsync(player, entitlementID)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `player`: [Player](./Player.md)
- `entitlementID`: `number`

**Returns:** `boolean`

Documentation for this method is not yet available.

### GetTrialEndsAtAsync(player, entitlementID)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `player`: [Player](./Player.md)
- `entitlementID`: `number`

**Returns:** `string`

Documentation for this method is not yet available.

### IsGameTrialAsync(player)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `player`: [Player](./Player.md)

**Returns:** `boolean`

Documentation for this method is not yet available.
