# Strings

Strings are an important component of scripting, as they are used to represent sequences of letters, numbers, and symbols.

### Declaring a String <a href="#declaring-a-string" id="declaring-a-string"></a>

The most common method of declaring strings is to put double quotes (`"`) around the characters. The following declaration will cause the variable `str` to contain the string `Hello world!`:

```lua
local str = "Hello world!"
```

### Combining Strings <a href="#combining-strings" id="combining-strings"></a>

Strings can be combined through a method called **concatenation**. The Lua concatenation syntax is two dots (`..`) between the strings, for instance:

```lua
local str = "Your high score is "
local highScore = 5200
 
local combinedString = str .. highScore
 
print(str)
print(combinedString)
```
