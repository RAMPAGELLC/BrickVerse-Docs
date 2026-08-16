---
title: "GeometryService"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/GeometryService.svg" alt="GeometryService icon" width="72"><figcaption></figcaption></figure>

# GeometryService

**Inherits:** [Instance](./Instance.md)

{% hint style="info" %}
**Static class**

Access this class using `GeometryService`. It cannot be created with `Instance.New()`.
{% endhint %}

{% hint style="warning" %}
**Not instantiable**

This object cannot be created using `Instance.New()`.
{% endhint %}

## Methods

### UnionAsync(operands)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `operands`: { [Instance](./Instance.md) }

**Returns:** [UnionOperation](./UnionOperation.md)

Documentation for this method is not yet available.

### UnionMeshesAsync(meshes)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `meshes`: { [EditableMesh](./EditableMesh.md) }

**Returns:** [EditableMesh](./EditableMesh.md)

Documentation for this method is not yet available.

### SubtractMeshesAsync(source, cutters)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `source`: [EditableMesh](./EditableMesh.md)
- `cutters`: { [EditableMesh](./EditableMesh.md) }

**Returns:** [EditableMesh](./EditableMesh.md)

Documentation for this method is not yet available.
