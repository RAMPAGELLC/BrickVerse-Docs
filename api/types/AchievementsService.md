---
title: "AchievementsService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/AchievementsService.svg" alt="AchievementsService icon" width="72"><figcaption></figcaption></figure>

# AchievementsService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Achievements`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### UseAchievementSound

**Type:** `boolean`

Documentation for this property is not yet available.

### NotifyAchievements

**Type:** `boolean`

Documentation for this property is not yet available.

## Methods

### AwardAsync(userID, achievementID)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `userID`: `string`
- `achievementID`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### HasAchievementAsync(userID, achievementID)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `userID`: `string`
- `achievementID`: `number`

**Returns:** `boolean`

Documentation for this method is not yet available.

## Events

### GotAchievement(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
