---
title: "ChatService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/ChatService.svg" alt="ChatService icon" width="72"><figcaption></figcaption></figure>

# ChatService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `Chat`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Properties

### ChatPredicate

**Type:** `() -> ()`

Documentation for this property is not yet available.

## Methods

### BroadcastMessage(msg)

#### Parameters

- `msg`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### UnicastMessage(msg, plr)

#### Parameters

- `msg`: `string`
- `plr`: [Player](./Player.md)

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### NewChatMessage(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### MessageReceived(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### MessageDeclined(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
