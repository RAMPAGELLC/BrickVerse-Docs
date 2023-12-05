# Empowering Responsible Gameplay: A Guide to ModerationService in BrickVerse

## Introduction

Welcome to BrickVerse, the dynamic social platform that empowers teens to unleash their creativity and craft captivating gaming experiences. In this developer article, we'll delve into the robust ModerationService provided by BrickVerse, a powerful tool designed to maintain a safe and enjoyable environment for all players. ModerationService allows game creators to enforce rules and regulations seamlessly, ensuring responsible gameplay and fostering a positive gaming community.

### ModerationService Overview

ModerationService is an integral part of BrickVerse, offering developers a comprehensive set of tools to moderate in-game players effectively. This service enables the enforcement of rules and policies by targeting players through their **Hardware ID (HWID), IP address, and UserId**. With features such as kicks, temporary bans, and permanent bans, ModerationService empowers game creators to maintain a healthy and secure gaming environment.

For privacy reasons we will not display HWID, IP addresses, etc. to game developers or players. This is strictly automated internally.

#### Basic Usage

Integrating ModerationService into your scripts is straightforward, thanks to the user-friendly design of BrickVerse's API. Here are some basic examples of how you can utilize ModerationService:

```lua
luaCopy code-- Temporary ban ArkInfinity for 10 hours with a reason
game.ModerationService:TemporaryBanAsync(game.Universe.Players.ArkInfinity, "Reason", 10)

-- Permanently ban ArkInfinity with a reason
game.ModerationService:BanAsync(game.Universe.Players.ArkInfinity, "Reason")

-- Kick ArkInfinity from the server with a reason
game.ModerationService:KickAsync(game.Universe.Players.ArkInfinity, "Reason")
```

These simple calls demonstrate the versatility of ModerationService, allowing you to take appropriate actions against players who violate the rules of your game.

#### Key Features

1. **HWID, IP, and UserId Moderation Link:** ModerationService provides the flexibility to moderate players based on various identifiers, ensuring a targeted approach to rule enforcement.
2. **Temporary and Permanent Actions:** Whether it's a temporary ban for a specified duration or a permanent ban, ModerationService offers the flexibility needed to address different levels of rule violations.
3. **Reasoning:** Adding a reason when applying moderation actions enhances transparency and communication. Players will understand why a particular action was taken, promoting a sense of fairness.

### Best Practices for ModerationService

1. **Clear Rules:** Clearly define and communicate the rules of your game to players. This helps in justifying moderation actions and encourages responsible gameplay.
2. **Consistent Enforcement:** Apply moderation actions consistently to maintain fairness and trust within the gaming community.
3. **Periodic Review:** Regularly review and update your moderation policies to adapt to evolving community dynamics and ensure the continued effectiveness of your rules.
