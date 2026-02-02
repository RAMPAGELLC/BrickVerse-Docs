---
description: >-
  This API Reference Manual documents all of classes, enumerations, data types,
  services, event, callbacks, and properties developers use while creating there
  game universes.
---

# API

## BrickVerse Globals

### Functions

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><a href="./">function</a> , <a href="./">table</a> <strong>pairs</strong> ( <a href="./">table</a> t )</td></tr><tr><td><p>Returns an iterator function, the passed table <em>t</em> and nil, so that the construction will iterate over all key/value pairs of that table when used in a generic for-loop:</p><p></p><pre class="language-lua"><code class="lang-lua">local scores = { ["John"] = 5, ["Sally"] = 10 }

for name, score in pairs(scores) do   
   print(name .. " has score: " .. score) -- "John has score: 5" etc
end
</code></pre></td></tr></tbody></table>

| [bool](./) , [Variant](./) **pcall** ( [function](./) func, [Tuple](./) args )                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Calls the function _func_ with the given arguments in protected mode. This means that any error inside _func_ is not propagated; instead, pcall catches the error and returns a status code. Its first result is the status code (a boolean), which is true if the call succeeds without errors. In such case, pcall also returns all results from the call, after this first result. In case of any error, pcall returns false plus the error message. |

|                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [void](./) **print** ( [Tuple](./) params )                                                                                                                                                                                                                                                                                                 |
| Receives any number of arguments, and prints their values to the output. `print` is not intended for formatted output, but only as a quick way to show a value, typically for debugging. For a formatted output, use string.format. On BrickVerse, print does not call `tostring`, but will metatables for the the `__tostring` metamethod. |

| [Variant](./) **loadstring** ( [string](./) contents )                                                                   |
| ------------------------------------------------------------------------------------------------------------------------ |
| Loads Lua code from a string, and returns it as a function. This cannot load the binary version of Lua using loadstring. |

| [Variant](./) **require** ( [ModuleScript](./) module )                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Runs the supplied <a href="./"><code>ModuleScript</code></a> if it has not been run already, and returns what the ModuleScript returned (in both cases).</p><p>If the ModuleScript the user wants to use has been uploaded to BrickVerse (with the instance’s name being ‘MainModule’), it can be loaded by using the require function on the asset ID of the ModuleScript, though only on the server.</p> |

| [string](./) **typeof** ( [Variant](./) object )                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Returns the type of the object specified, as a string.<br>This function is more accurate than Lua’s native <em>type</em> function, as it does not denote BrickVerse-specific types as <em>userdata</em>.</p> |

| [number](./) , [number](./) **wait** ( [number](./) seconds = 0.03 )                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Yields the current thread until the specified amount of seconds have elapsed.<br>The delay will have a minimum duration of 29 milliseconds, but this minimum may be higher depending on the target framerate and various throttling conditions. If the <em>seconds</em> parameter is not specified, the minimum duration will be used.<br>This function returns:</p><ul><li>Actual time yielded (in seconds)</li><li>Total time since the software was initialized (in seconds)</li></ul> |

| [void](./) **warn** ( [Tuple](./) params )                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Behaves identically to Lua’s print function, except the output is styled as a warning, with yellow text and a timestamp.<br>This function accepts any number of arguments, and will attempt to convert them into strings which will then be joined together with spaces between them.</p> |

| [void](./) **delay** ( [number](./) delayTime, [function](./) callback )                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Schedules a function to be executed after _delayTime_ seconds have passed, without yielding the current thread. This function allows multiple Lua threads to be executed in parallel from the same stack. The delay will have a minimum duration of 29 milliseconds, but this minimum may be higher depending on the target framerate and various throttling conditions. If the _delayTime_ parameter is not specified, the minimum duration will be used. |

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><a href="./">string</a> <strong>tostring</strong> ( <a href="./">Variant</a> e )</td></tr><tr><td><p>Receives an argument of any type and converts it to a string in a reasonable format. For complete control of how numbers are converted, use string.format. If the metatable of <code>e</code> has a <code>__tostring</code> metamethod, then it will be called with <code>e</code> as the only argument and will return the result.</p><p></p><pre><code>local isBrickVerseCool = true
-- Convert the boolean to a string then concatenate:
print("BrickVerse is cool: " .. tostring(isBrickVerseCool)) --> BrickVerse is cool: true
</code></pre></td></tr></tbody></table>

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><a href="./">Variant</a> <strong>tonumber</strong> ( <a href="./">Variant</a> arg, <a href="./">int</a> base = 10 )</td></tr><tr><td><p>Attempts to convert the arg into a number with a specified base to interpret the value in. If it cannot be converted, this function returns nil.</p><p>The base may be any integer between 2 and 36, inclusive. In bases above 10, the letter ‘A’ (in either upper or lower case) represents 10, ‘B’ represents 11, and so forth, with ‘Z’ representing 35. In base 10 (the default), the number may have a decimal part, as well as an optional exponent part. In other bases, only unsigned integers are accepted.</p><p>If a string begins with “0x” and a base is not provided, the 0x is trimmed and the base is assumed to be 16, or hexadecimal.</p><p></p><pre><code>print(tonumber("1337")) --> 1337 (assumes base 10, decimal)
print(tonumber("1.25")) --> 1.25 (base 10 may have decimal portions)
print(tonumber("3e2")) --> 300 (base 10 may have exponent portion, 3 &#x26;times; 10 ^ 2)
print(tonumber("25", 8)) --> 21 (base 8, octal)
print(tonumber("0x100")) --> 256 (assumes base 16, hexadecimal)
print(tonumber("brickverse")) --> nil (does not raise an error)-- Tip: use with assert if you would like unconvertable numbers to raise an error
print(assert(tonumber("brickverse"))) --> Error: assertion failed
</code></pre></td></tr></tbody></table>

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td><a href="./">Variant</a> <strong>assert</strong> ( <a href="./">Variant</a> value, <a href="./">string</a> errorMessage = assertion failed! )</td></tr><tr><td><p>Throws an error if the provided <code>value</code> is <strong>false</strong> or <strong>nil</strong>. If the assertion passes, it returns all values passed to it.</p><p></p><pre><code>local product = 90 * 4
assert(product == 360, "Oh dear, multiplication is broken")-- The line above does nothing, because 90 times 4 is 360
</code></pre></td></tr></tbody></table>

| [Variant](./) **collectgarbage** ( [string](./) operation )                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Performs an operation on the Lua garbage collector based on the specified option.</p><p>BrickVerse's Lua sandbox only allows the <strong>“count”</strong> option to be used, so none of the other standard options are available.</p><p>The <strong>“count”</strong> option returns the total memory in use by Lua (in kilobytes).</p> |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [void](./) **error** ( [string](./) message, [int](./) level = 1 )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <p>Terminates the last protected function called and outputs <em>message</em> as an error message. If the function containing the error is not called in a protected function (pcall), then the script which called the function will terminate. The error function itself never returns and acts like a script error.</p><p>The <em>level</em> argument specifies how to get the error position. With level 1 (the default), the error position is where the error function was called. Level 2 points the error to where the function that called error was called; and so on. Passing a level 0 avoids the addition of error position information to the message.</p> |



### Variables

| [string](./) **\_VERSION**                                                                         |
| -------------------------------------------------------------------------------------------------- |
| A global variable (not a function) that holds a string containing the current interpreter version. |

| [DataModel](./) **game**                                                                               |
| ------------------------------------------------------------------------------------------------------ |
| A reference to the [`DataModel`](./), which is the root Instance of BrickVerse parent/child hierarchy. |

|                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------- |
| [DataModel](./) **Scene**                                                                                             |
| A reference to the [`DataModel`](./), which is the root Instance of BrickVerse streamed parts under [`Universe`](./). |

| [LuaSourceContainer](./) **script**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>A reference to the script object that is executing the code you are writing.<br>It can be either a <a href="/broken/pages/-MdQY07jDbhugILMsQHF"><code>ServerScript</code></a>, a <a href="/broken/pages/-MdQfQoqboY3Dn4qTQRS"><code>ClientScript</code></a>, or a <a href="https://developer.roblox.com/en-us/api-reference/class/ModuleScript"><code>ModuleScript</code></a> and sometimes a <a href="https://developer.roblox.com/en-us/api-reference/class/CoreScript"><code>CoreScript</code></a><code>.</code><br></p><p>This variable is not available when executing code from BrickVerse Studio’s command bar.</p> |

|                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [array](./) **shared**                                                                                                                                                                                                      |
|  table that is shared between all scripts of the same context level. Only shared across same authority level, for example it can't go across client -> server / server -> client. Only server -> server / client -> client. |

| [array](./) **\_G**                                                                     |
| --------------------------------------------------------------------------------------- |
| A table that is shared between all scripts of the same context level. Same as \_shared. |

|                                                                                       |
| ------------------------------------------------------------------------------------- |
| [Bool](./) **IsCoreScript**                                                           |
| Boolean variable if it's a corescript. Variable can be set, however it has no affect. |

## Lua Globals

{% content-ref url="math.md" %}
[math.md](math.md)
{% endcontent-ref %}
