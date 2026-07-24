# Client vs Server

BrickVerse multiplayer games run across an authoritative server and individual player clients.

Understanding the trust boundary is essential.

## ServerScript

A `ServerScript` runs on the server.

Use it for:

- damage;
- rewards;
- currency;
- inventory ownership;
- persistent data;
- moderation;
- game rules;
- NPC decisions;
- privileged HTTP requests;
- and secret configuration.

## ClientScript

A `ClientScript` runs for one player.

Use it for:

- keyboard, mouse, touch, and controller input;
- PlayerGUI;
- camera behavior;
- local effects;
- local animation;
- and requesting actions from the server.

## ModuleScript

A `ModuleScript` runs where it is required.

A module used by a ClientScript is still client code. A module used by a ServerScript is server code.

## What the client can change

A player controls their local client. Assume they can:

- invoke network events manually;
- modify request values;
- call requests more quickly than intended;
- skip client cooldowns;
- alter local UI;
- read replicated code and data;
- and report false positions or targets.

Client code improves the user experience. It does not establish trust.

## Authoritative flow

```text
Client detects input
        ↓
Client sends requested action
        ↓
Server validates player and payload
        ↓
Server checks cooldown and game state
        ↓
Server applies the result
        ↓
Server notifies clients
```

## Unsafe purchase flow

```lua
-- ClientScript: unsafe design
purchaseEvent:InvokeServer(message)

-- ServerScript: unsafe
purchaseEvent.InvokedServer:Connect(function(player, message)
	local price = message:GetInt("price")
	removeCoins(player, price)
	grantItem(player, message:GetString("itemId"))
end)
```

The client controls `price`.

## Safe purchase flow

The client sends only intent:

```lua
local message = NetMessage.New()
message:AddString("itemId", "sword")

purchaseEvent:InvokeServer(message)
```

The server owns the price:

```lua
local ITEMS = {
	sword = {
		price = 250,
	},
}

purchaseEvent.InvokedServer:Connect(function(player, message)
	local itemId = message:GetString("itemId")
	local definition = ITEMS[itemId]

	if not definition then
		return
	end

	local profile = getProfile(player)

	if not profile or profile.coins < definition.price then
		return
	end

	profile.coins -= definition.price
	addItem(profile.inventory, itemId, 1)
end)
```

## Validate types

```lua
local function validItemId(value: any): boolean
	return type(value) == "string"
		and #value >= 1
		and #value <= 64
end
```

For `NetMessage`, use the correct typed getter and handle invalid messages through `pcall` when needed.

## Validate state

Type validation is not enough:

```lua
local function canOpenDoor(player: Player, door: Instance): boolean
	if not door:HasTag("Door") then
		return false
	end

	if player.IsDead then
		return false
	end

	if not player.Character then
		return false
	end

	-- Add distance, permission, and game-state checks.
	return true
end
```

## Rate limiting

```lua
local lastRequest: { [Player]: number } = {}
local COOLDOWN = 0.25

local function useRequest(player: Player): boolean
	local now = os.clock()
	local previous = lastRequest[player] or 0

	if now - previous < COOLDOWN then
		return false
	end

	lastRequest[player] = now
	return true
end

Players.PlayerRemoved:Connect(function(player)
	lastRequest[player] = nil
end)
```

Use separate rate limits for separate actions.

## Client-side UI

A client may predict UI immediately:

```lua
button.Clicked:Connect(function()
	button.Text = "Purchasing..."
	sendPurchaseRequest()
end)
```

But it should wait for the server result before showing ownership:

```lua
resultEvent.InvokedClient:Connect(function(message)
	local success = message:GetBool("success")

	if success then
		button.Text = "Owned"
	else
		button.Text = "Purchase"
	end
end)
```

## Replicated objects

Anything visible to the client should be treated as public:

- shared modules;
- NetworkEvents;
- UI assets;
- replicated configuration;
- replicated Instance properties.

Do not store passwords, secret tokens, moderation credentials, or private business rules in replicated content.

## Server-only data

Keep private data in server-only hierarchy or server module memory:

```lua
local PRIVATE_REWARD_TABLE = {
	daily = 100,
	weekly = 750,
}
```

Secret Universe Config values should only be read on the server.

## Client input example

ClientScript:

```lua
local jumpAction = Input:BindButton("JumpRequest")

jumpAction.Pressed:Connect(function()
	local message = NetMessage.New()
	message:AddString("action", "jump")

	actionEvent:InvokeServer(message)
end)
```

ServerScript:

```lua
actionEvent.InvokedServer:Connect(function(player, message)
	if message:GetString("action") ~= "jump" then
		return
	end

	if player.IsDead or not player.CanMove then
		return
	end

	player:Jump()
end)
```

## Server checklist

Before applying an action, ask:

1. Is the sender a valid Player?
2. Is the message type correct?
3. Is the requested object valid and still in the World?
4. Does the Player own or have permission to use it?
5. Is the Player close enough?
6. Has the cooldown elapsed?
7. Is the current round or state compatible?
8. Are amounts clamped to server limits?
9. Can the operation be repeated for duplicate rewards?
10. Should the action be logged?

## Rule of thumb

The client asks.

The server decides.
