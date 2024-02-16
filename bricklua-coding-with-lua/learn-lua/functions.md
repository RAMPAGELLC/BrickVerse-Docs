# Functions

**Functions** are sets of instructions that can be used multiple times in a script. Once defined, a function can be executed through a command or triggered through an event.

### Defining Functions <a href="#defining-functions" id="defining-functions"></a>

A basic function declaration includes the `function` keyword followed by the **function name** and a pair of parentheses (`()`). Since the function’s body will be a block of code, it must be closed with the `end` keyword.

```lua
local function addNumbers()
 
end

-- To call function run addNumbers()
```

Between the `()` and `end` is where commands and other code make up the function **body**. These commands will be executed when the function is called:

```lua
local function addNumbers()
	-- Function body
	print("Function called!")
end
```
