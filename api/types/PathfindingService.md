---
title: "PathfindingService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/PathfindingService.svg" alt="PathfindingService icon" width="72"><figcaption></figcaption></figure>

# PathfindingService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `PathfindingService`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Methods

### ComputeAsync(start, finish, optimize?)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `start`: `Vector3`
- `finish`: `Vector3`
- `optimize`: `boolean` — optional — default: `True`

**Returns:** [PathfindingPath](./PathfindingPath.md)

Documentation for this method is not yet available.

### CheckOcclusion(path, startWaypoint?)

#### Parameters

- `path`: [PathfindingPath](./PathfindingPath.md)
- `startWaypoint`: `number` — optional — default: `0`

**Returns:** `number`

Documentation for this method is not yet available.
