---
description: This is useful for managing players in your universe
---

# Players

## Properties

| Name        | Type    | Description                                                                                   | Authority |
| ----------- | ------- | --------------------------------------------------------------------------------------------- | --------- |
| LocalPlayer | Player  | When called from a client script, returns the local player. Will not work for Server Scripts. | Core      |
| Name        | Void    | Returns Player Name                                                                           | Core      |
| Admin       | Boolean | Returns whether or not the player is BrickVerse Staff                                         | Core      |
| Host        | Boolean | Returns whether or not the player is the World Creator                                        | Core      |
| BVID        | Int     | Returns UserID Of player on BrickVerse                                                        | Core      |

Inherited from [Dynamic](https://docs.brickverse.co/bricklua-lua-references-manual/dymanic) Set

## Functions

| Name                         | Type   | Property | Description                                            |
| ---------------------------- | ------ | -------- | ------------------------------------------------------ |
| GetPlayerByUsername          | Player | Players  | Returns player with the username from BrickVerse.co DB |
| GetPlayerByUserId            | Player | Players  | Returns player with the userid from BrickVerse.co DB   |
| GetPlayers                   | Table  | Players  | Returns all connected players                          |
| Kick                         | Void   | Player   | Disconnect a player from the world                     |
| GetPlayerCharacterByUserId   | Model  | Players  | Returns character with the userid in workplace         |
| GetPlayerCharacterByUsername | Model  | Players  | Returns character with the username in workplace       |
| GetPlayerCharacterByNetID    | Model  | Players  | Returns character with the netid in workplace          |
| MutePlayer                   | Void   | Player   | Blocks player from speaking in chat & voicechat.       |
| MuteChat                     | Void   | Player   | Blocks player from speaking in chat                    |
| MuteVoice                    | Void   | Player   | Blocks player from speaking in voice chat              |
| Respawn                      | Void   | Player   | Respawns the player                                    |
| NETID                        | Void   | Player   | Returns ID of the server id of the player              |
| PlayerCount                  | Int    | Players  | Return player count                                    |
| MaxPlayers                   | Int    | Players  | Returns max players                                    |

## Events

| Name            | Description                                                           |
| --------------- | --------------------------------------------------------------------- |
| PlayerConnected | Invoked when a player connected successfully to the world             |
| PlayerRemoved   | Invoked when a player disconnected successfully to the world          |
| OnShutDown      | Invoked when server is shutdown by BrickVerse staff or world creator. |

