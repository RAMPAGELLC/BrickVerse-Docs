# Functions

Functions group reusable behavior. They can accept arguments, return values, call other functions, and be passed to events as callbacks.

## Declaring a function

```lua
local function greet()
	print("Welcome to BrickVerse")
end

greet()
```

## Parameters

Parameters pass values into a function:

```lua
local function greetPlayer(playerName: string)
	print("Welcome, " .. playerName)
end

greetPlayer("Builder")
```

## Return values

Use `return` to send a result back:

```lua
local function calculateReward(level: number): number
	return 50 + level * 10
end

local reward = calculateReward(5)
print(reward)
```

A function stops when it reaches `return`:

```lua
local function canPurchase(coins: number, price: number): boolean
	if price < 0 then
		return false
	end

	return coins >= price
end
```

## Multiple return values

BrickLua functions can return more than one value:

```lua
local function divide(a: number, b: number): (boolean, number?)
	if b == 0 then
		return false, nil
	end

	return true, a / b
end

local success, result = divide(10, 2)

if success then
	print(result)
end
```

## Guard clauses

Guard clauses reject invalid input early and keep code readable:

```lua
local function damageNPC(npc: Instance, amount: number)
	if not npc:IsA("NPC") then
		warn("damageNPC expected an NPC")
		return
	end

	if amount <= 0 then
		return
	end

	if npc.IsDead then
		return
	end

	npc:TakeDamage(amount)
end
```

## Functions as values

Functions can be stored in variables:

```lua
local announce = function(message: string)
	print("[Announcement]", message)
end

announce("The round has started")
```

They can also be passed into other functions:

```lua
local function repeatAction(count: number, action: (number) -> ())
	for index = 1, count do
		action(index)
	end
end

repeatAction(3, function(index)
	print("Run", index)
end)
```

## Event callbacks

`Connect` receives a function:

```lua
Players.PlayerAdded:Connect(function(player)
	print(player.Name, "joined")
end)
```

You can use a named function instead:

```lua
local function onPlayerAdded(player: Player)
	print(player.Name, "joined")
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

Named functions are useful when the callback is large or used more than once.

## Methods and the colon syntax

A method belongs to an object:

```lua
part:Destroy()
part:AddTag("Collectible")
```

The colon passes the object automatically. These are conceptually equivalent:

```lua
part:AddTag("Collectible")
Instance.AddTag(part, "Collectible")
```

Use the colon for Game API methods.

## Optional parameters

A parameter can be optional:

```lua
local function announce(message: string, prefix: string?)
	local finalPrefix = prefix or "Server"
	print("[" .. finalPrefix .. "] " .. message)
end

announce("Round starting")
announce("Maintenance soon", "Notice")
```

## Default values

Use `or` to supply a default:

```lua
local function createPlatform(name: string?, position: Vector3?)
	local part = Instance.New("Part", world)
	part.Name = name or "Platform"
	part.Position = position or Vector3.Zero
	part.Size = Vector3.New(8, 1, 8)
	part.Anchored = true

	return part
end
```

## Closures

A closure remembers variables from its outer scope:

```lua
local touches = 0

local part = Instance.New("Part", world)
part.Touched:Connect(function()
	touches += 1
	print("Touches:", touches)
end)
```

Closures are useful, but be careful when they keep references alive longer than intended.

## Factory functions

A factory creates configured Instances:

```lua
local function createPart(
	name: string,
	position: Vector3,
	size: Vector3,
	color: Color
): Instance
	local part = Instance.New("Part", world)
	part.Name = name
	part.Position = position
	part.Size = size
	part.Color = color
	part.Anchored = true
	part.CanCollide = true

	return part
end

createPart(
	"BluePlatform",
	Vector3.New(0, 2, 0),
	Vector3.New(10, 1, 10),
	Color.FromRGB(1, 135, 248)
)
```

## Validation functions

Server scripts should validate client requests through small focused functions:

```lua
local function isFiniteNumber(value: any): boolean
	return type(value) == "number"
		and value == value
		and value ~= math.huge
		and value ~= -math.huge
end

local function isValidPurchaseAmount(value: any): boolean
	return isFiniteNumber(value)
		and value >= 1
		and value <= 100
		and value % 1 == 0
end
```

## Error handling with `pcall`

Use `pcall` around operations that can fail, such as data or web requests:

```lua
local success, result = pcall(function()
	return Datastore:GetDatastore("Profiles"):GetAsync("player-key")
end)

if not success then
	warn("Could not load data:", result)
end
```

## Complete example

```lua
local function createCheckpoint(
	name: string,
	position: Vector3,
	onReached: (Player) -> ()
): Instance
	local checkpoint = Instance.New("Part", world)
	checkpoint.Name = name
	checkpoint.Position = position
	checkpoint.Size = Vector3.New(6, 1, 6)
	checkpoint.Anchored = true
	checkpoint.Color = Color.FromRGB(0, 220, 120)
	checkpoint:AddTag("Checkpoint")

	checkpoint.Clicked:Connect(function(player)
		onReached(player)
	end)

	return checkpoint
end

createCheckpoint("Checkpoint1", Vector3.New(0, 1, 20), function(player)
	print(player.Name, "reached the checkpoint")
end)
```
