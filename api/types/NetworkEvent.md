---
title: "NetworkEvent"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/NetworkEvent.svg" alt="NetworkEvent icon" width="72"><figcaption></figcaption></figure>

# NetworkEvent

**Inherits:** [Instance](./Instance.md)

## Properties

### Reliable

**Type:** `boolean`

Documentation for this property is not yet available.

## Methods

### InvokeServer(msg?, _?)

#### Parameters

- `msg`: [NetMessage](./NetMessage.md) — optional
- `_`: `any` — optional

**Returns:** `nil`

Documentation for this method is not yet available.

### InvokeClient(msg?, player?)

#### Parameters

- `msg`: [NetMessage](./NetMessage.md) — optional
- `player`: [Player](./Player.md) — optional

**Returns:** `nil`

Documentation for this method is not yet available.

### InvokeClients(msg?)

#### Parameters

- `msg`: [NetMessage](./NetMessage.md) — optional

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### InvokedServer(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### InvokedClient(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
