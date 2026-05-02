# Creating Your First Guild Bot

BrickVerse bots use a modern command router system — no `!commands`, no manual parsing.

This guide shows how to build a real bot using the official SDK.

***

### What You’ll Build

A bot that supports:

* `/ping` → replies “pong”
* `/echo` → repeats input
* Buttons, select menus, and modals

***

### Install the SDK

```bash
npm install @metagames/channel-bot-sdk
```

***

### Create Your Bot File

Create:

```
bot.ts
```

***

### Full Working Example

```ts
import {
  ChannelBotClient,
  CommandRouter,
  DEFAULT_ROUTER_SUBSCRIBED_EVENTS,
} from "@metagames/channel-bot-sdk";

const client = new ChannelBotClient({
  token: process.env.BOT_TOKEN!,
  apiBaseUrl: "https://api.brickverse.gg",
  subscribedEvents: DEFAULT_ROUTER_SUBSCRIBED_EVENTS,
});

const router = new CommandRouter()

  // Slash command: /ping
  .command("ping", async (ctx) => {
    await ctx.replyMention("pong");
  })

  // Slash command: /echo <text>
  .command("echo", async (ctx) => {
    await ctx.reply(ctx.args.join(" ") || "Nothing to echo.");
  })

  // Button interaction
  .button("verify", async (ctx) => {
    await ctx.replyEphemeral("Verification flow started.");
  })

  // Select menu interaction
  .selectMenu("role-picker", async (ctx) => {
    await ctx.reply(
      `You selected: ${ctx.selectedValues.join(", ") || "none"}`
    );
  })

  // Modal interaction
  .modal("support-form", async (ctx) => {
    await ctx.replyEphemeral(
      `Received form fields: ${Object.keys(ctx.modalValues).join(", ")}`
    );
  });

client.useCommandRouter(router);

// Fired when bot is ready
client.on("guildBot.ready", (event) => {
  console.log(`Logged in as ${event.bot.username}`);
});

// Start bot
await client.connect();
```

***

### Running Your Bot

Set your token:

```bash
BOT_TOKEN=your_bot_token_here
```

Run:

```bash
npx ts-node bot.ts
```

***

### Using Your Bot

Once running, use slash commands in a guild:

```
/ping
→ pong

/echo hello world
→ hello world
```

***

### How Commands Work

You define commands using:

```ts
router.command("name", handler)
```

The SDK automatically:

* Parses slash commands
* Routes interactions
* Handles responses
* Manages context

***

### Context (`ctx`) Helpers

Inside handlers:

```ts
ctx.reply("message")            // public reply
ctx.replyMention("message")     // mentions user
ctx.replyEphemeral("message")   // private reply

ctx.args                        // command arguments
ctx.selectedValues              // select menu values
ctx.modalValues                 // modal input values
```

***

### Interaction Types

BrickVerse bots support more than commands:

#### Buttons

```ts
.button("verify", async (ctx) => {
  await ctx.replyEphemeral("Clicked!");
});
```

#### Select Menus

```ts
.selectMenu("role-picker", async (ctx) => {
  await ctx.reply(ctx.selectedValues.join(", "));
});
```

#### Modals

```ts
.modal("support-form", async (ctx) => {
  await ctx.replyEphemeral("Form submitted.");
});
```

***

### Token Safety

Never expose your token:

❌ Bad

```ts
token: "abc123"
```

✅ Good

```ts
token: process.env.BOT_TOKEN!
```

***

### SDK & API

SDK: [https://github.com/BrickVerse-co/channel-bot-sdk](https://github.com/BrickVerse-co/channel-bot-sdk)

NPM: [https://www.npmjs.com/package/@metagames/channel-bot-sdk](https://www.npmjs.com/package/@metagames/channel-bot-sdk)

API Docs: [https://api.brickverse.gg/swagger](https://api.brickverse.gg/swagger)

***

### Next Steps

You can now build:

* Moderation bots
* Verification systems
* Game integrations
* Role pickers
* Ticket/support systems

***

### Pro Tip

Keep your router modular:

```ts
const router = new CommandRouter()
  .command("ping", pingCommand)
  .command("echo", echoCommand);
```

Split commands into separate files as your bot grows.



