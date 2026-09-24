---
title: "AudioNode"
description: ""
---

# AudioNode

**Inherits:** [Instance](./Instance.md)
**Inherited by:** [AudioDeviceInput](./AudioDeviceInput.md), [AudioDeviceOutput](./AudioDeviceOutput.md), [AudioPlayer](./AudioPlayer.md), [AudioProcessor](./AudioProcessor.md)

{% hint style="danger" %}
**Abstract object**

This object exists as a base for other objects and cannot be created or accessed directly.
{% endhint %}

## Methods

### GetInputPins()

**Returns:** `{ string }`

Documentation for this method is not yet available.

### GetOutputPins()

**Returns:** `{ string }`

Documentation for this method is not yet available.

### GetConnectedWires(pin)

#### Parameters

- `pin`: `string`

**Returns:** { [AudioWire](./AudioWire.md) }

Documentation for this method is not yet available.

## Events

### WiringChanged(value)

**Type:** [BVSignal](./BVSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
