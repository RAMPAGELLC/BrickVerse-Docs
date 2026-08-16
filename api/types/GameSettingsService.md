---
title: "GameSettingsService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/GameSettingsService.svg" alt="GameSettingsService icon" width="72"><figcaption></figcaption></figure>

# GameSettingsService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `GameSettings`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Methods

### GetSettings()

**Returns:** { [GameSetting](./GameSetting.md) }

Documentation for this method is not yet available.

### GetSetting(key)

#### Parameters

- `key`: `string`

**Returns:** [GameSetting](./GameSetting.md)

Documentation for this method is not yet available.

## Events

### SettingChanged(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
