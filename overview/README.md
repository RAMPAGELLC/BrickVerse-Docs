# Overview

BrickVerse is a multiplayer game platform with an instance-based Game API and a scripting language based on a fork of Luau.

These guides are written for developers who already understand another engine or platform and want to become productive in BrickVerse without relearning every general game-development concept. Each article focuses on the parts that change when moving to BrickVerse:

* how projects are organized;
* how objects are represented in the instance hierarchy;
* how BrickLua scripts run;
* how client and server execution are separated;
* how core Game API services are accessed;
* and how familiar concepts from another platform translate to BrickVerse.

{% hint style="info" %}
The comparisons in this section are conceptual. Similar systems can have different lifecycle, replication, security, or authority rules. Use the Game API reference as the source of truth for individual classes, properties, methods, and events.
{% endhint %}

### Choose your previous platform

#### Roblox

Start here if you are familiar with Experiences, Places, Instances, Services, Luau, RemoteEvents, DataStores, and Roblox user interfaces.

See **For Roblox Developers**.

#### Unity

Start here if you are familiar with Scenes, GameObjects, Components, MonoBehaviours, Prefabs, C#, and common Unity networking patterns.

See **For Unity Developers**.

#### Unreal Engine

Start here if you are familiar with Levels, Actors, Components, Blueprints, GameModes, replication, and authoritative multiplayer servers.

See **For Unreal Engine Developers**.

#### Godot

Start here if you are familiar with scene trees, Nodes, packed scenes, Resources, signals, GDScript, or Godot multiplayer authority.

See **For Godot Developers**.

#### Web and JavaScript development

Start here if your background is primarily JavaScript or TypeScript and you are familiar with modules, event emitters, asynchronous APIs, object trees, and client-server applications.

See **For Web Developers**.

### BrickVerse terminology

| BrickVerse term  | Meaning                                                   |
| ---------------- | --------------------------------------------------------- |
| **Universe**     | A complete published game or experience.                  |
| **World**        | An individual playable world within a universe.           |
| **Scene**        | The active 3D hierarchy for the running world.            |
| **Instance**     | A runtime object in the BrickVerse hierarchy.             |
| **Service**      | A top-level system obtained through `game:GetService()`.  |
| **BrickLua**     | BrickVerse's scripting language, based on a fork of Luau. |
| **ServerScript** | A script that runs with server authority.                 |
| **ClientScript** | A script that runs on a player's client.                  |
| **ScriptModule** | Reusable BrickLua code loaded with `require`.             |

### The basic scripting model

Services are retrieved from the global `game` object:

```lua
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local WorldStoreService = game:GetService("WorldStoreService")
```

Instances are created with `Instance.new`, configured through properties, and inserted into the hierarchy by assigning a parent:

```lua
local brick = Instance.new("Brick")
brick.Name = "WelcomeBrick"
brick.Parent = Scene
```

BrickLua uses familiar Luau syntax:

```lua
local function greet(name: string): string
	return "Welcome, " .. name
end

print(greet("Builder"))
```

### Core services to learn first

| Service             | Purpose                                                              |
| ------------------- | -------------------------------------------------------------------- |
| `Players`           | Connected players, player lookup, characters, and connection events. |
| `Scene`             | Active replicated 3D world content.                                  |
| `ReplicatedStorage` | Shared objects available to server and clients.                      |
| `ServerStorage`     | Server-only objects and data.                                        |
| `ScriptService`     | Server-side scripts and server startup logic.                        |
| `ClientGui`         | Client-facing interface hierarchy.                                   |
| `RunService`        | Runtime and frame-related execution.                                 |
| `UserInputService`  | Client input.                                                        |
| `NetworkService`    | Client-server communication.                                         |
| `WorldStoreService` | Persistent universe or world data.                                   |
| `WebService`        | Supported outbound web requests.                                     |
| `ENVService`        | Universe configuration and server-only secrets.                      |
| `Lighting`          | World lighting and visual environment.                               |
| `SoundService`      | Global audio behavior.                                               |

### Recommended learning order

1. Learn Universes, Worlds, and the Scene hierarchy.
2. Create and modify Instances.
3. Write a small `ServerScript`.
4. Write a small `ClientScript`.
5. Use a service through `game:GetService()`.
6. Build a basic interface under `ClientGui`.
7. Add client-server communication with `NetworkService`.
8. Save a small value with `WorldStoreService`.
9. Use `ENVService` for live configuration or server-only secrets.

The platform-specific articles explain these systems using terminology from your previous environment.
