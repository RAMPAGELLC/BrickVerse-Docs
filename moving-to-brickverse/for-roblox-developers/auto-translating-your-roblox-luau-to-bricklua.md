# Auto-translating your Roblox Luau to BrickLua

## Translating Roblox Luau to BrickLua

`RBLXLuau2BrickLua` helps migrate Roblox Luau scripts to BrickLua, the scripting language used by BrickVerse.

The translator attempts to replace known Roblox classes, services, properties, methods, constructors, and scripting patterns with their closest BrickVerse equivalents.

{% hint style="danger" %}
Translation does not guarantee that a script will work without changes. Roblox and BrickVerse use different Game APIs, object models, networking systems, physics behavior, and client/server architecture.
{% endhint %}

### What the translator does

The translator can assist with common changes such as:

* replacing known Roblox service names;
* converting Instance creation syntax;
* translating common hierarchy references;
* replacing supported class names;
* mapping known methods and properties;
* converting supported value constructors;
* identifying unsupported APIs;
* and producing warnings for code that needs manual review.

It is intended to reduce repetitive migration work, not automatically port an entire game.

### Requirements

Install:

* a supported Python or Node.js runtime, depending on the repository version;
* [RBLXLuau2BrickLua](https://github.com/BrickVerse-co/RBLXLuau2BrickLua);
* Git, when installing from source;
* and access to the current BrickVerse Game API documentation.

The World converter may also call this translator automatically when converting scripts inside a Roblox place.

### Back up your scripts

Before translation:

1. Keep the original Roblox scripts unchanged.
2. Copy the scripts into a separate migration directory.
3. Commit the original source to version control.
4. Write translated scripts to a different output directory.

Recommended structure:

```
migration/
├── roblox-source/
│   ├── Server/
│   ├── Client/
│   └── Shared/
├── bricklua-output/
└── reports/
```

Do not overwrite the only copy of your Roblox source.

### Translate one script first

Begin with a small script that uses only a few Roblox APIs.

Example Roblox script:

```lua
local Players = game:GetService("Players")

local platform = Instance.new("Part")
platform.Name = "Platform"
platform.Anchored = true
platform.Size = Vector3.new(10, 1, 10)
platform.Parent = workspace

Players.PlayerAdded:Connect(function(player)
	print(player.Name .. " joined")
end)
```

A translated result may resemble:

```lua
local Players = game:GetService("Players")

local platform = Instance.New("Part")
platform.Name = "Platform"
platform.Anchored = true
platform.Size = Vector3.New(10, 1, 10)
platform.Parent = Scene

Players.PlayerAdded:Connect(function(player)
	print(player.Name .. " joined")
end)
```

The exact output depends on the translator version and current BrickVerse API mappings.

### Install the translator

Clone the repository:

```bash
git clone https://github.com/BrickVerse-co/RBLXLuau2BrickLua.git
cd RBLXLuau2BrickLua
```

Follow the runtime and dependency instructions in the repository.

For a Python version, installation may use:

```bash
python -m pip install -r requirements.txt
```

For a Node.js version, installation may use:

```bash
npm install
```

{% hint style="info" %}
Use only the installation command supported by the repository version you downloaded.
{% endhint %}

### Run the translator

The general translation flow requires:

* an input script or source directory;
* an output file or directory;
* and optional mapping or API-update settings.

Generic command structure:

```bash
<translator-command> <input> <output>
```

Single file example:

```bash
<translator-command> "./roblox-source/RoundManager.luau" "./bricklua-output/RoundManager.luau"
```

Directory example:

```bash
<translator-command> "./roblox-source" "./bricklua-output"
```

Replace `<translator-command>` with the command documented by the repository.

### Translate scripts during World conversion

`RBLX2BRICKWORLD` can use the translator while converting a Roblox place.

The workflow is:

```
Roblox Script
      ↓
RBLX2BRICKWORLD extracts Source
      ↓
RBLXLuau2BrickLua translates known APIs
      ↓
BrickLua script is added to the converted World
      ↓
Developer reviews and tests the result
```

When script conversion is disabled, the World converter may skip scripts or preserve their source only as migration data.

### Review translator warnings

A good translation report should distinguish between:

| Result      | Meaning                                                        |
| ----------- | -------------------------------------------------------------- |
| Converted   | A known mapping was applied.                                   |
| Unchanged   | The syntax is valid in both languages or no change was needed. |
| Warning     | A possible mapping was found but requires review.              |
| Unsupported | No safe BrickVerse equivalent is known.                        |
| Error       | The input could not be parsed or translated.                   |

Review every warning and unsupported item.

{% hint style="danger" %}
Do not remove translator warnings simply to make the output look complete. A warning often identifies behavior that cannot be migrated safely through text replacement.
{% endhint %}

### Common automatic conversions

#### Instance creation

Roblox:

```lua
local part = Instance.new("Part")
```

BrickLua:

```lua
local part = Instance.New("Part")
```

#### Vector constructors

Roblox:

```lua
local position = Vector3.new(0, 5, 0)
```

BrickLua:

```lua
local position = Vector3.New(0, 5, 0)
```

#### Workspace

Roblox:

```lua
part.Parent = workspace
```

BrickLua:

```lua
part.Parent = Scene
```

#### Finding children

Roblox:

```lua
local door = workspace:FindFirstChild("Door")
```

A BrickLua equivalent may use the corresponding BrickVerse hierarchy method:

```lua
local door = Scene:FindChild("Door")
```

Always confirm the exact method against the current Game API.

### APIs that commonly require manual work

### CFrame

Roblox frequently uses `CFrame` for combined position and rotation:

```lua
part.CFrame = CFrame.new(0, 5, 0) * CFrame.Angles(0, math.rad(90), 0)
```

BrickVerse may represent these values as separate properties:

```lua
part.Position = Vector3.New(0, 5, 0)
part.Rotation = Vector3.New(0, 90, 0)
```

Complex object-space and world-space CFrame calculations need manual conversion.

### RemoteEvents and RemoteFunctions

Roblox:

```lua
PurchaseEvent:FireServer(itemId)
```

BrickVerse networking uses its own network classes and message format.

A migration normally requires:

1. creating the BrickVerse network object;
2. constructing a supported message;
3. invoking the server;
4. receiving the server event;
5. validating the sender;
6. and returning a result to the client.

Do not translate networking through a simple method rename unless the APIs are known to be equivalent.

### TweenService

Roblox:

```lua
local tween = TweenService:Create(part, info, {
	Transparency = 1,
})

tween:Play()
```

BrickVerse animation or tween behavior may use a different service or require a manual interpolation loop.

The translator should flag this for review.

### DataStoreService

Roblox:

```lua
local store = DataStoreService:GetDataStore("Profiles")
local data = store:GetAsync(key)
```

BrickVerse persistence may use its datastore service with different naming, limits, value handling, and server requirements.

Review:

* datastore service name;
* method capitalization;
* supported values;
* error handling;
* request limits;
* and server-only access.

### CollectionService

Roblox tags may be convertible to BrickVerse Instance tags.

Roblox:

```lua
CollectionService:AddTag(part, "Collectible")
```

Possible BrickLua equivalent:

```lua
part:AddTag("Collectible")
```

Queries may also need to be rewritten to use BrickVerse hierarchy tag methods.

### User interfaces

Roblox UI uses classes and values such as:

* `ScreenGui`;
* `Frame`;
* `TextLabel`;
* `TextButton`;
* `UDim`;
* `UDim2`;
* anchors;
* and Roblox-specific layout behavior.

BrickVerse UI uses its own UI classes and relative/offset properties. UI conversion normally requires more than renaming classes.

### Character code

Roblox character scripts often expect:

```lua
player.Character
character:FindFirstChildOfClass("Humanoid")
character.HumanoidRootPart
```

BrickVerse player and character classes may expose health, movement, position, tools, and respawning differently.

Review all character and Humanoid logic manually.

### Services

Search translated scripts for Roblox service references:

```lua
game:GetService("ReplicatedStorage")
game:GetService("ServerStorage")
game:GetService("ServerScriptService")
game:GetService("StarterGui")
game:GetService("TweenService")
game:GetService("CollectionService")
game:GetService("DataStoreService")
game:GetService("PathfindingService")
game:GetService("MarketplaceService")
```

Each service must be mapped to a BrickVerse service, hierarchy location, or replacement architecture.

### Server and client scripts

Preserve the intended execution side:

| Roblox location or type | BrickVerse target                         |
| ----------------------- | ----------------------------------------- |
| Server `Script`         | `ServerScript`                            |
| `LocalScript`           | `ClientScript`                            |
| `ModuleScript`          | `ModuleScript`                            |
| Replicated module       | Shared client/server-accessible hierarchy |
| Server-only module      | Server-only hierarchy                     |

{% hint style="danger" %}
Moving server validation into a shared or client script creates a security vulnerability. The translator cannot determine whether gameplay logic is secure merely by converting its syntax.
{% endhint %}

### Validate networking

For every client-to-server request, verify:

1. The sender is identified by the server.
2. All message fields have the expected type.
3. Numbers are finite and clamped.
4. Referenced Instances belong to the expected World hierarchy.
5. The player owns or can use the requested object.
6. Distance and game-state requirements are checked.
7. A server-controlled cooldown is enforced.
8. Rewards and prices are calculated by the server.

Roblox client validation code must not be treated as trusted after migration.

### Check remaining Roblox identifiers

Search the translated output for:

```
workspace
Workspace
CFrame
UDim
UDim2
Enum.
RemoteEvent
RemoteFunction
FireServer
FireClient
FireAllClients
InvokeServer
InvokeClient
ReplicatedStorage
ServerStorage
ServerScriptService
StarterPlayer
StarterGui
TweenService
CollectionService
DataStoreService
MarketplaceService
PathfindingService
HumanoidRootPart
```

Some may appear in comments or compatibility code, but each result should be inspected.

### Compare against the BrickVerse Game API

The translator should use the latest available BrickVerse API mappings, but the Game API may change after the translator is released.

Before publishing:

1. Open the BrickVerse Game API reference.
2. Search for every converted service and class.
3. Confirm method names and parameter order.
4. Confirm whether a method is asynchronous.
5. Confirm client/server restrictions.
6. Replace obsolete mappings.

Do not assume a successful text conversion means the API call is valid.

### Test translated scripts

#### Syntax test

Check that the script loads without a parser or compiler error.

#### Startup test

Check initialization, service lookup, and hierarchy references.

#### Behavior test

Test the exact gameplay feature the script controls.

#### Multiplayer test

Test with multiple clients and an authoritative server.

#### Failure test

Test missing data, invalid requests, disconnected players, unavailable web APIs, and datastore failures.

#### Security test

Attempt to send invalid or repeated client requests.

### Example migration review

Original Roblox code:

```lua
PurchaseRemote.OnServerEvent:Connect(function(player, itemId, price)
	local profile = Profiles[player]

	if profile.Coins >= price then
		profile.Coins -= price
		grantItem(player, itemId)
	end
end)
```

This code is unsafe because the client can choose `price`.

A safer BrickLua design keeps prices on the server:

```lua
local ITEMS = {
	sword = {
		price = 250,
	},
}

PurchaseEvent.InvokedServer:Connect(function(player, message)
	local itemId = message:GetString("itemId")
	local item = ITEMS[itemId]

	if not item then
		return
	end

	local profile = Profiles[player]

	if not profile then
		return
	end

	if profile.Coins < item.price then
		return
	end

	profile.Coins -= item.price
	grantItem(player, itemId)
end)
```

The translator may help replace APIs, but the developer must fix insecure architecture.

### Recommended migration workflow

1. Translate a single small script.
2. Review its report.
3. Fix unsupported APIs.
4. Test it in BrickVerse Creator.
5. Update custom mappings when appropriate.
6. Translate one subsystem at a time.
7. Test server and client behavior together.
8. Translate the complete project only after the smaller tests work.

Suggested subsystem order:

```
1. Utility modules
2. Shared configuration
3. Simple map scripts
4. User interface
5. Player systems
6. Networking
7. Inventory and economy
8. Persistent data
9. NPCs and combat
10. External web integrations
```

### Troubleshooting

#### The translator made no changes

The script may use standard Luau syntax without known Roblox APIs, or the mapping database may not contain the APIs used by the script.

#### The output contains warnings

Read each warning and compare the original behavior with the current BrickVerse Game API.

#### The output does not compile

Check:

* unmatched syntax introduced during translation;
* unsupported Luau syntax;
* renamed classes;
* type annotations;
* and incomplete API replacements.

#### A service cannot be found

The Roblox service may not exist in BrickVerse or may use a different service or hierarchy.

#### The script compiles but does not work

Compilation checks syntax, not gameplay equivalence. Inspect events, hierarchy paths, networking, execution side, physics, and property semantics.

#### The translated script is insecure

Move authoritative state to the server and validate every client request. Translation cannot automatically prove that a gameplay system is secure.

### Limitations

Automatic translation cannot safely guarantee compatibility for:

* networking;
* CFrame math;
* advanced physics;
* TweenService;
* UI layout;
* DataStore architecture;
* pathfinding;
* Roblox marketplace systems;
* Roblox avatar assumptions;
* engine-specific assets;
* and custom modules that depend heavily on Roblox behavior.

Treat translated code as a starting point for a manual port.

### Related tools

* [RBLXLuau2BrickLua](https://github.com/BrickVerse-co/RBLXLuau2BrickLua)
* [RBLX2BRICKWORLD](https://github.com/BrickVerse-co/RBLX2BRICKWORLD)
* [BrickVerse Game API](https://developers.brickverse.gg/game-api/api)
