# For Unreal Engine Developers

## BrickVerse for Unreal Engine Developers

BrickVerse provides a hosted, authoritative multiplayer runtime with a service-based Game API and scripting through BrickLua, a fork of Luau.

Unreal developers will recognize concepts such as server authority, replicated state, world hierarchies, player objects, collision, and network messages. The implementation is intentionally simpler and platform-managed.

### Terminology at a glance

| Unreal Engine                      | BrickVerse                                 |
| ---------------------------------- | ------------------------------------------ |
| Project or packaged game           | Universe                                   |
| Map / Level                        | World                                      |
| Loaded World hierarchy             | `Scene`                                    |
| Actor                              | `Dynamic` or `Dynamic3D`                   |
| Scene Component                    | Child `Instance` or specialized object     |
| Pawn / Character                   | `BrickversianModel` with character systems |
| PlayerController / player identity | `Player` plus client scripts               |
| GameMode authority                 | Server scripts and `AuthorityService`      |
| Replicated property / RPC          | Instance replication and `NetworkService`  |
| Blueprint Function Library         | `ScriptModule`                             |
| SaveGame or backend service        | `WorldStoreService`                        |
| Config variables / backend flags   | `ENVService`                               |

{% hint style="warning" %}
BrickVerse does not reproduce Unreal's Actor, Component, Pawn, Controller, GameMode, and GameState framework one-for-one. Map the responsibility of your system, not only its class name.
{% endhint %}

### Universes, Worlds, and Scene

A **Universe** is the entire published game.

A **World** is a playable destination within that Universe.

`Scene` exposes the active 3D object hierarchy for the running World.

```lua
local object = Scene:FindFirstChild("Arena")
```

Create runtime objects through the Instance API:

```lua
local wall = Instance.new("Brick")
wall.Name = "ArenaWall"
wall.Parent = Scene
```

### Instances and 3D objects

BrickVerse uses an inheritance-based Instance hierarchy.

| BrickVerse class     | Unreal concept                        |
| -------------------- | ------------------------------------- |
| `Instance`           | Base runtime object                   |
| `Dynamic`            | Runtime-editable object               |
| `Dynamic3D`          | Actor-like object with 3D presence    |
| `BasePart`           | Physical and rendered primitive       |
| `Brick`              | Basic world geometry object           |
| `Model`              | Group or hierarchy of related objects |
| `SpawnPart`          | Player Start                          |
| `BasePartConstraint` | Physics Constraint                    |
| `SpotLight`          | Spot Light                            |
| `OmniLight`          | Point Light                           |
| `DirectionalLight`   | Directional Light                     |

Parent-child structure is central:

```lua
local model = Instance.new("Model")
model.Name = "Door"
model.Parent = Scene

local panel = Instance.new("Brick")
panel.Name = "Panel"
panel.Parent = model
```

### Services

Services are platform-owned systems:

```lua
local Players = game:GetService("Players")
local NetworkService = game:GetService("NetworkService")
local AuthorityService = game:GetService("AuthorityService")
```

| Service              | Responsibility                  |
| -------------------- | ------------------------------- |
| `Players`            | Connected users and characters  |
| `Scene`              | Active World hierarchy          |
| `RunService`         | Runtime and frame execution     |
| `UserInputService`   | Client input                    |
| `InteractionService` | World interaction prompts       |
| `NetworkService`     | Client-server messages          |
| `AuthorityService`   | Execution and authority context |
| `WorldStoreService`  | Persistent data                 |
| `ENVService`         | Live configuration and secrets  |
| `Lighting`           | Lighting and environment        |
| `SoundService`       | Global audio                    |
| `ClientGui`          | Client UI hierarchy             |

This removes the need to build many framework-level manager actors yourself.

### BrickLua instead of C++ or Blueprints

Gameplay code is written in BrickLua.

```lua
local maxHealth: number = 100

local function calculateDamage(baseDamage: number, multiplier: number): number
	return baseDamage * multiplier
end
```

A module replaces many Blueprint Function Library or static helper-class use cases:

```lua
local Combat = {}

function Combat.ClampDamage(value: number): number
	return math.max(0, value)
end

return Combat
```

BrickLua is sandboxed. Native engine internals, arbitrary operating-system APIs, and Unreal-specific APIs are not available.

### Server and client scripts

Use `ServerScript` for authoritative rules.

Use `ClientScript` for input, camera, interface logic, and local presentation.

Use `ScriptModule` for reusable code.

```
ServerScript
├── validates combat
├── awards currency
├── saves data
└── reads secrets

ClientScript
├── reads input
├── updates HUD
├── controls camera
└── requests actions
```

This roughly replaces the distinction between authority-only Unreal logic and locally controlled client behavior.

### Authority and validation

Unreal's authority checks have a direct conceptual parallel in BrickVerse.

Never accept a client message as proof that an action succeeded.

```
Client: "I fired at target 42."
Server:
1. Is this player allowed to fire?
2. Is the weapon equipped?
3. Is the fire rate valid?
4. Is the target hittable?
5. What damage should be applied?
```

The server decides the final state.

Use `AuthorityService` and the current Game API's execution-context facilities when code needs to check where it is running.

### Networking and replication

Instance state intended for clients can replicate through the platform. Explicit client-server messages are handled through `NetworkService`.

Think of `NetworkService` as the BrickVerse layer for RPC-like requests, events, and responses.

Use it for intent and non-instance data, not as a way to let the client own authoritative state.

```lua
-- Conceptual validation
local function requestEquip(player, itemId)
	if type(itemId) ~= "string" then
		return false
	end

	if not playerOwnsItem(player, itemId) then
		return false
	end

	equipItem(player, itemId)
	return true
end
```

### Players and characters

`Player` represents the connected user.

`BrickversianModel` represents the player's in-world character model.

`Humanoid` provides character-oriented behavior such as movement, health, and state.

| BrickVerse            | Unreal                                 |
| --------------------- | -------------------------------------- |
| `Player`              | Player identity and connection         |
| `BrickversianModel`   | Character or Pawn                      |
| `Humanoid`            | Character movement and health behavior |
| `Players.LocalPlayer` | Local owning player                    |
| `Player:Respawn()`    | Restart or respawn pawn                |
| `Player:Kick()`       | Disconnect player                      |

Do not place persistent player identity solely on the character. Characters may be destroyed and respawned while the `Player` remains connected.

### Interactions

`InteractionPrompt` is similar to an interactable prompt placed in the world.

`InteractionService` manages interaction behavior at the service level.

Use prompts for doors, pickups, switches, NPC conversations, and other proximity-based actions. Validate the final action on the server.

### User interfaces

BrickVerse provides instance-based screen UI.

| BrickVerse      | Unreal UMG                    |
| --------------- | ----------------------------- |
| `ScreenUI`      | Root widget added to viewport |
| `Frame`         | Panel or container            |
| `TextLabel`     | Text Block                    |
| `TextButton`    | Button with text              |
| `ImageLabel`    | Image                         |
| `ImageButton`   | Image-based Button            |
| `ScrollFrame`   | Scroll Box                    |
| `ViewportFrame` | Scene or model viewport       |

```lua
local ClientGui = game:GetService("ClientGui")

local screen = Instance.new("ScreenUI")
screen.Name = "HUD"
screen.Parent = ClientGui

local health = Instance.new("TextLabel")
health.Name = "Health"
health.Text = "Health: 100"
health.Parent = screen
```

HUD interaction belongs in client scripts. The server should provide authoritative values.

### Persistent data

`WorldStoreService` is the persistent storage layer.

It is closer to a managed backend service than to a local SaveGame object. Use it for player progression, inventory, settings, and Universe state.

All storage operations should be server-controlled and treated as asynchronous and fallible.

### Configuration and secrets

`ENVService` provides live Universe configuration.

```lua
local ENVService = game:GetService("ENVService")
local playlist = ENVService:GetConfigAsync("ACTIVE_PLAYLIST")
```

Use it for feature flags, event rotation, tuning values, and API configuration.

Values marked as secrets are unavailable to clients.

### Common migration mistakes

#### Building a GameMode clone before learning the services

BrickVerse splits responsibilities across server scripts and built-in services.

#### Assuming client ownership means trust

The client may control input and presentation, but the server validates outcomes.

#### Recreating Unreal's complete framework

Use the simpler BrickVerse hierarchy instead of reproducing Controllers, States, Subsystems, and Components when they are unnecessary.

#### Treating modules as replicated authority

A shared module can be visible to clients. Visibility does not make client execution authoritative.

#### Putting API credentials in client scripts

Read secret values only from server code through `ENVService`.

### First BrickVerse server script

```lua
local Players = game:GetService("Players")

print("Dedicated World server started")

for _, player in Players:GetPlayers() do
	print("Connected:", player.Name)
end
```

The next systems to learn are `NetworkService`, `AuthorityService`, `ClientGui`, and `WorldStoreService`.
