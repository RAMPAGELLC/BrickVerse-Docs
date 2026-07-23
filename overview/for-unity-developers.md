# For Unity Developers

## BrickVerse for Unity Developers

BrickVerse is not a general-purpose engine project that you compile and ship yourself. It is a hosted multiplayer game platform with an instance hierarchy, built-in services, integrated publishing, and sandboxed scripting through BrickLua.

Unity developers should think less in terms of assembling packages and singleton managers, and more in terms of creating objects inside a managed runtime.

### Terminology at a glance

| Unity                        | BrickVerse                                       |
| ---------------------------- | ------------------------------------------------ |
| Project or published game    | Universe                                         |
| Scene                        | World                                            |
| Active scene hierarchy       | `Scene`                                          |
| GameObject                   | `Dynamic` or another `Instance`                  |
| Transform-bearing GameObject | `Dynamic3D`                                      |
| Prefab                       | Reusable model or asset                          |
| MonoBehaviour                | `ServerScript` or `ClientScript`                 |
| ScriptableObject             | Asset, configuration, or module depending on use |
| Static manager               | Service                                          |
| C# event / UnityEvent        | BrickVerse event                                 |
| Persistent backend           | `WorldStoreService`                              |
| Network manager / RPC layer  | `NetworkService`                                 |

{% hint style="info" %}
BrickVerse objects do not use Unity's exact GameObject-and-Component model. The closest mapping depends on the object. Treat these as mental shortcuts, not class equivalence.
{% endhint %}

### Universes and Worlds

A **Universe** is the complete game.

A **World** is an individual playable environment inside that Universe.

This is similar to a Unity project containing multiple scenes, but BrickVerse Worlds are published platform destinations with multiplayer runtime behavior.

```
Universe
├── Lobby World
├── Main World
└── Competitive World
```

### The Scene hierarchy

The active 3D world is exposed through `Scene`.

```lua
local platform = Instance.new("Brick")
platform.Name = "StartingPlatform"
platform.Parent = Scene
```

Unity developers can think of `Scene` as the active scene hierarchy and an `Instance` as an object managed by the runtime.

Common 3D classes include:

| BrickVerse           | Unity concept                                            |
| -------------------- | -------------------------------------------------------- |
| `Dynamic3D`          | Object with a transform                                  |
| `BasePart`           | Rendered and physical scene object                       |
| `Brick`              | Primitive GameObject with rendering and physics behavior |
| `Model`              | Parent container for related objects                     |
| `SpawnPart`          | Spawn-point object                                       |
| `SpotLight`          | Spot Light                                               |
| `OmniLight`          | Point Light                                              |
| `DirectionalLight`   | Directional Light                                        |
| `BasePartConstraint` | Joint or constraint                                      |

### Services instead of manager objects

Core systems are provided as services:

```lua
local Players = game:GetService("Players")
local Lighting = game:GetService("Lighting")
local RunService = game:GetService("RunService")
```

This replaces many patterns where a Unity project would create persistent manager GameObjects.

| BrickVerse service  | Unity responsibility              |
| ------------------- | --------------------------------- |
| `Players`           | Connected-player manager          |
| `Scene`             | Active world hierarchy            |
| `Lighting`          | Lighting and environment settings |
| `SoundService`      | Global audio management           |
| `RunService`        | Runtime state and frame callbacks |
| `UserInputService`  | Input system                      |
| `ClientGui`         | Runtime UI root                   |
| `NetworkService`    | Multiplayer messages and requests |
| `WorldStoreService` | Persistent backend                |
| `WebService`        | HTTP integration                  |
| `ENVService`        | Remote configuration and secrets  |

Do not instantiate services. Retrieve them through `game:GetService()`.

### BrickLua instead of C\#

Gameplay scripts are written in BrickLua, a fork of Luau.

```lua
local speed: number = 12

local function calculateDistance(time: number): number
	return speed * time
end

print(calculateDistance(2))
```

Common translations:

| C#                               | BrickLua                       |
| -------------------------------- | ------------------------------ |
| `var` or explicit local variable | `local`                        |
| class utility                    | module table                   |
| `List<T>`                        | table                          |
| `Dictionary<TKey,TValue>`        | table                          |
| `event`                          | BrickVerse event               |
| coroutine / async operation      | coroutine or async API pattern |
| `null`                           | `nil`                          |

A reusable module looks like this:

```lua
local Rewards = {}

function Rewards.Calculate(level: number): number
	return 100 + level * 25
end

return Rewards
```

### Script execution

Use a `ServerScript` for authoritative game state and a `ClientScript` for local presentation and input.

#### Server responsibilities

* damage validation;
* inventory and rewards;
* persistent data;
* matchmaking decisions;
* moderation;
* privileged web requests;
* and secret configuration.

#### Client responsibilities

* keyboard, mouse, and controller input;
* interface behavior;
* camera behavior;
* local effects;
* and sending requests to the server.

This is similar to separating dedicated-server code from a Unity client, except the execution model is built directly into the BrickVerse hierarchy.

### Lifecycle thinking

Do not mechanically translate `Awake`, `Start`, `Update`, and `OnDestroy`.

Instead, identify what the code is trying to do:

* initialize when the script begins;
* subscribe to an event;
* run each frame through `RunService`;
* react to an Instance being added or removed;
* or clean up when the script or object leaves the hierarchy.

```lua
local RunService = game:GetService("RunService")

-- Subscribe using the event exposed by the current RunService API.
-- Keep expensive work out of per-frame callbacks.
```

Follow the API reference for the exact runtime events currently exposed.

### Networking

Use `NetworkService` for communication between clients and the authoritative server.

A Unity developer may compare this to RPCs, Commands, ClientRPCs, or messages in a networking package.

The security rule is simple:

```
Client proposes an action.
Server validates the action.
Server changes authoritative state.
Clients receive the result.
```

Never trust a client-provided price, reward, damage value, or ownership claim.

### Shared and private content

Use `ReplicatedStorage` for modules and objects that both sides require.

Use `ServerStorage` for private templates, rules, and data.

```
ReplicatedStorage
├── SharedModules
└── SharedAssets

ServerStorage
├── ServerModules
├── PrivateTemplates
└── RewardDefinitions
```

This is more explicit than placing everything under a Unity Resources folder. Replicated content must be considered visible to clients.

### User interfaces

BrickVerse UI is instance-based rather than built with Unity UI components.

| BrickVerse      | Unity UI concept                 |
| --------------- | -------------------------------- |
| `ScreenUI`      | Canvas                           |
| `Frame`         | Panel                            |
| `TextLabel`     | Text or TMP text                 |
| `TextButton`    | Button with text                 |
| `ImageLabel`    | Image                            |
| `ImageButton`   | Image-based Button               |
| `ScrollFrame`   | Scroll View                      |
| `ViewportFrame` | Render texture-style 3D viewport |

```lua
local ClientGui = game:GetService("ClientGui")

local screen = Instance.new("ScreenUI")
screen.Name = "HUD"
screen.Parent = ClientGui

local score = Instance.new("TextLabel")
score.Name = "Score"
score.Text = "Score: 0"
score.Parent = screen
```

Create local interaction logic in a `ClientScript`.

### Persistent data

`WorldStoreService` provides persistent storage.

Unlike saving a local file with `PlayerPrefs`, this is server-side platform storage intended for multiplayer state.

Use it for:

* progression;
* inventory;
* settings;
* unlocked content;
* and universe state.

Handle storage calls as asynchronous operations that can fail. Keep an authoritative in-memory representation while a player is connected, validate mutations, and save through server code.

### Live configuration

`ENVService` provides Universe configuration.

```lua
local ENVService = game:GetService("ENVService")
local multiplier = ENVService:GetConfigAsync("XP_MULTIPLIER")
```

Use it as a replacement for some Remote Config, environment-variable, and feature-flag workflows.

Configurations marked as secrets are server-only and cannot be fetched by clients.

### Assets and reusable content

A Unity Prefab is closest to a reusable BrickVerse model or asset.

The key difference is that assets are managed and distributed by the platform. Scripts interact with the loaded Instances rather than directly loading arbitrary local project files.

### Common migration mistakes

#### Recreating Unity managers as scene objects

Check whether BrickVerse already provides the system as a service.

#### Expecting components on every object

BrickVerse has its own class hierarchy. Find the appropriate Instance class instead of assuming a GameObject-plus-component design.

#### Running authoritative logic on the client

Move rewards, inventory, persistence, and validation to a `ServerScript`.

#### Storing secrets in scripts

Use server-only configuration through `ENVService`.

#### Porting Update loops directly

Prefer events. Use frame callbacks only for work that genuinely must happen every frame.

### First BrickVerse script

```lua
local Players = game:GetService("Players")

print("World server started")

for _, player in Players:GetPlayers() do
	print("Player:", player.Name)
end
```

After creating a server script, build a small client interface and then connect both sides through `NetworkService`.
