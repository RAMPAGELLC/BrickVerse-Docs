# For Godot Developers

## BrickVerse for Godot Developers

BrickVerse uses Godot technology internally, but BrickVerse games do not directly use the full Godot Engine API. Creators build against the BrickVerse Game API and write gameplay scripts in BrickLua, a fork of Luau.

Godot experience is still useful because the runtime has familiar ideas: a hierarchy of objects, parent-child ownership, signals or events, 3D nodes, resources, client-server authority, and scene-based organization.

### Terminology at a glance

| Godot                         | BrickVerse                         |
| ----------------------------- | ---------------------------------- |
| Project                       | Universe                           |
| Main scene or level scene     | World                              |
| SceneTree branch              | `Scene` hierarchy                  |
| `Node`                        | `Instance`                         |
| `Node3D`                      | `Dynamic3D`                        |
| PackedScene                   | Reusable model or asset            |
| Resource                      | Asset or resource object           |
| Signal                        | Event                              |
| Autoload singleton            | Service                            |
| GDScript / C# script          | BrickLua script                    |
| Multiplayer RPC               | `NetworkService`                   |
| Config or backend persistence | `ENVService` / `WorldStoreService` |

{% hint style="info" %}
Do not use Godot classes, methods, or annotations inside BrickLua unless the BrickVerse Game API explicitly exposes them.
{% endhint %}

### Universes and Worlds

A **Universe** is the complete published game.

A **World** is an individual playable environment.

The active World exposes its 3D hierarchy through `Scene`.

```lua
local building = Scene:FindFirstChild("Building")
```

This is conceptually similar to accessing a branch of the active SceneTree, but the object model is BrickVerse-specific.

### Instances and hierarchy

All hierarchy objects derive from `Instance`.

```lua
local brick = Instance.new("Brick")
brick.Name = "Floor"
brick.Parent = Scene
```

Assigning `Parent` inserts the object into the hierarchy.

| BrickVerse           | Godot concept                   |
| -------------------- | ------------------------------- |
| `Instance`           | `Node`                          |
| `Dynamic`            | Runtime-editable Node           |
| `Dynamic3D`          | `Node3D`                        |
| `BasePart`           | Mesh/physics-oriented 3D object |
| `Brick`              | Primitive 3D body               |
| `Model`              | Node used to group a hierarchy  |
| `SpawnPart`          | Spawn marker                    |
| `BasePartConstraint` | Joint                           |
| `SpotLight`          | `SpotLight3D`                   |
| `OmniLight`          | `OmniLight3D`                   |
| `DirectionalLight`   | `DirectionalLight3D`            |

Unlike a raw Godot project, you should not assume access to every engine Node type.

### Services instead of autoloads

BrickVerse provides global systems through `game:GetService()`:

```lua
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local SoundService = game:GetService("SoundService")
```

| BrickVerse service  | Godot-style responsibility             |
| ------------------- | -------------------------------------- |
| `Players`           | Multiplayer peer and player management |
| `Scene`             | Active world hierarchy                 |
| `RunService`        | Runtime and frame execution            |
| `UserInputService`  | Input singleton                        |
| `Lighting`          | World environment and lighting         |
| `SoundService`      | Global audio                           |
| `ClientGui`         | UI root                                |
| `NetworkService`    | RPC and network messaging              |
| `AuthorityService`  | Multiplayer authority context          |
| `WorldStoreService` | Persistent backend                     |
| `ENVService`        | Remote configuration and secrets       |

Do not create your own copy of a built-in service.

### BrickLua instead of GDScript

BrickLua uses Luau syntax:

```lua
local playerSpeed: number = 10

local function calculateTravelTime(distance: number): number
	return distance / playerSpeed
end
```

Common syntax comparisons:

| GDScript            | BrickLua                |
| ------------------- | ----------------------- |
| `var value = 1`     | `local value = 1`       |
| `func move():`      | `local function move()` |
| `null`              | `nil`                   |
| `Array`             | table                   |
| `Dictionary`        | table                   |
| signal connection   | event connection        |
| script class helper | module table            |

A module:

```lua
local Strings = {}

function Strings.FormatScore(score: number): string
	return "Score: " .. tostring(score)
end

return Strings
```

BrickLua is sandboxed and cannot call arbitrary Godot, .NET, filesystem, or operating-system APIs.

### Server and client execution

Godot developers familiar with multiplayer authority should apply the same security principles.

Use `ServerScript` for:

* authoritative world rules;
* damage and rewards;
* inventory;
* persistence;
* moderation;
* server-only web requests;
* and secrets.

Use `ClientScript` for:

* local input;
* camera behavior;
* UI;
* local visual effects;
* and network requests.

Use `ScriptModule` for reusable code.

### Events instead of direct signal assumptions

BrickVerse objects expose events through the Game API.

The exact connection method and event names are defined per class. Treat them like Godot signals conceptually:

```lua
-- Conceptual shape:
-- object.SomeEvent:Connect(function(value)
--     print(value)
-- end)
```

Prefer events over polling whenever possible.

### Frame processing

`RunService` provides runtime and frame-related execution.

Do not port `_process` or `_physics_process` blindly. Ask whether the operation can be triggered by an event instead.

Good frame-loop uses include:

* camera interpolation;
* local visual animation;
* continuously sampled input;
* and effects that genuinely change every frame.

Avoid expensive searches, persistence calls, or network requests every frame.

### Networking and authority

`NetworkService` handles explicit communication.

Conceptually:

| Godot multiplayer       | BrickVerse                                   |
| ----------------------- | -------------------------------------------- |
| RPC to authority        | Client request through `NetworkService`      |
| authority validates     | Server script validates                      |
| replicated result       | Server publishes or changes replicated state |
| peer-local presentation | Client script                                |

Never allow a client to determine final damage, currency, inventory, or saved state.

### Shared and server-only objects

`ReplicatedStorage` contains objects needed by both server and clients.

`ServerStorage` contains private server objects.

This resembles separating replicated resources from authority-only server data, but it is enforced through the BrickVerse runtime hierarchy.

### UI

BrickVerse UI classes are similar in purpose to Godot Control nodes.

| BrickVerse      | Godot                                |
| --------------- | ------------------------------------ |
| `ScreenUI`      | `CanvasLayer` or UI root             |
| `Frame`         | `Panel` or `Control` container       |
| `TextLabel`     | `Label`                              |
| `TextButton`    | `Button`                             |
| `ImageLabel`    | `TextureRect`                        |
| `ImageButton`   | `TextureButton`                      |
| `ScrollFrame`   | `ScrollContainer`                    |
| `ViewportFrame` | `SubViewportContainer`-style display |

```lua
local ClientGui = game:GetService("ClientGui")

local screen = Instance.new("ScreenUI")
screen.Name = "Menu"
screen.Parent = ClientGui

local button = Instance.new("TextButton")
button.Name = "PlayButton"
button.Text = "Play"
button.Parent = screen
```

Handle UI input in a `ClientScript`.

### Persistent data

Use `WorldStoreService` instead of local files or `ConfigFile` for authoritative game data.

Persistent calls should run on the server and be treated as asynchronous operations that may fail.

### Live configuration and secrets

`ENVService` provides live Universe configuration:

```lua
local ENVService = game:GetService("ENVService")
local enabled = ENVService:GetConfigAsync("NEW_LOBBY_ENABLED")
```

Secret values are server-only.

Use configuration for feature flags, event selection, tuning, promotional codes, and external service settings.

### Common migration mistakes

#### Calling Godot APIs from BrickLua

BrickVerse exposes its own API, not the complete engine API.

#### Rebuilding autoloads that already exist as services

Check `game:GetService()` first.

#### Assuming a client peer is authoritative

Keep important state changes on the server.

#### Porting `_process` everywhere

Prefer events and targeted runtime callbacks.

#### Treating WorldStoreService like a local save file

It is a shared platform backend and requires server-side validation and failure handling.

### First BrickVerse script

```lua
local Players = game:GetService("Players")

print("World loaded")

for _, player in Players:GetPlayers() do
	print(player.Name)
end
```

After that, create a client UI, subscribe to an event, and learn `NetworkService`.
