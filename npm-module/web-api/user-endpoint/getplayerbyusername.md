# GetPlayerByUsername

## bot.GetPlayerByUsername(username: string)

Request player data by username.

## Example

```javascript
const { Client } = requre("brickverse");
let bot = new Client();

bot.login("example", true).then(async() => {
    let {success, data} = await bot.GetPlayerByUsername("BrickVerse");
    
    if (success) {
        console.log(data);
    } else {
        console.log("API call failed, reason: " . data);
    }
});
```

## Returned Data

```json
{
    "status": "success",
    "username": "ArkInfinity",
    "id": 3,
    "cubes": 500,
    "plan": "LEVEL_3",
    "rank": "Manager",
    "avatar_body": "generatedurl.png",
    "avatar_head": "generatedurl.png"
}
```

More information at [https://developers.brickverse.co/api/user/v1-user-avatar-1](https://developers.brickverse.co/api/user/v1-user-avatar-1)

## Parameters

| Name     | Type   | Description |
| -------- | ------ | ----------- |
| username | string | Player name |
