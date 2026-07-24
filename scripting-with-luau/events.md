# Events

Events allow scripts to react when something happens. They are preferable to repeatedly checking state in a loop.

BrickVerse signals support:

- `Connect`
- `Disconnect`
- `Once`
- `Wait`

## Connecting to an event

```lua
Players.PlayerAdded:Connect(function(player)
	print(player.Name, "joined the server")
end)
```

The callback receives the values documented by the event.

## Store the connection

`Connect` returns a connection object:

```lua
local connection = Players.PlayerAdded:Connect(function(player)
	print(player.Name, "joined")
end)
```

Disconnect it when the listener is no longer needed:

```lua
connection:Disconnect()
```

## Part events

Physical objects expose interaction and collision events.

```lua
local pad = world:WaitChild("LaunchPad")

pad.Touched:Connect(function(other)
	print("Touched by", other.Name)
end)

pad.TouchEnded:Connect(function(other)
	print("Stopped touching", other.Name)
end)
```

A Part can also expose mouse and click events:

```lua
pad.MouseEnter:Connect(function()
	pad.Color = Color.FromRGB(60, 180, 255)
end)

pad.MouseExit:Connect(function()
	pad.Color = Color.FromRGB(1, 135, 248)
end)

pad.Clicked:Connect(function(player)
	print(player.Name, "clicked the pad")
end)
```

{% hint style="warning" %}
A click event identifies the requesting player, but a server script must still validate range, cooldown, ownership, and any other requirements.
{% endhint %}

## Player events

```lua
Players.PlayerAdded:Connect(function(player)
	print(player.Name, "joined")
end)

Players.PlayerRemoved:Connect(function(player)
	print(player.Name, "left")
end)
```

Individual players expose events such as:

```lua
player.Chatted:Connect(function(message)
	print(player.Name .. ":", message)
end)

player.Respawned:Connect(function()
	print(player.Name, "respawned")
end)
```

## Instance hierarchy events

Instances report child changes:

```lua
local folder = Instance.New("Folder", world)
folder.Name = "Enemies"

folder.ChildAdded:Connect(function(child)
	print("Added enemy:", child.Name)
end)

folder.ChildRemoved:Connect(function(child)
	print("Removed enemy:", child.Name)
end)
```

Networked objects also expose lifecycle events:

```lua
part.Destroying:Connect(function()
	print(part.Name, "is being destroyed")
end)

part.TreeEntered:Connect(function()
	print(part.Name, "entered the hierarchy")
end)

part.TreeExited:Connect(function()
	print(part.Name, "left the hierarchy")
end)
```

## Property changes

Use `PropertyChanged` when you need to observe property updates:

```lua
part.PropertyChanged:Connect(function(propertyName)
	if propertyName == "Color" then
		print("The Part color changed")
	end
end)
```

Prefer a more specific event when one exists.

## Run once

`Once` invokes the callback a single time:

```lua
Players.PlayerAdded:Once(function(player)
	print("The first player is", player.Name)
end)
```

This is useful for one-time initialization.

## Wait for an event

`Wait` pauses the current script thread until the event fires:

```lua
local player = Players.PlayerAdded:Wait()
print(player.Name, "was the next player to join")
```

Do not block an important startup path unnecessarily. Event connections are often more flexible.

## Avoid duplicate connections

This creates a new connection each time `setup` runs:

```lua
local function setup()
	part.Touched:Connect(function(other)
		print(other.Name)
	end)
end
```

Calling `setup` more than once causes duplicate callbacks.

Track the connection:

```lua
local touchConnection = nil

local function setup()
	if touchConnection then
		touchConnection:Disconnect()
	end

	touchConnection = part.Touched:Connect(function(other)
		print(other.Name)
	end)
end
```

## Debouncing repeated events

Touch and click events may fire rapidly. Use a debounce:

```lua
local busy = false

part.Touched:Connect(function(other)
	if busy then
		return
	end

	busy = true
	print("Activated by", other.Name)

	task.delay(1, function()
		busy = false
	end)
end)
```

For multiplayer actions, use a per-player cooldown rather than one global boolean:

```lua
local lastActivation: { [Player]: number } = {}
local COOLDOWN = 1.5

part.Clicked:Connect(function(player)
	local now = os.clock()
	local previous = lastActivation[player] or 0

	if now - previous < COOLDOWN then
		return
	end

	lastActivation[player] = now
	print(player.Name, "activated the Part")
end)

Players.PlayerRemoved:Connect(function(player)
	lastActivation[player] = nil
end)
```

## Custom events

Use `BindableEvent` for communication between scripts on the same side:

```lua
local event = Instance.New("BindableEvent")
event.Name = "RoundStarted"
event.Parent = script.Parent

event.Invoked:Connect(function()
	print("The round started")
end)

event:Invoke({
	round = 1,
	duration = 120,
})
```

Use `NetworkEvent` instead when communicating between client and server.

## Complete checkpoint example

```lua
local checkpoint = world:WaitChild("Checkpoint")
local reached: { [Player]: boolean } = {}

checkpoint.Clicked:Connect(function(player)
	if reached[player] then
		return
	end

	reached[player] = true
	checkpoint.Color = Color.FromRGB(0, 220, 120)

	print(player.Name, "reached the checkpoint")
end)

Players.PlayerRemoved:Connect(function(player)
	reached[player] = nil
end)
```
