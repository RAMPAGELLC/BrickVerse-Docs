# Style Your Code

## Principles

* The purpose of a style guide is to avoid arguments.
  * There's no one right answer to how to format code, but consistency is important, so we agree to accept this one, somewhat arbitrary standard so we can spend more time writing code and less time arguing about formatting details in the review.
* Optimize code for reading, not writing.
  * You will write your code once. Many people will need to read it, from the reviewers, to any one else that touches the code, to you when you come back to it in six months.
  * All else being equal, consider what the diffs might look like. It's much easier to read a diff that doesn't involve moving things between lines. Clean diffs make it easier to get your code reviewed.
* Avoid magic, such as surprising or dangerous Lua features:
  * Magical code is really nice to use, until something goes wrong. Then no one knows why it broke or how to fix it.
  * _Metatables_ are a good example of a powerful feature that should be used with care.
* Be consistent with idiomatic Lua when appropriate.

## Requires

* All `require` calls should be at the top of a file, making dependencies static.
*   Use relative paths when importing modules from the same package.

    ```
    local OtherThing = require(script.Parent.OtherThing)
    ```
*   Use absolute paths when importing modules from a different package.

    ```
    local CorePackages = game:GetService("CorePackages")
    local Roact = require(CorePackages.Roact)
    ```



    **Metatables**

    Metatables are an incredibly powerful Lua feature that can be used to overload operators, implement prototypical inheritance, and tinker with limited object lifecycle.

    At BrickVerse, we limit use of metatables to a couple cases:

    * Implementing prototype-based classes
    * Guarding against typos

    **Prototype-based classes**

    The most popular pattern for classes in Lua is sometimes referred to as the One True Pattern. It defines class members, instance members, and metamethods in the same table and highlights Lua's strengths well.

    First up, we create a regular, empty table:

    ```
    local MyClass = {}
    ```

    Next, we assign the `__index` member on the class back to itself. This is a handy trick that lets us use the class's table as the metatable for instances as well.

    When we construct an instance, we'll tell Lua to use our `__index` value to find values that are missing in our instances. It's sort of like `prototype` in JavaScript, if you're familiar.

    ```
    MyClass.__index = MyClass
    ```

    In most cases, we create a default constructor for our class. By convention, we usually call it `new`.

    Methods that don't operate on instances of our class are usually defined using a dot (`.`) instead of a colon (`:`).

    ```
    function MyClass.new()
        local self = {
            -- Define members of the instance here, even if they're `nil` by default.
            phrase = "bark",
        }

        -- Tell Lua to fall back to looking in MyClass.__index for missing fields.
        setmetatable(self, MyClass)

        return self
    end
    ```

    We can also define methods that operate on instances. These are just methods that expect their first argument to be an instance. By convention, we define them using a colon (`:`):

    ```
    -- This is functionally identical to `function MyClass.bark(self)`
    function MyClass:bark()
        print("My phrase is", self.phrase)
    end
    ```

    At this point, our class is ready to use!

    We can construct instances and start tinkering with it:

    ```
    local instance = MyClass.new()

    -- Properties on the instance are visible, since it's just a table:
    print(instance.phrase) -- "bark"

    -- Methods are pulled from MyClass because of our metatable:
    instance:bark() -- "My phrase is bark"

    -- We can also invoke methods with a dot by explicitly passing `instance`:
    MyClass.bark(instance)
    instance.bark(instance)
    ```

    Further additions you can make to your class as needed:

    * Introduce a `__tostring` metamethod to make debugging easier
    * Define quasi-private members using two underscores as a prefix
    *   Add a method to check type given an instance, like:

        ```
        function MyClass.isMyClass(instance)
            return getmetatable(instance).__index == MyClass
        end
        ```

    **Guarding against typos**

    Indexing into a table in Lua gives you `nil` if the key isn't present, which can cause errors that are difficult to trace!

    Our other major use case for metatables is to prevent certain forms of this problem. For types that act like enums, we can carefully apply an `__index` metamethod that throws:

    ```
    local MyEnum = {
        A = "A",
        B = "B",
        C = "C",
    }

    setmetatable(MyEnum, {
        __index = function(self, key)
            error(string.format("%q is not a valid member of MyEnum",
                tostring(key)), 2)
        end,
    })
    ```

    Since `__index` is only called when a key is missing in the table, `MyEnum.A` and `MyEnum.B` will still give you back the expected values, but `MyEnum.FROB` will throw, hopefully helping engineers track down bugs more easily.

    **General Punctuation**

    * Don't use semicolons `;`. They are generally only useful to separate multiple statements on a single line, but you shouldn't be putting multiple statements on a single line anyway.

    **General Whitespace**

    * **Indent with tabs**.
    * Keep lines under 120 columns wide, assuming four column wide tabs.
      * Luacheck will warn for lines over 120 _bytes_ wide; it isn't accurate with tab characters!
    * Wrap comments to 80 columns wide, assuming four column wide tabs.
      * This is different than normal code; the hope is that short lines help improve readability of comment prose, but is too restrictive for code.
    * Don't leave whitespace at the end of lines.
      * If your editor has an auto-trimming function, turn it on!
    * Add a newline at the end of the file.
    *   No vertical alignment!

        * Vertical alignment makes code more difficult to edit and often gets messed up by subsequent editors.

        Good:

        ```
        local frobulator = 132
        local grog = 17
        ```

        Bad:

        ```
        local frobulator = 132
        local grog       =  17
        ```
    *   Use a **single** empty line to express groups when useful. Do not start blocks with a blank line. Excess empty lines harm whole-file readability.

        ```
        local Foo = require(Common.Foo)

        local function gargle()
            -- gargle gargle
        end

        Foo.frobulate()
        Foo.frobulate()

        Foo.munge()
        ```
    *   Use one statement per line. Put function bodies on new lines.

        Good:

        ```
        table.sort(stuff, function(a, b)
            local sum = a + b
            return math.abs(sum) > 2
        end)
        ```

        Bad:

        ```
        table.sort(stuff, function(a, b) local sum = a + b return math.abs(sum) > 2 end)
        ```

        This is especially true for functions that return multiple values. Compare these two statements:

        ```
        Rodux.Store.new(function(state) return state end, mockState, nil)
        Rodux.Store.new(function(state) return state, mockState end, nil)
        ```

        It's much easier to spot the mistake (and much harder to make in the first place) if the function isn't on one line.

        ```
        Rodux.Store.new(function(state)
            return state
        end, mockState, nil)
        Rodux.Store.new(function(state)
            return state, mockState
        end, nil)
        ```

        This is also true for `if` blocks, even if their body is just a `return` statement.

        Good:

        ```
        if valueIsInvalid then
            return
        end
        ```

        Bad:

        ```
        if valueIsInvalid then return end
        ```

        Most of the time this pattern is used, it's because we're performing validation of an input or condition. It's much easier to add logging, or expand the conditional, when the statement is broken across multiple lines. It will also diff better in code review.
    *   Put a space before and after operators, except when clarifying precedence.

        Good:

        ```
        print(5 + 5 * 6^2)
        ```

        Bad:

        ```
        print(5+5* 6 ^2)
        ```
    *   Put a space after each commas in tables and function calls.

        Good:

        ```
        local friends = {"bob", "amy", "joe"}
        foo(5, 6, 7)
        ```

        Bad:

        ```
        local friends = {"bob","amy" ,"joe"}
        foo(5,6 ,7)
        ```
    *   When creating blocks, inline any opening syntax elements.

        Good:

        ```
        local foo = {
            bar = 2,
        }

        if foo then
            -- do something
        end
        ```

        Bad:

        ```
        local foo =
        {
            bar = 2,
        }

        if foo
        then
            -- do something
        end
        ```
    *   Avoid putting curly braces for tables on their own line. Doing so harms readability, since it forces the reader to move to another line in an awkward spot in the statement.

        Good:

        ```
        local foo = {
            bar = {
                baz = "baz",
            },
        }

        frob({
            x = 1,
        })
        ```

        Bad:

        ```
        local foo =
        {
            bar =

            {
                baz = "baz",
            },
        }

        frob(
        {
            x = 1,
        })
        ```

        Exception:

        ```
        -- In function calls with large inline tables or functions, sometimes it's
        -- more clear to put braces and functions on new lines:
        foo(
            {
                type = "foo",
            },
            function(something)
                print("Hello," something)
            end
        )

        -- As opposed to:
        foo({
            type = "foo",
        }, function(something) -- How do we indent this line?
            print("Hello,", something)
        end)
        ```

    **Newlines in Long Expressions**[**¶**](https://roblox.github.io/lua-style-guide/#newlines-in-long-expressions)

    * First, try and break up the expression so that no one part is long enough to need newlines. This isn't always the right answer, as keeping an expression together is sometimes more readable than trying to parse how several small expressions relate, but it's worth pausing to consider which case you're in.
    * It is often worth breaking up tables and arrays with more than two or three keys, or with nested sub-tables, even if it doesn't exceed the line length limit. Shorter, simpler tables can stay on one line though.
    * Prefer adding the extra trailing comma to the elements within a multiline table or array. This makes it easier to add new items or rearrange existing items.
    *   Break dictionary-like tables with more than a couple keys onto multiple lines.

        Good:

        ```
        local foo = { type = "foo" }

        local bar = {
            type = "bar",
            phrase = "hooray",
        }

        -- It's also okay to use multiple lines for a single field
        local baz = {
            type = "baz",
        }
        ```

        Bad:

        ```
        local stuff = { hello = "world", hola = "mundo", howdy = "y'all", sup = "homies" }
        ```
    *   Break list-like tables onto multiple lines however it makes sense.

        * Make sure to follow the line length limit!

        ```
        local libs = { "roact", "rodux", "testez", "cryo", "otter" }

        -- You can break these onto multiple lines, which makes diffs cleaner:
        local libs = {
            "roact",
            "rodux",
            "testez",
            "cryo",
            "otter",
        }

        -- We can also group them, if grouping has useful information:
        local libs = {
            "roact", "rodux", "cryo",

            "testez", "otter",
        }
        ```
    * For long argument lists or longer, nested tables, prefer to expand all the subtables. This makes for the cleanest diffs as further changes are made.

    ```
        local aTable = {
            {
                aLongKey = aLongValue,
                anotherLongKey = anotherLongValue,
            },
            {
                aLongKey = anotherLongValue,
                anotherLongKey = aLongValue,
            },
        }

        doSomething(
            {
                aLongKey = aLongValue,
                anotherLongKey = anotherLongValue,
            },
            {
                aLongKey = anotherLongValue,
                anotherLongKey = aLongValue,
            }
        )
    ```

    In some situations where we only ever expect table literals, the following is acceptable, though there's a chance automated tooling could change this later. In particular, this comes up a lot in Roact code (`doSomething` being `Roact.createElement`).

    ```
        local aTable = {{
            aLongKey = aLongValue,
            anotherLongKey = anotherLongValue,
        }, {
            aLongKey = anotherLongValue,
            anotherLongKey = aLongValue,
        }}

        doSomething({
            aLongKey = aLongValue,
            anotherLongKey = anotherLongValue,
        }, {
            aLongKey = anotherLongValue,
            anotherLongKey = aLongValue,
        })
    ```

    However, this case is less acceptable if there are any non-tables added to the mix. In this case, you should use the style above.

    ```
        doSomething({
            aLongKey = aLongValue,
            anotherLongKey = anotherLongValue
        }, notATableLiteral, {
            aLongKey = anotherLongValue,
            anotherLongKey = aLongValue
        })
    ```

    ```
        doSomething(
            {
                aLongKey = aLongValue,
                anotherLongKey = anotherLongValue
            },
            notATableLiteral,
            {
                aLongKey = anotherLongValue,
                anotherLongKey = aLongValue
            }
        )
    ```

    * For long expressions try and add newlines between logical subunits. If you're adding up lots of terms, place each term on its own line. If you have parenthesized subexpressions, put each subexpression on a newline.
      * Place the operator at the beginning of the new line. This makes it clearer at a glance that this is a continuation of the previous line.
      * If you have to need to add newlines within a parenthesized subexpression, reconsider if you can't use temporary variables. If you still can't, add a new level of indentation for the parts of the statement inside the open parentheses much like you would with nested tables.
      * Don't put extra parentheses around the whole expression. This is necessary in Python, but Lua doesn't need anything special to indicate multiline expressions.
    *   For long conditions in `if` statements, put the condition in its own indented section and place the `then` on its own line to separate the condition from the body of the `if` block. Break up the condition as any other long expression.

        Good:

        ```
        if
            someReallyLongCondition
            and someOtherReallyLongCondition
            and somethingElse
        then
            doSomething()
            doSomethingElse()
        end
        ```

        Bad:

        ```
        if someReallyLongCondition and someOtherReallyLongCondition
            and somethingElse then
            doSomething()
            doSomethingElse()
        end

        if someReallyLongCondition and someOtherReallyLongCondition
                and somethingElse then
            doSomething()
            doSomethingElse()
        end

        if someReallyLongCondition and someOtherReallyLongCondition
            and somethingElse then
                doSomething()
                doSomethingElse()
        end
        ```

    **Blocks**[**¶**](https://roblox.github.io/lua-style-guide/#blocks)

    *   Don't use parentheses around the conditions in `if`, `while`, or `repeat` blocks. They aren't necessary in Lua!

        ```
        if CONDITION then
        end

        while CONDITION do
        end

        repeat
        until CONDITION
        ```
    *   Use `do` blocks if limiting the scope of a variable is useful.

        ```
        local getId
        do
            local lastId = 0
            getId = function()
                lastId = lastId + 1
                return lastId
            end
        end
        ```

    **Literals**

    *   Use double quotes when declaring string literals.

        * Using single quotes means we have to escape apostrophes, which are often useful in English words.
        * Empty strings are easier to identify with double quotes, because in some fonts two single quotes might look like a single double quote (`""` vs `''`)

        Good:

        ```
        print("Here's a message!")
        ```

        Bad:

        ```
        print('Here\'s a message!')
        ```

        * Single quotes are acceptable if the string contains double quotes to reduce escape sequences.

        Exception:

        ```
        print('Quoth the raven, "Nevermore"')
        ```

        * If the string contains both single and double quotes, prefer double quotes on the outside, but use your best judgement.

    **Tables**

    * Avoid tables with both list-like and dictionary-like keys.
      * Iterating over these _mixed_ tables is troublesome.
    * Iterate over list-like tables with `ipairs` and dictionary-like tables with `pairs`.
      * This helps clarify what kind of table we're expecting in a given block of code!
    *   Add trailing commas in **multi-line** tables.

        * This lets us re-sort lines with a single keypress and makes diffs cleaner when adding new items.

        ```
        local frobs = {
            andrew = true,
            billy = true,
            caroline = true,
        }
        ```

    **Functions**

    * Keep the number of arguments to a given function small, preferably 1 or 2.
    *   Always use parentheses when calling a function. Lua allows you to skip them in many cases, but the results are typically much harder to parse.

        Good:

        ```
        local x = doSomething("home")
        local y = doSomethingElse({u = 1, v = 2})
        ```

        Bad:

        ```
        local x = doSomething "home"
        local y = doSomethingElse{u = 1, v = 2}
        ```

        Of particular note, the last example - using the curly braces as if they were function call syntax - is common in other Lua codebases, but while it's more readable than other ways of using this feature, for consistency we don't use it in our codebase.
    *   Declare named functions using function-prefix syntax. Non-member functions should always be local.

        Good:

        ```
        local function add(a, b)
            return a + b
        end
        ```

        Bad:

        ```
        -- This is a global!
        function add(a, b)
            return a + b
        end

        local add = function(a, b)
            return a + b
        end
        ```

        Exception:

        ```
        -- An exception can be made for late-initializing functions in conditionals:
        local doSomething

        if CONDITION then
            function doSomething()
                -- Version of doSomething with CONDITION enabled
            end
        else
            function doSomething()
                -- Version of doSomething with CONDITION disabled
            end
        end
        ```
    *   When declaring a function inside a table, use function-prefix syntax. Differentiate between `.` and `:` to denote intended calling convention.

        Good:

        ```
        -- This function should be called as Frobulator.new()
        function Frobulator.new()
            return {}
        end

        -- This function should be called as Frobulator:frob()
        function Frobulator:frob()
            print("Frobbing", self)
        end
        ```

        Bad:

        ```
        function Frobulator.garb(self)
            print("Frobbing", self)
        end

        Frobulator.jarp = function()
            return {}
        end
        ```

    **Comments**

    * Wrap comments to 80 columns wide.
      * It's easier to read comments with shorter lines, but fitting code into 80 columns can be challenging.
    *   Use single line comments for inline notes:

        * If the comment spans multiple lines, use multiple single-line comments.
        * Sublime Text has an automatic wrap feature (alt+Q on Windows) to help with this!

        ```
        -- This condition is really important because the world would blow up if it
        -- were missing.
        if not foo then
            stopWorldFromBlowingUp()
        end
        ```
    *   Use block comments for documenting items:

        * Use a block comment at the top of files to describe their purpose.
        * Use a block comment before functions or objects to describe their intent.

        ```
        --[[
            Shuts off the cosmic moon ray immediately.

            Should only be called within 15 minutes of midnight Mountain Standard
            Time, or the cosmic moon ray may be damaged.
        ]]
        local function stopCosmicMoonRay()
        end
        ```
    *   Comments should focus on _why_ code is written a certain way instead of _what_ the code is doing.

        Good:

        ```
        -- Without this condition, the aircraft hangar would fill up with water.
        if waterLevelTooHigh() then
            drainHangar()
        end
        ```

        Bad:

        ```
        -- Check if the water level is too high.
        if waterLevelTooHigh() then
            -- Drain the hangar
            drainHangar()
        end
        ```
    *   No section comments.

        Comments that only exist to break up a large file are a code smell; you probably need to find some way to make your file smaller instead of working around that problem with section comments. Comments that only exist to demark already obvious groupings of code (e.g. `--- VARIABLES ---`) and overly stylized comments can actually make the code harder to read, not easier. Additionally, when writing section headers, you (and anyone else editing the file later) have to be thorough to avoid confusing the reader with questions of where sections end.

        Some examples of ways of breaking up files:

        * Move inner classes and static functions into their own files, which aren't included in the public API. This also makes testing those classes and functions easier.
        * Check if there are any existing libraries that can simplify your code. If you're writing something and think that you could make part of this into a library, there's a good chance someone already has.

        If you can't break the file up, and still feel like you need section headings, consider these alternatives.

        *   If you want to put a section header on a group of functions, put that information in a block comment attached to the first function in that section. You should still make sure the comment is about the function its attached to, but it can also include information about the section as a whole. Try and write the comment in a way that makes it clear what's included in the section.

            ```
            --[[
                All of the readX functions return the next token from the string
                passed in to the Reader or returns nil if the next token doesn't
                match the type the function is trying to read.

                local test = "123 ABC"
                i = reader:readInt()
                print(i, ",", test.remaining) -- 123 , ABC

                readInt reads an integer, positive or negative.
            ]]
            function Reader:readInt() -- ...

            -- readFloat reads a floating point number, but does not accept
            -- scientific notation
            function Reader:readFloat() -- ...
            ```
        * The same can be done for a group of variables in some cases. All the same caveats apply though, and you have to consider whether one block comment or a normal comment on each variable (or even using just whitespace to separate groups) would be more readable.
        * General organization of your code can aid readibility while making logical sections more obvious as well. Module level variables and functions can appear in any order, so you can sometimes put a group of variables above a group of functions to make a section.

    **Naming**

    * Spell out words fully! Abbreviations generally make code easier to write, but harder to read.
    * Use `PascalCase` names for class and enum-like objects.
    * Use `PascalCase` for all BrickVerse APIs. `camelCase` APIs are mostly deprecated, but still work for now.
    * Use `camelCase` names for local variables, member values, and functions.
    * For acronyms within names, don't capitalize the whole thing. For example, `aJsonVariable` or `MakeHttpCall`.
    * The exception to this is when the abbreviation represents a set. For example, in `anRGBValue` or `GetXYZ`. In these cases, `RGB` should be treated as an abbreviation of `RedGreenBlue` and not as an acronym.
    * Use `LOUD_SNAKE_CASE` names for local consants.
    * Prefix private members with an underscore, like `_camelCase`.
      * Lua does not have visibility rules, but using a character like an underscore helps make private access stand out.
    * A File's name should match the name of the object it exports.
      * If your module exports a single function named `doSomething`, the file should be named `doSomething.lua`.

    `FooThing.lua`:

    ```
    local FOO_THRESHOLD = 6

    local FooThing = {}

    FooThing.someMemberConstant = 5

    function FooThing.go()
        print("Foo Delta:", FooThing.someMemberConstant - FOO_THRESHOLD)
    end

    return FooThing
    ```

    **Yielding**

    Do not call yielding functions on the main task. Wrap them in `coroutine.wrap` or `delay`, and consider exposing a Promise or Promise-like async interface for your own functions.

    **Pros:**

    * BrickVerse's yielding model makes calling asynchronous tasks transparent to the user, which lets users call complicated functions without understanding coroutines or other async primitives.

    **Cons:**

    *   Unintended yielding can cause hard-to-track data races. Simple code involving callbacks can cause confusing bugs if the input callback yields.

        ```
        local value = 0

        local function doSomething(callback)
            local newValue = value + 1
            callback(newValue)
            value = newValue
        end
        ```

    **Error Handling**

    When writing functions that can fail, return `success, result`, use a `Result` type, or use an async primitive that encodes failure, like `Promise`.

    Do not throw errors except when validating correct usage of a function.

    ```
    local function thisCanFail(someValue)
        assert(typeof(someValue) == "string", "someValue must be a string!")

        if success() then
            return true, "Congratulations! You won!"
        else
            return false, Error.new("ERR_BLAH", "Something horrible failed!")
        end
    end
    ```

    **Pros:**

    * Using exceptions lets unhandled errors bubble up 'automatically' to your caller
    * Stack traces are automatically attached to errors

    **Cons:**

    * Lua can only throw strings as errors, which makes distinguishing between them very difficult
    * Exceptions are not encoded into a function's contract explicitly. By returning `success, result`, you force your caller to consider whether an error will happen.

    **Exceptions:**

    * When calling functions that communicate failure by throwing, wrap calls in `pcall` and make it clear via comment what kinds of errors you're expecting to handle.

    **General BrickVerse Best Pratices**

    * All services should be referenced using `game:GetService` at the top of the file.
    * When importing a module, use the name of the module for its variable name.



Gotchas\
[https://www.luafaq.org/gotchas.html](https://www.luafaq.org/gotchas.html)
--------------------------------------------------------------------------

Article by _**Roblox Corportation & Lua Org**_
