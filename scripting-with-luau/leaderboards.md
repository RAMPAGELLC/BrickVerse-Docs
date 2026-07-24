# Leaderboards

BrickVerse leaderboard statistics use `Stat` Instances and the global `Stats` service.

A Stat stores a value per Player and can be displayed by the platform.

## Create a Stat

```lua
local scoreStat = Instance.New("Stat", Stats)
scoreStat.Name = "Score"
scoreStat.DisplayName = "Score"
```

Create additional stats:

```lua
local winsStat = Instance.New("Stat", Stats)
winsStat.Name = "Wins"
winsStat.DisplayName = "Wins"
```

## Set a value

```lua
scoreStat:Set(player, 100)
winsStat:Set(player, 3)
```

Stats can also contain strings:

```lua
local rankStat = Instance.New("Stat", Stats)
rankStat.Name = "Rank"
rankStat.DisplayName = "Rank"

rankStat:Set(player, "Bronze")
```

## Read a value

```lua
local score = scoreStat:Get(player)
print(score)
```

Get the formatted display value:

```lua
print(scoreStat:GetDisplayValue(player))
```

## Observe changes

A Player exposes `StatChanged`:

```lua
player.StatChanged:Connect(function(stat, value)
	print(stat.Name, "changed to", value)
end)
```

## Initialize players

```lua
local function setupPlayer(player: Player)
	scoreStat:Set(player, 0)
	winsStat:Set(player, 0)
end

for _, player in ipairs(Players:GetPlayers()) do
	setupPlayer(player)
end

Players.PlayerAdded:Connect(setupPlayer)
```

## Add score

```lua
local function addScore(player: Player, amount: number)
	if amount <= 0 then
		return
	end

	local current = scoreStat:Get(player) or 0
	scoreStat:Set(player, current + amount)
end
```

Call only from server-validated gameplay:

```lua
addScore(player, 10)
```

## Team totals

```lua
local total = scoreStat:GetTotalForTeam(player.Team)
print("Team score:", total)
```

Check that the Player has a Team before using it.

## List configured Stats

```lua
for _, stat in ipairs(Stats:GetStats()) do
	print(stat.Name, stat:GetDisplayName())
end
```

## Persistent stats

Stats are runtime values. Save persistent progression with Datastores.

```lua
type Profile = {
	wins: number,
	bestScore: number,
}

local profiles: { [Player]: Profile } = {}
```

When a player loads:

```lua
local function applyProfile(player: Player, profile: Profile)
	winsStat:Set(player, profile.wins)
	scoreStat:Set(player, 0)
end
```

When a round ends:

```lua
local function finishRound(player: Player, roundScore: number)
	local profile = profiles[player]

	if not profile then
		return
	end

	if roundScore > profile.bestScore then
		profile.bestScore = roundScore
	end

	scoreStat:Set(player, roundScore)
end
```

## Rank labels

```lua
local function getRank(wins: number): string
	if wins >= 100 then
		return "Diamond"
	elseif wins >= 50 then
		return "Gold"
	elseif wins >= 20 then
		return "Silver"
	else
		return "Bronze"
	end
end

local function updateRank(player: Player)
	local wins = winsStat:Get(player) or 0
	rankStat:Set(player, getRank(wins))
end
```

## Do not trust client scores

Unsafe:

```lua
-- Client sends "I earned 5000 points."
```

Safe:

```lua
-- Client requests an action.
-- Server validates the action.
-- Server calculates the score.
-- Server updates the Stat.
```

## Round leaderboard

```lua
local roundScores: { [Player]: number } = {}

local function setRoundScore(player: Player, value: number)
	value = math.max(0, math.floor(value))
	roundScores[player] = value
	scoreStat:Set(player, value)
end

local function addRoundScore(player: Player, amount: number)
	setRoundScore(
		player,
		(roundScores[player] or 0) + amount
	)
end

local function getRanking()
	local entries = {}

	for player, score in pairs(roundScores) do
		table.insert(entries, {
			player = player,
			score = score,
		})
	end

	table.sort(entries, function(a, b)
		return a.score > b.score
	end)

	return entries
end
```

Display the results:

```lua
for place, entry in ipairs(getRanking()) do
	print(place, entry.player.Name, entry.score)
end
```

## Cleanup

```lua
Players.PlayerRemoved:Connect(function(player)
	roundScores[player] = nil
end)
```

## Complete score system

```lua
local scoreStat = Instance.New("Stat", Stats)
scoreStat.Name = "Score"
scoreStat.DisplayName = "Score"

local winsStat = Instance.New("Stat", Stats)
winsStat.Name = "Wins"
winsStat.DisplayName = "Wins"

local roundScores: { [Player]: number } = {}

local function setup(player: Player)
	roundScores[player] = 0
	scoreStat:Set(player, 0)
	winsStat:Set(player, 0)
end

local function award(player: Player, amount: number)
	if amount <= 0 then
		return
	end

	local nextScore = (roundScores[player] or 0) + amount
	roundScores[player] = nextScore
	scoreStat:Set(player, nextScore)
end

for _, player in ipairs(Players:GetPlayers()) do
	setup(player)
end

Players.PlayerAdded:Connect(setup)

Players.PlayerRemoved:Connect(function(player)
	roundScores[player] = nil
end)
```
