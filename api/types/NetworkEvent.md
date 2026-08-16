---
title: "NetworkEvent"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/NetworkEvent.svg" alt="NetworkEvent icon" width="72"><figcaption></figcaption></figure>

# NetworkEvent

**Inherits:** [Instance](./Instance.md)

## Properties

### RateLimitEnabled

**Type:** `boolean`

Documentation for this property is not yet available.

### RateLimitMaxRequests

**Type:** `number`

Documentation for this property is not yet available.

### RateLimitWindowSeconds

**Type:** `number`

Documentation for this property is not yet available.

### RateLimitScope

**Type:** [NetworkEventRateLimitScope](../enums/NetworkEventRateLimitScope.md)

Documentation for this property is not yet available.

### LogRateLimitRejections

**Type:** `boolean`

Documentation for this property is not yet available.

### Reliable

**Type:** `boolean`

Documentation for this property is not yet available.

## Methods

### InvokeServer(payload?, _?)

#### Parameters

- `payload`: `any` — optional
- `_`: `any` — optional

**Returns:** `nil`

Documentation for this method is not yet available.

### InvokeClient(payload?, player?)

#### Parameters

- `payload`: `any` — optional
- `player`: [Player](./Player.md) — optional

**Returns:** `nil`

Documentation for this method is not yet available.

### InvokeClients(payload?)

#### Parameters

- `payload`: `any` — optional

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
