# Game API

The Game API is the scripting reference for building experiences on BrickVerse.

It documents the classes, objects, services, properties, methods, events, enums, and data types available to game scripts. Use this section when you need to understand how an object behaves, what values it exposes, which functions can be called, or which events your scripts can listen for.

The API is designed for both quick reference and deeper exploration. Each page focuses on a specific class or enum and includes its inheritance information, available members, expected parameter types, return values, and any important usage restrictions.

## What you can find here

The Game API reference includes documentation for:

- Instances and game objects
- World and scene objects
- Players and characters
- Physics and collision systems
- User interface elements
- Audio and visual effects
- Networking and replication
- Server-only and client-only APIs
- Data types such as vectors, colors, bounds, and rotations
- Services provided automatically by BrickVerse
- Events and signals
- Enumerations used throughout the engine

Classes are organized into folders based on their purpose. Each folder contains related API types, making it easier to browse objects used for rendering, physics, interfaces, networking, scripting, and other engine systems.

## Reading an API page

Most class pages include several sections.

### Inheritance

Inheritance shows which class an object is based on.

A class may inherit properties, methods, and events from another class. For example, an object that inherits from `Instance` also has access to the members documented on the `Instance` page unless stated otherwise.

Some pages also list classes that inherit from the current type.

### Properties

Properties are values stored on an object.

A property may be writable, read-only, static, replicated, or unavailable to scripts. The property entry shows its type and any special restrictions that apply.

```lua
part.Name = "Platform"
part.Position = Vector3.New(0, 5, 0)
````

Read-only properties can be accessed but cannot be assigned a new value.

```lua
print(part.ClassName)
```

### Methods

Methods are functions provided by a class.

Each method page lists its parameters, optional values, return type, and whether the method may yield while waiting for an operation to complete.

```lua
local child = parent:FindChild("Platform")
```

Static methods are called directly from the class rather than from an object instance.

```lua
local color = Color.FromRGB(255, 120, 40)
```

### Events

Events allow scripts to react when something happens.

Events use signals and can be connected to a callback function.

```lua
part.Touched:Connect(function(other)
    print(other.Name .. " touched the part")
end)
```

Some events provide parameters containing additional information about what occurred.

### Enums

Enums provide a fixed set of named values.

They are commonly used for modes, states, directions, input types, materials, and configuration options.

```lua
part.Material = Material.Metal
```

Using enum values instead of raw numbers or strings makes scripts easier to read and less likely to break.

## Client and server availability

Some APIs are only available in specific script environments.

Server-only APIs can only be accessed from server scripts. These APIs commonly manage secure data, authoritative game state, persistence, moderation, or operations that should not be controlled by players.

Client-only APIs can only be accessed from local scripts. These APIs commonly manage player input, local interfaces, cameras, and effects that only need to appear for one player.

When an API is restricted to one environment, its page will include a notice explaining where it can be used.

## Replication

Many game objects are replicated between the server and connected clients.

Changes made by the server are generally authoritative and may be sent to players automatically. Some objects or properties do not replicate, while others may only replicate in one direction.

Always review the notes on an API page before relying on a property or method for synchronized gameplay.

For secure or competitive systems, important game state should be validated and controlled by the server.

## Creating objects

Objects that support construction can usually be created with `Instance.New()`.

```lua
local part = Instance.New("Part")
part.Name = "Platform"
part.Parent = World
```

Not every documented class can be created manually.

Some classes are abstract and only exist as a base for other classes. Others are static classes, services, or engine-managed objects that BrickVerse creates automatically.

Pages for these classes include a notice explaining how the object is accessed.

## Services

Services are engine-managed objects that provide access to major platform systems.

They are created automatically by BrickVerse and should not normally be created or reparented by scripts.

Depending on the service, it may provide features such as player management, configuration, networking, data storage, input, matchmaking, or world control.

## Type notation

The API uses typed Luau-style notation.

Common primitive types include:

* `string`
* `number`
* `boolean`
* `nil`
* `any`

Collection types may appear in forms such as:

```lua
{ Instance }
```

This represents a collection containing `Instance` objects.

Optional parameters may be marked as optional and may include a default value.

```lua
Destroy(time: number = 0)
```

Union types indicate that more than one type may be accepted or returned.

```lua
Instance | nil
```

A return type of `nil` means the method does not return a value.

## Yielding methods

Some methods wait for an operation to finish before returning.

These methods may pause the current script thread and are marked as yielding or asynchronous in the documentation.

```lua
local child = parent:WaitChild("SpawnPoint")
```

Avoid calling yielding methods repeatedly in performance-sensitive loops unless necessary.

## Obsolete APIs

Obsolete members remain documented for compatibility with older games but should not be used in new projects.

They may be changed or removed in a future engine version. Use the recommended replacement whenever one is listed.

## API availability and changes

BrickVerse is actively developed, and the Game API may change as new engine features are introduced.

New classes and members may be added over time. Existing APIs may receive additional parameters, improved behavior, or updated documentation. Breaking changes will be avoided where practical, but unfinished or experimental APIs may change more frequently.

Check the documentation again when updating older projects or when an API behaves differently than expected.

## Getting started

A good place to begin is with the core object hierarchy and the classes used most often in gameplay scripts:

* `Instance`
* `NetworkedObject`
* `Part`
* `World`
* `Player`
* `Script`
* `Vector2`
* `Vector3`
* `Color`

From there, browse the folders in this section based on the system you are building.

Use the class pages as a reference while scripting, and follow linked types to explore related objects, parameters, return values, and inherited functionality.