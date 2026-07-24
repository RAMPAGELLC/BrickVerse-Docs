# For Roblox Developers

## BrickVerse for Roblox Developers

BrickVerse will feel familiar to Roblox developers because both platforms use an instance hierarchy, service-based APIs, Luau-style scripting, and a multiplayer client-server runtime.

The most important adjustment is not syntax. It is learning the BrickVerse names, authority boundaries, and service responsibilities.

### Terminology at a glance

| Roblox                     | BrickVerse          |
| -------------------------- | ------------------- |
| Experience                 | Universe            |
| Place                      | World               |
| `Workspace`                | `Scene`             |
| `Instance`                 | `Instance`          |
| `ServerScriptService`      | `ScriptService`     |
| `ReplicatedStorage`        | `ReplicatedStorage` |
| `ServerStorage`            | `ServerStorage`     |
| `StarterGui` / `PlayerGui` | `ClientGui`         |
| `Script`                   | `ServerScript`      |
| `LocalScript`              | `ClientScript`      |
| `ModuleScript`             | `ScriptModule`      |
| `DataStoreService`         | `WorldStoreService` |
| `HttpService`              | `WebService`        |
| Remote networking          | `NetworkService`    |
| Experience configuration   | `ENVService`        |

{% hint style="warning" %}
A row in this table means “closest concept,” not “identical API.” Do not assume that Roblox methods, event names, replication rules, or security behavior transfer directly.
{% endhint %}

### Universes and Worlds

A BrickVerse **Universe** is the complete published game. A Universe can contain one or more **Worlds**.

A World is the closest equivalent to a Roblox Place. It contains the playable environment and runtime hierarchy loaded for a server.

```
Universe
├── Starting World
├── Lobby World
└── Match World
```

Use a Universe when thinking about game-wide configuration, persistence, and publishing. Use a World when thinking about a particular playable location or server destination.

### The instance hierarchy

BrickVerse objects derive from `Instance` and are arranged through parent-child relationships.

```lua
local brick = Instance.new("Brick")
brick.Name = "Platform"
brick.Parent = Scene
```

The object only becomes part of the active hierarchy after it is parented.

Common base concepts include:

| BrickVerse class | Purpose                             |
| ---------------- | ----------------------------------- |
| `Instance`       | Base object in the hierarchy.       |
| `Dynamic`        | Editable or runtime-created object. |
| `Dynamic3D`      | Base object with a 3D presence.     |
| `BasePart`       | Base physical part.                 |
| `Brick`          | Basic physical building object.     |
| `SpawnPart`      | Player spawn location.              |
| `Model`          | Container for related objects.      |

`Scene` is the active 3D hierarchy and is the closest equivalent to `Workspace`.

```lua
local spawn = Scene:FindFirstChild("MainSpawn")
```

### Services

Services are obtained through `game:GetService()`:

```lua
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
```

Do not construct services with `Instance.new`. Services are owned by the runtime.

#### Important service mappings

| BrickVerse           | Roblox concept                                |
| -------------------- | --------------------------------------------- |
| `Players`            | `Players`                                     |
| `Scene`              | `Workspace`                                   |
| `ReplicatedStorage`  | `ReplicatedStorage`                           |
| `ServerStorage`      | `ServerStorage`                               |
| `ScriptService`      | `ServerScriptService`                         |
| `ClientGui`          | `StarterGui` and `PlayerGui` responsibilities |
| `RunService`         | `RunService`                                  |
| `UserInputService`   | `UserInputService`                            |
| `Lighting`           | `Lighting`                                    |
| `SoundService`       | `SoundService`                                |
| `ChatService`        | Text chat systems                             |
| `InteractionService` | Proximity interaction management              |
| `WorldStoreService`  | `DataStoreService`                            |
| `WebService`         | `HttpService`                                 |
| `NetworkService`     | Remote communication layer                    |
| `AuthorityService`   | BrickVerse authority and execution context    |
| `ENVService`         | Live universe configuration and secrets       |

### BrickLua

BrickVerse scripting uses **BrickLua**, a fork of Luau. Roblox developers should recognize most everyday syntax immediately:

```lua
local Players = game:GetService("Players")

local function getDisplayName(player): string
	return player.Name
end

for _, player in Players:GetPlayers() do
	print(getDisplayName(player))
end
```

BrickLua supports familiar concepts such as:

* local variables;
* functions;
* tables;
* type annotations;
* modules;
* events;
* coroutines and task-style execution where supported;
* and object-oriented patterns built around instances and metatables.

The exact standard library and sandbox are controlled by BrickVerse. Code that depends on Roblox-only globals or services must be rewritten.

#### Roblox-specific APIs do not automatically exist

This Roblox code:

```lua
local DataStoreService = game:GetService("DataStoreService")
```

becomes a BrickVerse service lookup:

```lua
local WorldStoreService = game:GetService("WorldStoreService")
```

The same applies to remote networking, HTTP access, GUI placement, and platform-specific globals.

### Script types

| BrickVerse     | Roblox         |
| -------------- | -------------- |
| `ServerScript` | `Script`       |
| `ClientScript` | `LocalScript`  |
| `ScriptModule` | `ModuleScript` |

Use server scripts for authoritative game rules, validation, persistence, rewards, and sensitive operations.

Use client scripts for input, camera behavior, local interface logic, and visual effects that do not need server authority.

Use modules to share reusable code:

```lua
-- ScriptModule
local MathHelpers = {}

function MathHelpers.ClampScore(score: number): number
	return math.max(0, score)
end

return MathHelpers
```

```lua
local MathHelpers = require(script.Parent.MathHelpers)
print(MathHelpers.ClampScore(-5))
```

### Players and characters

The `Players` service manages connected users.

```lua
local Players = game:GetService("Players")

for _, player in Players:GetPlayers() do
	print(player.Name)
end
```

Common conceptual mappings include:

| BrickVerse              | Roblox                   |
| ----------------------- | ------------------------ |
| `Player`                | `Player`                 |
| `Players.LocalPlayer`   | `Players.LocalPlayer`    |
| `Players:GetPlayers()`  | `Players:GetPlayers()`   |
| player connection event | `PlayerAdded`            |
| player removal event    | `PlayerRemoving`         |
| `Player:Kick()`         | `Player:Kick()`          |
| `Player:Respawn()`      | `Player:LoadCharacter()` |
| `BrickversianModel`     | Character model          |
| `Humanoid`              | `Humanoid`               |

Keep player rewards, inventory changes, moderation decisions, and persistence on the server.

### Client and server authority

Treat the client as untrusted.

A client can request an action, but the server should decide whether it is allowed.

```
Client input
    ↓
Network request
    ↓
Server validation
    ↓
Authoritative state change
    ↓
Replicated result
```

Never let the client directly decide:

* currency rewards;
* damage outcomes;
* item ownership;
* moderation state;
* paid purchases;
* persistent data;
* or privileged configuration.

`AuthorityService` and the script's execution context help distinguish where code is running. Follow the API reference for exact methods and properties.

### Networking

Roblox developers may expect `RemoteEvent` and `RemoteFunction` instances. BrickVerse centralizes network communication through `NetworkService`.

Use the networking layer to:

* send a client request to the server;
* publish an authoritative result;
* synchronize non-instance data;
* and request a response when necessary.

The exact method names depend on the current Game API. The important migration principle is unchanged: validate every client-provided value on the server.

```lua
-- Conceptual server-side validation
local function purchaseItem(player, itemId)
	if type(itemId) ~= "string" then
		return false
	end

	if not canPurchase(player, itemId) then
		return false
	end

	grantItem(player, itemId)
	return true
end
```

### Replicated and server-only storage

Use `ReplicatedStorage` for objects and modules that must be available to both server and clients.

Use `ServerStorage` for templates, data, or modules that clients must not access.

```
ReplicatedStorage
├── SharedModules
├── SharedAssets
└── NetworkDefinitions

ServerStorage
├── RewardTables
├── PrivateTemplates
└── ServerModules
```

Do not place secrets in replicated objects.

### User interfaces

BrickVerse UI is instance-based.

| BrickVerse      | Roblox           |
| --------------- | ---------------- |
| `ScreenUI`      | `ScreenGui`      |
| `Frame`         | `Frame`          |
| `TextLabel`     | `TextLabel`      |
| `TextButton`    | `TextButton`     |
| `ImageLabel`    | `ImageLabel`     |
| `ImageButton`   | `ImageButton`    |
| `ScrollFrame`   | `ScrollingFrame` |
| `ViewportFrame` | `ViewportFrame`  |

A basic interface can be created like this:

```lua
local ClientGui = game:GetService("ClientGui")

local screen = Instance.new("ScreenUI")
screen.Name = "MainUI"
screen.Parent = ClientGui

local title = Instance.new("TextLabel")
title.Name = "Title"
title.Text = "Welcome to BrickVerse"
title.Parent = screen
```

Input and local interface behavior should normally be handled by a `ClientScript`.

### Persistent data

`WorldStoreService` is the closest equivalent to Roblox's `DataStoreService`.

Use it for data that must survive between sessions, such as:

* player progression;
* unlocked items;
* settings;
* match history;
* and universe-wide state.

Persistence belongs on the server.

```lua
local WorldStoreService = game:GetService("WorldStoreService")

-- Conceptual flow:
-- 1. Read the player's saved data.
-- 2. Apply defaults when no data exists.
-- 3. Update in-memory server state.
-- 4. Save validated state through the store API.
```

Expect asynchronous methods and failure cases. Production code should handle rejected requests, unavailable data, and retry rules without duplicating rewards.

### Universe configuration and secrets

`ENVService` provides live configuration values.

```lua
local ENVService = game:GetService("ENVService")
local eventName = ENVService:GetConfigAsync("CURRENT_EVENT")
```

Configurations can be useful for:

* enabling seasonal events;
* changing reward multipliers;
* rotating promotional codes;
* selecting API environments;
* and controlling feature flags without republishing.

A configuration marked as secret cannot be fetched by clients. Secret values should only be read by server code.

Server code can update supported values:

```lua
ENVService:SetConfigAsync("CURRENT_EVENT", "SUMMER")
```

### Web requests

Use `WebService` for supported outbound requests.

Do not embed private API keys in client scripts or replicated objects. Store secrets through server-only configuration and make privileged requests from the server.

### Common migration mistakes

#### Assuming every Roblox global exists

BrickLua is based on Luau, but Roblox-specific services and globals are not automatically available.

#### Trusting client requests

Client scripts can be modified. Validate requests on the server.

#### Putting secrets in replicated storage

Anything replicated to clients should be treated as public.

#### Treating a World as the whole game

A World is one playable location. The Universe is the complete published game.

#### Translating names without checking behavior

A similarly named service may still have different events, parameters, or lifecycle rules.

### First BrickVerse script

Create a `ServerScript` and use the `Players` service:

```lua
local Players = game:GetService("Players")

print("Server script started")

for _, player in Players:GetPlayers() do
	print("Connected player:", player.Name)
end
```

Then create a `ClientScript` for local UI or input:

```lua
local Players = game:GetService("Players")
local localPlayer = Players.LocalPlayer

print("Running for:", localPlayer.Name)
```

Once those are working, learn `NetworkService`, `WorldStoreService`, and `ENVService`.
