# Empowering Game Creators: A Deep Dive into ENVService with Lua API in BrickVerse

## Introduction

Welcome to BrickVerse, the dynamic and innovative social platform that empowers teens to unleash their creativity and craft captivating gaming experiences. In this developer article, we'll explore the powerful ENVService and its seamless integration with the BrickLua API, revolutionizing the way budding game creators connect, collaborate, and share imaginative worlds on our platform.

### ENVService Overview

The ENVService in BrickVerse provides a secure and efficient method for handling variables, including tokens, passwords, and other sensitive data within your scripts. This service plays a crucial role in maintaining a secure environment for your creations while fostering collaboration and creativity.

#### Basic Usage with Lua API

Utilizing ENVService in your scripts is straightforward with the Lua API. The two primary functions are `game.env.get("variable")` and `game.env.set("variable", any..value)`. These functions allow you to read and modify environment variables seamlessly.

```lua
luaCopy code-- Reading a variable
local myVariable = game.env.get("variable")

-- Setting a variable
game.env.set("variable", "new_value")
```

These functions facilitate the interaction with environment variables, ensuring a smooth and secure scripting experience.

#### Security Features

One of the standout features of `game.env` is its robust security measures. It shields itself from crash dumps, exposure, analytics, and more. Providing a reliable and secure environment for your game scripts. By using `game.env`, you significantly reduce the risk of unauthorized access to sensitive information.

By default with BrickVerse game bundles sent to clients (players) when they connect is all your assets bundled up in a BrickVerse asset delivery package. Server scripts are not sent to the client. All scripts are compiled upon request.

### Permissions Management

In BrickVerse, managing permissions for ENV variables is a critical aspect of ensuring data security. The ENV panel on our website allows you to create variables with specific permissions, controlling access on both the client and server sides.

* **Read Permission:** Script can read the variable's value.
* **Write Permission:** Script can modify a existing variable's value. Exercise caution, as this is a powerful permission. **Its highly recommended to not give clients this permission.**
* **Create Permission:** Script can create a new variable. Exercise caution, as this is a powerful permission. **Its highly recommended to not give clients this permission.**

It's essential to note that granting write permission to clients is potentially risky, as any client can abuse it. Therefore, it's recommended to limit such permissions to trusted entities.

### BrickVerse.gg Website Integration

All ENV variable management takes place on the BrickVerse.gg website, providing a user-friendly interface to create, edit, and manage your variables. Here are some key points to keep in mind:

* **Maximum Variables:** Each universe, including worlds (which inherit from their parent universe), supports a maximum of 25 ENV variables.
* **Variable Types:** Variables can be booleans, strings, or arrays.
* **Character Limits:** There's a maximum length of 500 characters for the variable value and 50 characters for the variable key.

### Conclusion

In conclusion, ENVService with Lua API integration in BrickVerse offers a secure, user-friendly, and powerful solution for managing environment variables in your game scripts. By following best practices and leveraging the flexibility of permissions, you can create immersive and secure gaming experiences while fostering a vibrant community of young innovators on our platform. Dive into the world of BrickVerse, where your creativity knows no bounds!
