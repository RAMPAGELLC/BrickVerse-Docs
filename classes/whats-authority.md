# What's Authority?

Authority is script authority which limits your world from performing certain actions such as editing and/or reading data.

| Authority Name | Level | About                     |
| -------------- | ----- | ------------------------- |
| Backend        | 5     | Authority over everything |
| Core           | 4     | BrickVerse Core Scripts   |
| Plugin         | 3     | Studio Plugins            |
| Server         | 2     | Server Scripts            |
| Client         | 1     | Client Scripts            |

What is modulescripts classified under? Well if a module is called on the server, it will be assigned authority level 2, and obvious if it was called on client it will be given authority level 1.\
\
Level 4 authority ("Core") has some extra security where data can be read, however cannot be modified unless allowed by Level 4. Level 4 is used for core scripts with security not needed.

Level 5 authority ("Backend") has authority to grant authority levels, it's data cannot be read or modified by Level 4 and under. Level 5 is typically used for our backend apis.\
\
Level 2+ cannot be read or modified by client as it's impossible.
