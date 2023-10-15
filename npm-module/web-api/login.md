# login

Once you inited a new client you must login into your BrickVerse bot account, simply use Client Object.login(brickverse token)

## Example

```javascript
const { Client } = requre("brickverse");
let bot = new Client();

bot.login(process.env.BRICKVERSE_SECURITY_TOKEN, false).then(async() => {
    await bot.SendFriendRequest(1);
});
```

## Parameters

| Name  | Type    | Description                                              |
| ----- | ------- | -------------------------------------------------------- |
| token | string  | BrickVerse Security Token or Bot Token for bot accounts. |
| isbot | boolean | If bot or player account.                                |

