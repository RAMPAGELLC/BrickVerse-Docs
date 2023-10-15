# Tables

A **table** is a Lua data type that can store multiple values including [numbers](numbers.md), [booleans](boolean.md), [strings](strings.md), [functions](functions.md), and more. Tables are constructed with curly braces (`{}`) as shown here:

```lua
-- Construct an empty table assigned to variable "t"
local t = {}
print(t)
```

Once constructed, a table can behave as either an **array** or a **dictionary** as illustrated in the following sections.

### Arrays <a href="#arrays" id="arrays"></a>

An array is a simple list of ordered values, useful for storing collections of data such as a group of players with special permissions.

#### Creating Arrays <a href="#creating-arrays" id="creating-arrays"></a>

To create an array using a Lua table, simply store the values sequentially, separated by commas. An array value can be any non-`nil` type (boolean, number, string, function, userdata, or even another table).

```lua
-- Construct an array with three items
local testArray = {"A string", 3.14159, workspace.Part}
```

#### Reading From Arrays <a href="#reading-from-arrays" id="reading-from-arrays"></a>

To read from an array, add a pair of brackets after its reference and specify the index number of the element inside (`[pos]`):

{% hint style="danger" %}
Unlike some languages, Lua uses **1-based indexing** for arrays, meaning that the first item in the array is `[1]`, not `[0]`.
{% endhint %}

```lua
-- Construct an array with three items
local testArray = {"A string", 3.14159, workspace.Part}
 
print(testArray[1])
print(testArray[2])
print(testArray[3])l
```

#### Writing Into Arrays <a href="#writing-into-arrays" id="writing-into-arrays"></a>

The value of an array index can be defined or rewritten by indicating the index number in brackets (`[pos]`) followed by `=` and then the value:

```lua
local testArray = {"A string", 3.14159, workspace.Part}
 
testArray[2] = 12345
testArray[4] = "New string"
 
print(testArray[2])
print(testArray[4])
```

#### Iterating Over Arrays <a href="#iterating-over-arrays" id="iterating-over-arrays"></a>

Arrays can be iterated over (looped through) in two ways:

* Use the built-in `ipairs()` function in a `for` loop.
* Get the array’s length using the `#` operator and loop from **1** to that length value.

```lua
local testArray = {"A string", 3.14159, workspace.Part, "New string"}
 
-- Loop using "ipairs()"
for index, value in ipairs(testArray) do
	print(index, value)
end
 
-- Iterate using the array length operator (#)
for index = 1, #testArray do
	print(index, testArray[index])
end
```

#### Inserting Items <a href="#inserting-items" id="inserting-items"></a>

An item can be inserted at the **end** of an array through either of these methods:

* Pass the array reference and the item value to Lua’s `table.insert()` function.
* Add the new item to the array using the `t[#t+1]` syntax.

```lua
local testArray = {"A string", 3.14159}
 
table.insert(testArray, "New string")
testArray[#testArray+1] = "Another new string"
 
print(testArray[3])
print(testArray[4])
```
