# HTTP Requests

The global `Http` service sends supported web requests from BrickLua.

Use HTTP for trusted integrations such as:

- game-owned APIs;
- server status reporting;
- moderation services;
- configuration systems;
- webhooks;
- and external game services.

{% hint style="danger" %}
Make privileged requests from a ServerScript. Never place secret API keys in client-visible scripts or Instances.
{% endhint %}

## GET request

```lua
local success, body = pcall(function()
	return Http:GetAsync("https://example.invalid/status")
end)

if success then
	print(body)
else
	warn("GET failed:", body)
end
```

## Request headers

```lua
local headers = {
	["Accept"] = "application/json",
	["X-Game-Server"] = world.ServerID,
}

local body = Http:GetAsync(
	"https://example.invalid/status",
	headers
)
```

## POST JSON

```lua
local payload = json.serialize({
	worldId = world.WorldID,
	serverId = world.ServerID,
	players = world.PlayersConnected,
})

local headers = {
	["Content-Type"] = "application/json",
	["Accept"] = "application/json",
}

local response = Http:PostAsync(
	"https://example.invalid/server-heartbeat",
	payload,
	headers
)
```

## Other convenience methods

```lua
Http:PutAsync(url, body, headers)
Http:PatchAsync(url, body, headers)
Http:DeleteAsync(url, body, headers)
```

Each asynchronous method returns the response body string.

## Detailed request

Use `HttpRequestData` when you need status codes or response headers:

```lua
local request = HttpRequestData.New()
request.URL = "https://example.invalid/items"
request.Method = HttpRequestMethod.Get
request.Headers = {
	["Accept"] = "application/json",
}

local response = Http:RequestAsync(request)

print(response.Success)
print(response.StatusCode)
print(response.Body)
```

## POST with RequestAsync

```lua
local request = HttpRequestData.New()
request.URL = "https://example.invalid/events"
request.Method = HttpRequestMethod.Post
request.Headers = {
	["Content-Type"] = "application/json",
}
request.Body = json.serialize({
	event = "round_started",
	serverId = world.ServerID,
})

local response = Http:RequestAsync(request)

if not response.Success then
	warn("Request failed with status", response.StatusCode)
	return
end

print(response.Body)
```

## Parse JSON responses

```lua
local response = Http:GetAsync(
	"https://example.invalid/config"
)

local success, data = pcall(function()
	return json.parse(response)
end)

if not success then
	warn("Invalid JSON response:", data)
	return
end

print(data.message)
```

Validate external values before using them.

## Buffers

The HTTP API also supports buffer responses:

```lua
local data = Http:GetBufferAsync(
	"https://example.invalid/binary"
)
```

Buffer variants exist for POST, PUT, DELETE, and PATCH.

## Callback methods

Non-Async convenience methods accept callbacks:

```lua
Http:Get(
	"https://example.invalid/status",
	function(body)
		print(body)
	end,
	{
		["Accept"] = "application/json",
	}
)
```

Use Async methods when sequential control flow is clearer. Use callbacks when appropriate for your architecture.

## Timeouts and failure handling

Treat every web request as fallible:

```lua
local function safeGet(url: string): string?
	local success, result = pcall(function()
		return Http:GetAsync(url)
	end)

	if not success then
		warn("HTTP GET failed:", result)
		return nil
	end

	return result
end
```

## Retries

Retry only safe operations and use backoff:

```lua
local function getWithRetry(url: string, attempts: number): string?
	for attempt = 1, attempts do
		local body = safeGet(url)

		if body then
			return body
		end

		if attempt < attempts then
			task.wait(attempt * 2)
		end
	end

	return nil
end
```

Do not blindly retry a purchase or reward POST because the remote server may have completed it before the connection failed. Use idempotency keys.

## Idempotency

```lua
local operationId =
	world.ServerID .. ":" .. tostring(os.time()) .. ":" .. player.UserID

local headers = {
	["Content-Type"] = "application/json",
	["Idempotency-Key"] = operationId,
}
```

The receiving API must support idempotency.

## Secret headers

Read secrets from a server-only Universe Config:

```lua
local apiKey = ConfigService:GetConfigAsync("GAME_API_KEY")

local headers = {
	["Authorization"] = "Bearer " .. apiKey,
	["Content-Type"] = "application/json",
}
```

Never print the secret or send it to a client.

## Rate limiting

Cache responses and avoid unnecessary requests:

```lua
local cachedConfig = nil
local cachedAt = 0
local CACHE_SECONDS = 60

local function getRemoteConfig()
	local now = os.clock()

	if cachedConfig and now - cachedAt < CACHE_SECONDS then
		return cachedConfig
	end

	local body = safeGet("https://example.invalid/config")

	if not body then
		return cachedConfig
	end

	local success, value = pcall(function()
		return json.parse(body)
	end)

	if not success then
		return cachedConfig
	end

	cachedConfig = value
	cachedAt = now
	return cachedConfig
end
```

## Complete heartbeat example

```lua
local ENDPOINT = "https://example.invalid/server-heartbeat"

local function sendHeartbeat()
	local request = HttpRequestData.New()
	request.URL = ENDPOINT
	request.Method = HttpRequestMethod.Post
	request.Headers = {
		["Content-Type"] = "application/json",
	}
	request.Body = json.serialize({
		universeId = world.UniverseID,
		worldId = world.WorldID,
		serverId = world.ServerID,
		playerCount = world.PlayersConnected,
		uptime = world.UpTime,
	})

	local success, response = pcall(function()
		return Http:RequestAsync(request)
	end)

	if not success then
		warn("Heartbeat request failed:", response)
		return
	end

	if not response.Success then
		warn("Heartbeat returned", response.StatusCode)
	end
end

task.spawn(function()
	while true do
		sendHeartbeat()
		task.wait(30)
	end
end)
```
