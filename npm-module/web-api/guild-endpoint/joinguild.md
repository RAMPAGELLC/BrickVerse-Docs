# JoinGuild

## bot.JoinGuild(guildId: number)

Join requested guild

## Example

```javascript
const { Client } = requre("brickverse");
let bot = new Client();

bot.login(process.env.BRICKVERSE_SECURITY_TOKEN, false).then(async() => {
    let success = await bot.JoinGuild(1);
    
    if (success) {
        console.log("Joined guild!");
    } else {
        console.log("API call failed");
    }
});
```

## Parameters

| Name    | Type   | Description |
| ------- | ------ | ----------- |
| guildId | number | Guild id    |
