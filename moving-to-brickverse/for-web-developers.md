# For Web Developers

## BrickVerse for Web and JavaScript Developers

BrickVerse scripting is approachable for JavaScript and TypeScript developers because BrickLua is dynamic, event-driven, module-friendly, and commonly uses asynchronous service APIs.

The largest difference is the object hierarchy. Instead of manipulating a DOM or application state tree, scripts work with replicated game Instances inside a multiplayer runtime.

### Terminology at a glance

| Web development                       | BrickVerse          |
| ------------------------------------- | ------------------- |
| Application                           | Universe            |
| Route, room, or deployed environment  | World               |
| DOM or component tree                 | Instance hierarchy  |
| DOM root for 3D content               | `Scene`             |
| Object or component instance          | `Instance`          |
| Singleton service                     | Game service        |
| Server process                        | `ServerScript`      |
| Browser script                        | `ClientScript`      |
| ES module                             | `ScriptModule`      |
| EventEmitter / DOM event              | BrickVerse event    |
| fetch wrapper                         | `WebService`        |
| Database or KV store                  | `WorldStoreService` |
| Environment variables / Remote Config | `ENVService`        |
| WebSocket or RPC layer                | `NetworkService`    |

### BrickLua basics

BrickLua is based on a fork of Luau.

```lua
local username: string = "Builder"
local score: number = 100

local function formatScore(name: string, value: number): string
	return name .. ": " .. tostring(value)
end

print(formatScore(username, score))
```

#### JavaScript-to-BrickLua syntax

| JavaScript           | BrickLua                    |
| -------------------- | --------------------------- |
| `const x = 1`        | `local x = 1`               |
| `let x = 1`          | `local x = 1`               |
| `null` / `undefined` | `nil`                       |
| object               | table                       |
| array                | table                       |
| `===`                | `==`                        |
| `!==`                | `~=`                        |
| `&&`                 | `and`                       |
| \`                   |                             |
| `!value`             | `not value`                 |
| template string      | concatenation or formatting |
| `export default`     | `return` from a module      |

A BrickLua table can act like an array:

```lua
local players = { "Alice", "Bob", "Casey" }

for index, name in ipairs(players) do
	print(index, name)
end
```

Or like an object:

```lua
local profile = {
	level = 5,
	xp = 1250,
	title = "Builder"
}

print(profile.level)
```

### Modules

A `ScriptModule` is similar to an ES module:

```lua
local Currency = {}

function Currency.Format(amount: number): string
	return tostring(amount) .. " Cubes"
end

return Currency
```

Load it with `require`:

```lua
local Currency = require(script.Parent.Currency)
print(Currency.Format(500))
```

### Universes, Worlds, and Scene

A **Universe** is the complete published game.

A **World** is a playable destination or environment.

`Scene` is the active 3D hierarchy.

```lua
local brick = Instance.new("Brick")
brick.Name = "Platform"
brick.Parent = Scene
```

Think of `Scene` as a runtime object tree, but one that contains spatial, physical, and replicated game objects rather than HTML elements.

### Instances

Every object in the hierarchy derives from `Instance`.

Useful concepts include:

| BrickVerse       | Web analogy                     |
| ---------------- | ------------------------------- |
| `Instance`       | Base node                       |
| `Parent`         | Parent node                     |
| children         | Child nodes                     |
| property         | Object field or DOM property    |
| event            | EventEmitter or DOM event       |
| `FindFirstChild` | Query by child name             |
| `Instance.new()` | Constructor or element creation |

```lua
local model = Instance.new("Model")
model.Name = "Shop"
model.Parent = Scene
```

### Services

Services are runtime-owned singletons:

```lua
local Players = game:GetService("Players")
local WebService = game:GetService("WebService")
local WorldStoreService = game:GetService("WorldStoreService")
```

| Service             | Purpose                               |
| ------------------- | ------------------------------------- |
| `Players`           | Connected users                       |
| `Scene`             | Active 3D hierarchy                   |
| `ClientGui`         | Client UI                             |
| `UserInputService`  | Keyboard, mouse, and controller input |
| `RunService`        | Runtime callbacks                     |
| `NetworkService`    | Client-server messages                |
| `WorldStoreService` | Persistent data                       |
| `WebService`        | Supported HTTP requests               |
| `ENVService`        | Configuration and secrets             |
| `ReplicatedStorage` | Shared server-client objects          |
| `ServerStorage`     | Server-only objects                   |

### Server and client scripts

A BrickVerse game always has an important trust boundary.

#### `ServerScript`

Comparable to trusted backend code. Use it for:

* database-like storage;
* rewards;
* inventory;
* validation;
* moderation;
* secret API calls;
* and authoritative game state.

#### `ClientScript`

Comparable to browser code. Use it for:

* input;
* UI;
* camera control;
* local effects;
* and requesting actions.

#### `ScriptModule`

Comparable to a shared or server-only package depending on where the module is stored and required.

{% hint style="danger" %}
Client scripts are visible to and controlled by the player. Never store secrets or trust business-critical decisions on the client.
{% endhint %}

### Networking

`NetworkService` is the client-server communication layer.

A useful web analogy is a typed RPC or WebSocket message system.

```
ClientScript
    sends request
        ↓
NetworkService
        ↓
ServerScript
    authenticates through player context
    validates payload
    applies authoritative change
```

Never accept values such as price, currency gain, damage, or ownership directly from a client.

### Asynchronous APIs

Some BrickVerse methods perform storage, configuration, or network work and use asynchronous naming such as `Async`.

```lua
local ENVService = game:GetService("ENVService")
local activeEvent = ENVService:GetConfigAsync("ACTIVE_EVENT")
```

Treat these calls like remote API operations:

* they can take time;
* they can fail;
* they should not be run every frame;
* and they may need error handling or retry behavior.

### Persistent data

`WorldStoreService` is the platform persistence layer.

It is closer to a managed database or key-value store than `localStorage`.

Use it for:

* player profiles;
* progression;
* inventory;
* settings;
* and global Universe state.

Only trusted server scripts should update authoritative stored data.

### Configuration and secrets

`ENVService` combines ideas from environment variables, Remote Config, and feature flags.

```lua
local ENVService = game:GetService("ENVService")
local maintenanceMode = ENVService:GetConfigAsync("MAINTENANCE_MODE")
```

A secret configuration cannot be fetched by clients.

Use secrets for server-side credentials and use normal configuration for values that may be safely exposed.

### Web requests

`WebService` provides supported HTTP communication.

This is similar to `fetch`, but calls are subject to the BrickVerse sandbox, platform permissions, limits, and API design.

Make privileged requests from server scripts. Do not expose API keys to clients.

### User interfaces

BrickVerse UI is an Instance hierarchy, not HTML.

| BrickVerse      | Web concept              |
| --------------- | ------------------------ |
| `ScreenUI`      | Application or page root |
| `Frame`         | `div` or panel           |
| `TextLabel`     | Text element             |
| `TextButton`    | `button`                 |
| `ImageLabel`    | `img`                    |
| `ImageButton`   | Image button             |
| `ScrollFrame`   | Scrollable container     |
| `ViewportFrame` | Embedded 3D preview      |

```lua
local ClientGui = game:GetService("ClientGui")

local screen = Instance.new("ScreenUI")
screen.Name = "HUD"
screen.Parent = ClientGui

local label = Instance.new("TextLabel")
label.Name = "Status"
label.Text = "Connected"
label.Parent = screen
```

UI events should be handled from a client script.

### Events

BrickVerse events are similar to EventEmitter subscriptions or DOM event listeners.

Conceptually:

```lua
-- object.SomeEvent:Connect(function(value)
--     print(value)
-- end)
```

Disconnect subscriptions when the owning system is destroyed if the API does not clean them up automatically.

### Common migration mistakes

#### Treating ClientScript like a secure frontend bundle

Players control the client. Keep authority on the server.

#### Using polling instead of events

Subscribe to object and service events where possible.

#### Calling remote APIs every frame

Cache configuration and rate-limit web operations.

#### Storing data only in module tables

Module state is runtime memory, not persistent storage.

#### Expecting JavaScript syntax

BrickLua is Luau-based. Tables, iteration, equality operators, and module exports differ.

### First BrickVerse script

```lua
local Players = game:GetService("Players")

for _, player in Players:GetPlayers() do
	print("Connected user:", player.Name)
end
```

Then create a `ClientScript`, add a basic UI under `ClientGui`, and send a validated request through `NetworkService`.
