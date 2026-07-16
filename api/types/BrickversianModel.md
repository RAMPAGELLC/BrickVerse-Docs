---
title: "BrickversianModel"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/BrickversianModel.svg" alt="BrickversianModel icon" width="72"><figcaption></figcaption></figure>

# BrickversianModel

**Inherits:** [CharacterModel](./CharacterModel.md)

## Properties

### HeadColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### TorsoColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### LeftArmColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### RightArmColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### LeftLegColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### RightLegColor

**Type:** [Color](./Color.md)

Documentation for this property is not yet available.

### FaceImage

**Type:** [ImageAsset](./ImageAsset.md)

Documentation for this property is not yet available.

### BodyMesh

**Type:** [MeshAsset](./MeshAsset.md)

Documentation for this property is not yet available.

### Ragdolling

**Type:** `boolean`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### RagdollPosition

**Type:** `Vector3`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

### RagdollRotation

**Type:** `Vector3`

**Attributes:** Read-only

{% hint style="warning" %}
**Read-only**

This property can be read by scripts but cannot be changed.
{% endhint %}

Documentation for this property is not yet available.

## Methods

### StartRagdoll(force?)

#### Parameters

- `force`: `Vector3` — optional

**Returns:** `nil`

Documentation for this method is not yet available.

### StopRagdoll()

**Returns:** `nil`

Documentation for this method is not yet available.

### GetAttachment(attachmentEnum)

#### Parameters

- `attachmentEnum`: [CharacterAttachment](../enums/CharacterAttachment.md)

**Returns:** [Dynamic](./Dynamic.md)

Documentation for this method is not yet available.

### LoadAppearance(userID, loadTool?)

#### Parameters

- `userID`: `string`
- `loadTool`: `boolean` — optional — default: `True`

**Returns:** `nil`

Documentation for this method is not yet available.

### ClearAppearance()

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### RagdollStarted(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### RagdollStopped(value)

**Type:** `PTSignal`

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
