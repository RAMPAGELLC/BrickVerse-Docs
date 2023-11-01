# GetAvatar

## bot.GetAvatar(userId: number)

Request URL to the player avatar, file type returned is a .png.

## Example

```javascript
const { Client } = requre("brickverse");
let bot = new Client();

bot.login(process.env.BRICKVERSE_SECURITY_TOKEN, false).then(async() => {
    let {success, avatar} = await bot.GetAvatar(1);
    
    if (success) {
        console.log(avatar);
    } else {
        console.log("API call failed, reason: " . avatar);
    }
});
```

## Parameters

| Name   | Type   | Description |
| ------ | ------ | ----------- |
| userId | number | Player id   |
