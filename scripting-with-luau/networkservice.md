# NetworkService

BrickVerse client-server communication uses `NetworkEvent` Instances and typed `NetMessage` payloads.

A NetworkEvent can:

- invoke the server;
- invoke one client;
- invoke all clients;
- receive server invocations;
- and receive client invocations.

## Create a NetworkEvent

Create it in a hierarchy visible to both server and clients:

```lua
local event = Instance.New("NetworkEvent")
event.Name = "PurchaseItem"
event.Parent = world
```

For a real game, place network objects in a dedicated shared folder:

```text
World
└── Network
    ├── PurchaseItem
    ├── PurchaseResult
    └── RoundState
```

## Reliable delivery

```lua
event.Reliable = true
```

Reliable events are appropriate for important discrete messages such as purchases or state changes.

Use the current API behavior and avoid sending high-frequency visual data reliably unless necessary.

## Create a NetMessage

```lua
local message = NetMessage.New()
message:AddString("itemId", "sword")
message:AddInt("quantity", 1)
message:AddBool("gift", false)
```

Supported typed fields include:

- string;
- integer;
- number;
- boolean;
- `Vector2`;
- `Vector3`;
- `Color`;
- `Instance`;
- buffer.

## Client to server

ClientScript:

```lua
local network = world:WaitChild("Network")
local purchaseEvent = network:WaitChild("PurchaseItem")

local message = NetMessage.New()
message:AddString("itemId", "sword")
message:AddInt("quantity", 1)

purchaseEvent:InvokeServer(message)
```

ServerScript:

```lua
purchaseEvent.InvokedServer:Connect(function(player, message)
	local itemId = message:GetString("itemId")
	local quantity = message:GetInt("quantity")

	print(player.Name, itemId, quantity)
end)
```

The server callback receives the sending Player automatically.

## Server to one client

```lua
local result = NetMessage.New()
result:AddBool("success", true)
result:AddString("itemId", "sword")

purchaseResult:InvokeClient(result, player)
```

Client:

```lua
purchaseResult.InvokedClient:Connect(function(message)
	local success = message:GetBool("success")
	local itemId = message:GetString("itemId")

	print("Purchase result:", success, itemId)
end)
```

## Server to all clients

```lua
local state = NetMessage.New()
state:AddString("phase", "Playing")
state:AddInt("timeRemaining", 120)

roundState:InvokeClients(state)
```

Each client:

```lua
roundState.InvokedClient:Connect(function(message)
	local phase = message:GetString("phase")
	local timeRemaining = message:GetInt("timeRemaining")

	print(phase, timeRemaining)
end)
```

## Send BrickVerse values

```lua
local message = NetMessage.New()
message:AddVector3("position", Vector3.New(0, 5, 0))
message:AddColor("color", Color.FromRGB(1, 135, 248))
message:AddInstance("target", targetPart)
```

Read:

```lua
local position = message:GetVector3("position")
local color = message:GetColor("color")
local target = message:GetInstance("target")
```

The server must validate that an Instance is allowed and still belongs to the expected hierarchy.

## Validate messages

```lua
local ITEM_CONFIG = {
	sword = {
		price = 250,
		maxQuantity = 1,
	},
	medkit = {
		price = 75,
		maxQuantity = 5,
	},
}

purchaseEvent.InvokedServer:Connect(function(player, message)
	local success, itemId, quantity = pcall(function()
		return
			message:GetString("itemId"),
			message:GetInt("quantity")
	end)

	if not success then
		return
	end

	local definition = ITEM_CONFIG[itemId]

	if not definition then
		return
	end

	quantity = math.floor(quantity)

	if quantity < 1 or quantity > definition.maxQuantity then
		return
	end

	local profile = getProfile(player)

	if not profile then
		return
	end

	local totalPrice = definition.price * quantity

	if profile.coins < totalPrice then
		return
	end

	profile.coins -= totalPrice
	addItem(profile.inventory, itemId, quantity)
end)
```

## Per-player rate limiting

```lua
local requests: { [Player]: number } = {}
local MIN_INTERVAL = 0.2

local function consumeRequest(player: Player): boolean
	local now = os.clock()
	local previous = requests[player] or 0

	if now - previous < MIN_INTERVAL then
		return false
	end

	requests[player] = now
	return true
end

purchaseEvent.InvokedServer:Connect(function(player, message)
	if not consumeRequest(player) then
		return
	end

	-- Validate and handle.
end)

Players.PlayerRemoved:Connect(function(player)
	requests[player] = nil
end)
```

## Request and response IDs

For multiple simultaneous requests, add a request ID:

Client:

```lua
local requestId = tostring(os.clock())

local message = NetMessage.New()
message:AddString("requestId", requestId)
message:AddString("itemId", "sword")

purchaseEvent:InvokeServer(message)
```

Server response:

```lua
local response = NetMessage.New()
response:AddString("requestId", requestId)
response:AddBool("success", true)

purchaseResult:InvokeClient(response, player)
```

## Avoid sending too much data

Prefer small messages:

```lua
message:AddString("itemId", "sword")
message:AddInt("quantity", 1)
```

Do not send an entire replicated inventory when one item changed. Send a focused update or let replicated Instances represent state when appropriate.

## Complete door request

ClientScript:

```lua
local message = NetMessage.New()
message:AddInstance("door", selectedDoor)

doorRequest:InvokeServer(message)
```

ServerScript:

```lua
local lastUse: { [Player]: number } = {}

doorRequest.InvokedServer:Connect(function(player, message)
	local door = message:GetInstance("door")

	if not door or not door:HasTag("Door") then
		return
	end

	if not door:IsDescendantOf(world) then
		return
	end

	local now = os.clock()

	if now - (lastUse[player] or 0) < 1 then
		return
	end

	lastUse[player] = now

	-- Check player distance and permissions here.
	door.Rotation += Vector3.New(0, 90, 0)
end)

Players.PlayerRemoved:Connect(function(player)
	lastUse[player] = nil
end)
```
