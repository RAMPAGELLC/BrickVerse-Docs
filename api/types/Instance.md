---
title: "Instance"
description: ""
---

<figure><img src="../../.gitbook/assets/api-icons/Instance.svg" alt="Instance icon" width="72"><figcaption></figcaption></figure>

# Instance

**Inherits:** [NetworkedObject](./NetworkedObject.md)
**Inherited by:** [AchievementsService](./AchievementsService.md), [Animator](./Animator.md), [AssetsService](./AssetsService.md), [BindableEvent](./BindableEvent.md), [BodyPosition](./BodyPosition.md), [BodyRotation](./BodyRotation.md), [CaptureService](./CaptureService.md), [ChatService](./ChatService.md), [Clothing](./Clothing.md), [CoreUIService](./CoreUIService.md), [CreatorAddons](./CreatorAddons.md), [CreatorContextService](./CreatorContextService.md), [CreatorGUI](./CreatorGUI.md), [CreatorHistory](./CreatorHistory.md), [CreatorSelections](./CreatorSelections.md), [DatastoreService](./DatastoreService.md), [Dynamic](./Dynamic.md), [Environment](./Environment.md), [FilterService](./FilterService.md), [Folder](./Folder.md), [Grabbable](./Grabbable.md), [GUI](./GUI.md), [HiddenBase](./HiddenBase.md), [HttpService](./HttpService.md), [InputService](./InputService.md), [InsertService](./InsertService.md), [IOService](./IOService.md), [Lighting](./Lighting.md), [LightingModifier](./LightingModifier.md), [MissingInstance](./MissingInstance.md), [NetworkEvent](./NetworkEvent.md), [PlayerGUI](./PlayerGUI.md), [Players](./Players.md), [PreferencesService](./PreferencesService.md), [PresenceService](./PresenceService.md), [PurchasesService](./PurchasesService.md), [Script](./Script.md), [ScriptService](./ScriptService.md), [Sky](./Sky.md), [SocialService](./SocialService.md), [Stat](./Stat.md), [Stats](./Stats.md), [Team](./Team.md), [Teams](./Teams.md), [TweenService](./TweenService.md), [UIAspectRatioRestraint](./UIAspectRatioRestraint.md), [UICorner](./UICorner.md), [UIField](./UIField.md), [UIShadow](./UIShadow.md), [UIStroke](./UIStroke.md), [ValueBase](./ValueBase.md), [Weld](./Weld.md), [World](./World.md), [WorldsService](./WorldsService.md)

{% hint style="danger" %}
**Abstract object**

This object exists as a base for other objects and cannot be created or accessed directly.
{% endhint %}

## Properties

### Parent

**Type:** [Instance](./Instance.md)

Documentation for this property is not yet available.

### EditableChildren

**Type:** `boolean`

**Attributes:** Not accessible from scripts

Documentation for this property is not yet available.

### Tags

**Type:** `{ string }`

Documentation for this property is not yet available.

### Archivable

**Type:** `boolean`

Documentation for this property is not yet available.

## Methods

### GetDescendants()

**Returns:** { [Instance](./Instance.md) }

Documentation for this method is not yet available.

### FindChild(name)

#### Parameters

- `name`: `string`

**Returns:** [Instance](./Instance.md)

Documentation for this method is not yet available.

### WaitChild(name, timeoutSec?)

**Attributes:** Yields

{% hint style="info" %}
**Yielding method**

This method may yield the current script until the operation completes.
{% endhint %}

#### Parameters

- `name`: `string`
- `timeoutSec`: `number` — optional

**Returns:** [Instance](./Instance.md)

Documentation for this method is not yet available.

### FindChildByClass(className)

#### Parameters

- `className`: `string`

**Returns:** [Instance](./Instance.md)

Documentation for this method is not yet available.

### FindChildWithTag(tag)

#### Parameters

- `tag`: `string`

**Returns:** [Instance](./Instance.md)

Documentation for this method is not yet available.

### FindDescendant(path)

#### Parameters

- `path`: `string`

**Returns:** [Instance](./Instance.md)

Documentation for this method is not yet available.

### GetChildrenWithTag(tag)

#### Parameters

- `tag`: `string`

**Returns:** { [Instance](./Instance.md) }

Documentation for this method is not yet available.

### GetDescendantsWithTag(tag)

#### Parameters

- `tag`: `string`

**Returns:** { [Instance](./Instance.md) }

Documentation for this method is not yet available.

### FindAncestorByClass(className)

#### Parameters

- `className`: `string`

**Returns:** [Instance](./Instance.md)

Documentation for this method is not yet available.

### FindChildByIndex(index)

#### Parameters

- `index`: `number`

**Returns:** [Instance](./Instance.md)

Documentation for this method is not yet available.

### MoveChild(child, index)

#### Parameters

- `child`: [Instance](./Instance.md)
- `index`: `number`

**Returns:** `nil`

Documentation for this method is not yet available.

### GetChildren()

**Returns:** { [Instance](./Instance.md) }

Documentation for this method is not yet available.

### GetChildrenOfClass(className)

#### Parameters

- `className`: `string`

**Returns:** { [Instance](./Instance.md) }

Documentation for this method is not yet available.

### IsAncestorOf(instance)

#### Parameters

- `instance`: [Instance](./Instance.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

### IsDescendantOf(instance)

#### Parameters

- `instance`: [Instance](./Instance.md)

**Returns:** `boolean`

Documentation for this method is not yet available.

### IsDescendantOfClass(className)

#### Parameters

- `className`: `string`

**Returns:** `boolean`

Documentation for this method is not yet available.

### New(className, parent?)

**Attributes:** Static

#### Parameters

- `className`: `string`
- `parent`: [Instance](./Instance.md) — optional

**Returns:** [Instance](./Instance.md)

Documentation for this method is not yet available.

### AddTag(tag)

#### Parameters

- `tag`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### RemoveTag(tag)

#### Parameters

- `tag`: `string`

**Returns:** `nil`

Documentation for this method is not yet available.

### HasTag(tag)

#### Parameters

- `tag`: `string`

**Returns:** `boolean`

Documentation for this method is not yet available.

### Reparent(to)

#### Parameters

- `to`: [Instance](./Instance.md)

**Returns:** `nil`

Documentation for this method is not yet available.

### GetParent()

**Returns:** [Instance](./Instance.md)

Documentation for this method is not yet available.

### SetParent(newParent)

#### Parameters

- `newParent`: [Instance](./Instance.md)

**Returns:** `nil`

Documentation for this method is not yet available.

## Events

### ChildAdded(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### ChildRemoved(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### ChildDeleting(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.

### ChildDeleted(value)

**Type:** [PTSignal](./PTSignal.md)

#### Parameters

- `value`: `any`

This event is fired when its associated action occurs.
