# Introduction

BrickVerse.co has an official NPMJS Module written in TypeScript by BrickVerse.co, you can use the module by running `npm install brickverse` and requiring it. `require('brickverse');`

## Example

```javascript
const { Client } = requre("brickverse");
let bot = new Client();

bot.login(process.env.BRICKVERSE_SECURITY_TOKEN, false).then(async() => {
    await bot.SendFriendRequest(1);
    
    bot.quit(); // terminates session. this will invalidate your BRICKVERSE SECURITY TOKEN!
})
```

## GitHub

{% embed url="https://github.com/BrickVerse-co/BrickVerse-NPM-Module" %}

## NPM

(got unpublished, on waitlist of 24 hours)

```powershell
npm i brickverse
```

{% embed url="https://www.npmjs.com/package/brickverse" %}

## Yarn

```powershell
yarn add brickverse
```



{% hint style="danger" %}
If you fork it from GitHub, you must credit BrickVerse.co and do not claim it as official. Please note we do regularly make maintenance to our API which requires updates to the module.\
\
BrickVerse.co terms apply. https://www.brickverse.co/legal/terms
{% endhint %}
