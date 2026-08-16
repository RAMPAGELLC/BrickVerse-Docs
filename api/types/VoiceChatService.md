---
title: "VoiceChatService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/VoiceChatService.svg" alt="VoiceChatService icon" width="72"><figcaption></figcaption></figure>

# VoiceChatService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `VoiceChat`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### IsAvailable

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### MicrophoneEnabled

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### InputSensitivity

**Type:** `number`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IndicatorEnabled

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IndicatorColor

**Type:** [Color](./Color.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IndicatorIdleColor

**Type:** [Color](./Color.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### IndicatorMutedColor

**Type:** [Color](./Color.md)

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### SetMicrophoneEnabled(enabled)

#### Parameters

- `enabled`: `boolean`

**Returns:** `nil`

Documentation for this method is not yet available.

### SetInputSensitivity(sensitivity)

#### Parameters

- `sensitivity`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### SetIndicatorStyle(enabled, activeColor, idleColor, mutedColor)

#### Parameters

- `enabled`: `boolean`
- `activeColor`: [Color](./Color.md)
- `idleColor`: [Color](./Color.md)
- `mutedColor`: [Color](./Color.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### MutePlayer(player)

#### Parameters

- `player`: [Player](./Player.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### UnmutePlayer(player)

#### Parameters

- `player`: [Player](./Player.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### TogglePlayerMuted(player)

#### Parameters

- `player`: [Player](./Player.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

### IsPlayerMuted(player)

#### Parameters

- `player`: [Player](./Player.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

### IsPlayerSpeaking(player)

#### Parameters

- `player`: [Player](./Player.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

### GetVoiceLevel(player)

#### Parameters

- `player`: [Player](./Player.md)

**Returns:** `number`

Documentation for this method is not yet available.

### GetPlayerVolume(player)

#### Parameters

- `player`: [Player](./Player.md)

**Returns:** `number`

Documentation for this method is not yet available.

### SetPlayerVolume(player, volume)

#### Parameters

- `player`: [Player](./Player.md)
- `volume`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### MicrophoneChanged(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### PlayerMutedChanged(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### PlayerSpeakingChanged(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### VoiceLevelChanged(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
