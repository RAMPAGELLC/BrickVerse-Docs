# Conditional Structures

Conditional structures allow scripts to perform actions when specific conditions are met. These conditions can be checked with the **relational operators** summarized here:

| Operator | Description              | Example                |
| -------- | ------------------------ | ---------------------- |
| `==`     | Equal to                 | `3 == 5`  →  **false** |
| `~=`     | Not equal to             | `3 ~= 5`  →  **true**  |
| `>`      | Greater than             | `3 > 5`  →  **false**  |
| `<`      | Less than                | `3 < 5`  →  **true**   |
| `>=`     | Greater than or equal to | `3 >= 5`  →  **false** |
| `<=`     | Less than or equal to    | `3 <= 5`  →  **true**  |

### Conditional Tests <a href="#conditional-tests" id="conditional-tests"></a>

#### if — then <a href="#if-then" id="if-then"></a>

The basic `if`—`then` statement executes a block of code if a specific condition is true. For instance:

{% code title="Example" %}
```lua
if 2 + 3 == 5 then
   print("Two plus three is five")
end
```
{% endcode %}

Note that Lua considers the “absence of true” as “false.” This means that both `false` and `nil` will evaluate as non-true:

```lua
local nilVariable  -- Variable is declared but has no value, so it's nil
local falseVariable = false  -- Variable is declared with value of false
 
if nilVariable ~= true then
	print(nilVariable)  -- Outputs "nil" since nil is not true
end
 
if falseVariable ~= true then
	print(falseVariable)  -- Outputs "false" since false is not true
end
```

#### elseif — then <a href="#elseif-then" id="elseif-then"></a>

Adding an `elseif`—`then` statement to an `if`—`then` structure lets you check if alternative conditions are true, assuming the preceding conditions are false. Lua will go from top to bottom, stop at the first true condition it encounters, and execute its block of code.

```lua
if 25 > 100 then
	print("25 is greater than 100")
elseif 25 > 50 then
	print("25 is greater than 50") 
elseif 25 > 10 then
	print("25 is greater than 10") 
end
```

#### else <a href="#else" id="else"></a>

Finishing a conditional structure with `else` lets you execute a block of code if none of its preceding conditions evaluate to true. In the following example, both `10 > 100` and `10 > 25` are false, so those blocks of code will **not** execute but the `else` block will.

```lua
if 10 > 100 then
	print("10 is greater than 100")
elseif 10 > 25 then
	print("10 is greater than 25")
else
	print("10 is less than both 25 and 100")
end
```

### Conditional Loops <a href="#conditional-loops" id="conditional-loops"></a>

Conditional loops let you execute specific code while a condition is true, or repeat code until a condition becomes true.

#### while — do <a href="#while-do" id="while-do"></a>

The `while`—`do` loop evaluates if a condition is true or false. If false, the loop ends and the code following it continues to execute. If true, the code between `do` and `end` executes and the true/false condition is reevaluated afterward.

```lua
local timeRemaining = 10
 
while timeRemaining > 0 do
	print("Seconds remaining: " .. timeRemaining)
	wait(1)
	timeRemaining = timeRemaining - 1	
end
 
print("Timer reached zero!")
```

#### repeat — until <a href="#repeat-until" id="repeat-until"></a>

A `repeat`—`until` loop repeats until a certain condition is met. Note that the code between `repeat` and `until` is executed at least once because the conditional test is performed **afterward**.

```lua
local currentGoblinCount = 18
 
-- Spawn goblins up to a maximum of 25 in the game
repeat
	spawnGoblin()
	currentGoblinCount = currentGoblinCount + 1
	print("Current goblin count: " .. currentGoblinCount)
until currentGoblinCount == 25
 
print("Goblins repopulated!")
```

### Using Logical Operators <a href="#using-logical-operators" id="using-logical-operators"></a>

#### Multi-Condition Tests <a href="#multi-condition-tests" id="multi-condition-tests"></a>

To avoid repetitive conditional tests in a sequence, use the logical operators `and` and `or` to perform multi-condition tests. For example, the following structure tests that **two** conditions are true:

```lua
local pasta = true
local tomatoSauce = true
 
if pasta == true and tomatoSauce == true then
	print("We have spaghetti dinner!")
else
	print("Something is missing...")
end
```

Logical operators can also be combined to perform more complex logical tests. For instance, the following code checks whether two conditions are true **or** a third condition is true:

```etlua
local pasta = false
local tomatoSauce = true
local garlicBread = true
 
if (pasta == true and tomatoSauce == true) or garlicBread == true then
	print("We have either spaghetti dinner OR garlic bread!")
else
	print("Something is missing...")
end
```

#### Non-Truth Tests <a href="#non-truth-tests" id="non-truth-tests"></a>

While the relational operators can be “flipped” to test for non-truth conditions, the logical operator `not` is useful for testing the “absence of true” (either `false` **or** `nil`).

```lua
local nilVariable  -- Variable is declared but has no value, so it's nil
local falseVariable = false  -- Variable is declared with value of false
 
if not nilVariable then
	print(nilVariable)  -- Outputs "nil" since nil is not true
end
 
if not falseVariable then
	print(falseVariable)  -- Outputs "false" since false is not true
end
```

The `not` operator can also test for the opposite of an entire multi-condition statement. For example, the following code confirms that there are not more than 25 goblins **nor** is the player’s experience level less than 5.

```lua
local currentGoblinCount = 18
local playerExperienceLevel = 6
 
if not (currentGoblinCount > 25 or playerLevel < 5) then
	print("Spawn more goblins!")
end
```
