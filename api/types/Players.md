---
title: "Players"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/Players.svg" alt="Players icon" width="72"><figcaption></figcaption></figure>

# Players

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Players`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### LocalPlayer

**Type:** [Player](./Player.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### PlayerCollisionEnabled

**Type:** `boolean`

Documentation for this property is not yet available.

### UseServerAuthority

**Type:** `boolean`

**Attributes:** Not accessible from scripts

Documentation for this property is not yet available.

### PlayersCount

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### MaxPlayers

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### GetPlayers()

**Returns:** { [Player](./Player.md) }

Documentation for this method is not yet available.

### GetPlayer(username)

#### Parameters

- `username`: `string`

**Returns:** [Player](./Player.md)

Documentation for this method is not yet available.

### GetPlayerByID(userID)

#### Parameters

- `userID`: `string`

**Returns:** [Player](./Player.md)

Documentation for this method is not yet available.

## Events

### PlayerAdded(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### PlayerRemoved(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
