# BrickLua Tutorials

BrickLua is BrickVerse's scripting language. It is based on a fork of Luau and runs inside the BrickVerse sandbox.

This section teaches the language and the Game API through practical examples. The tutorials begin with basic syntax, then move into Instances, players, interfaces, networking, persistence, web requests, NPCs, and reusable gameplay systems.

{% hint style="info" %}
BrickLua uses a fork of Luau, but BrickVerse provides its own object model and Game API. APIs from other platforms are not automatically available.
{% endhint %}

## Tutorial order

1. Your First Script
2. Variables and Types
3. Functions
4. Events
5. Tables
6. Modules
7. Creating Parts
8. Working with Players
9. Building a UI
10. Making a Tool
11. Saving Data
12. Universe Configs
13. Using JSON
14. Using Tags
15. Client vs Server
16. NetworkService
17. HTTP Requests
18. Creating NPCs
19. Leaderboards
20. Inventory Systems
21. Common Scripting Patterns

## Common globals

BrickVerse exposes frequently used services and roots as global objects.

| Global | Purpose |
| --- | --- |
| `world` | The running World and its Instance hierarchy. |
| `Players` | Connected players and player events. |
| `PlayerGUI` | The local player's interface hierarchy. |
| `Datastore` | Server-side persistent data stores. |
| `Http` | HTTP requests. |
| `Stats` | Universe leaderboard statistics. |
| `Input` | Local keyboard, mouse, controller, and touch input. |

## Creating Instances

Use `Instance.New` to create an Instance:

```lua
local part = Instance.New("Part")
part.Name = "Platform"
part.Parent = world
```

You can pass the parent directly:

```lua
local part = Instance.New("Part", world)
part.Name = "Platform"
```

## Events

BrickVerse events support `Connect`, `Once`, `Wait`, and disconnection through the returned connection:

```lua
local connection = part.Touched:Connect(function(other)
	print("Touched by", other.Name)
end)

connection:Disconnect()
```

## Server authority

Client scripts are appropriate for input, camera behavior, interface logic, and local effects. Persistent data, damage, rewards, ownership, and other important state must be validated by a server script.
