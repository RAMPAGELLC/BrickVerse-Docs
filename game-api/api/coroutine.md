# coroutine

A **coroutine** is used to perform multiple tasks at the same time from within the same script. Such tasks might include producing values from inputs or performing work on a subroutine when solving a larger problem. A task doesn’t even need to have a defined ending point, but it does need to define particular times at which it will **yield** (pause) to let other things be worked on.

### Using Coroutines <a href="#using-coroutines" id="using-coroutines"></a>

A new coroutine can be created by providing a function to `coroutine.create()`. Once created, a coroutine doesn’t begin running until the first call to `coroutine.resume()` which passes the arguments to the function. This call returns when the function either halts or calls `coroutine.yield()` and, when this happens, `coroutine.resume()` returns either the values returned by the function, the values sent to `coroutine.yield()`, or an error message. If it does error, the second return value will instead be the thrown error.

```lua
local function task(...)
	-- This function might do some work for a bit then yield some value
	coroutine.yield("first")  -- To be returned by coroutine.resume()
	-- The function continues once it is resumed again
	return "second"
end
 
local taskCoro = coroutine.create(task)
-- Call resume for the first time, which runs the function from the beginning
local success, result = coroutine.resume(taskCoro, ...)
print(success, result)  --> true, first (task called coroutine.yield())
-- Continue running the function until it yields or halts
success, result = coroutine.resume(taskCoro)
print(success, result)  --> true, second (task halted because it returned "second")
```

During the lifetime of the coroutine, you can call `coroutine.status()` to inspect its status:



| Status        | Meaning                                                                                                                            |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **suspended** | The coroutine is waiting to be resumed. Coroutines begin in this state and enter it when their function calls `coroutine.yield()`. |
| **running**   | The coroutine is running right now.                                                                                                |
| **normal**    | The coroutine is awaiting the yield of another coroutine; in other words, it has resumed another coroutine.                        |
| **dead**      | The function has halted (returned or thrown an error). The coroutine cannot be used further.                                       |



#### Wrapping Coroutines <a href="#wrapping-coroutines" id="wrapping-coroutines"></a>

When working with coroutines, you can also forgo the use of the coroutine object and instead use a wrapper function. Such a wrapper function will resume a particular coroutine when it is called and will return only the yielded values. You can do this using `coroutine.wrap()`:



```
-- Create coroutine and return a wrapper function that resumes itlocal f = coroutine.wrap(task)-- Resume the coroutine as if we called coroutine.resume()local result = f()-- If an error occurs it will be raised here!-- This differs from coroutine.resume() which acts similar to pcall()
```

The first value returned from `coroutine.resume()` describes whether a coroutine ran without errors. However, functions returned by `coroutine.wrap()` will not do this: instead they directly return the values returned or passed to `coroutine.yield()`, if any. Should an error have occurred while running the coroutine function, the error is raised on the call of the returned function.

#### Producer Pattern Example <a href="#producer-pattern-example" id="producer-pattern-example"></a>

Imagine a task that produces repetitions of a word: each time it produces a repetition, the next one will produce one more. For example, providing `Hello` will produce `Hello`, `HelloHello`, `HelloHelloHello`, etc. To do this, you can define `repeatThis()`:



```
-- This function repeats a word every time its coroutine is resumedlocal function repeatThis(word)	local repetition = ""	while true do		-- Do one repetition then yield the result		repetition = repetition .. word		coroutine.yield(repetition)	endend
```

To run this function as a coroutine, you can use `coroutine.create()` followed by multiple calls to `coroutine.resume()`:



```
local repetitionCoro = coroutine.create(repeatThis)print(coroutine.resume(repetitionCoro, "Hello"))  -- true, Helloprint(coroutine.resume(repetitionCoro))           -- true, HelloHelloprint(coroutine.resume(repetitionCoro))           -- true, HelloHelloHello
```

For this producer function, you can also use `coroutine.wrap()` to get a function that produces values:



```
local f = coroutine.wrap(repeatThis)print(f("Hello"))  -- Helloprint(f())         -- HelloHelloprint(f())         -- HelloHelloHello
```

### Coroutine Functions <a href="#coroutine-functions" id="coroutine-functions"></a>

| [thread](coroutine.md#using-coroutines) **coroutine.create** ( [function](coroutine.md#using-coroutines) f ) |
| ------------------------------------------------------------------------------------------------------------ |
| Creates a new coroutine, with body f. f must be a Lua function.                                              |

| [bool](coroutine.md#using-coroutines) , [Variant](coroutine.md#using-coroutines) **coroutine.resume** ( [thread](coroutine.md#using-coroutines) co, [Variant](coroutine.md#using-coroutines) val1, [Variant](coroutine.md#using-coroutines) ... )                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Starts or continues the execution of coroutine `co`. The first time you resume a coroutine, it starts running its body. The values val1, … are passed as the arguments to the body function. If the coroutine has yielded, resume restarts it; the values val1, … are passed as the results from the yield. If the coroutine runs without any errors, resume returns true plus any values passed to yield (if the coroutine yields) or any values returned by the body function (if the coroutine terminates). If there is any error, resume returns false plus the error message. |

| [thread](coroutine.md#using-coroutines) **coroutine.running** ( ) |
| ----------------------------------------------------------------- |
| Returns the running coroutine.                                    |

| [string](coroutine.md#using-coroutines) **coroutine.status** ( [thread](coroutine.md#using-coroutines) co )                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Returns the status of coroutine co, as a string: ‘running’, if the coroutine is running (that is, it called status); ‘suspended’, if the coroutine is suspended in a call to yield, or if it has not started running yet; ‘normal’ if the coroutine is active but not running (that is, it has resumed another coroutine); and ‘dead’ if the coroutine has finished its body function, or if it has stopped with an error. |

| [thread](coroutine.md#using-coroutines) **coroutine.wrap** ( [function](coroutine.md#using-coroutines) f )                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Creates a new coroutine, with body f. f must be a Lua function. Returns a function that resumes the coroutine each time it is called. Any arguments passed to the function behave as the extra arguments to resume. Returns the same values returned by resume, except the first boolean. In case of error, propagates the error. |

| [Tuple](coroutine.md#using-coroutines) **coroutine.yield** ( [Tuple](coroutine.md#using-coroutines) ... )      |
| -------------------------------------------------------------------------------------------------------------- |
| Suspends the execution of the calling coroutine. Any arguments to yield are passed as extra results to resume. |
