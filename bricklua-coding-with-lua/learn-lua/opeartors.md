# Opeartors

An **operator** is a special set of symbols used to perform an operation or conditional evaluation.

### Logical <a href="#logical" id="logical"></a>

The logical operators for [conditional statements](conditional-structures.md) are `and`, `or`, and `not`. These operators consider both `false` and `nil` as “false” and anything else as “true.”

| Operator | Description                                          |
| -------- | ---------------------------------------------------- |
| `and`    | Evaluates as `true` only if both conditions are true |
| `or`     | Evaluates as `true` if either condition is true      |
| `not`    | Evaluates as the opposite of the condition           |

### Relational <a href="#relational" id="relational"></a>

Relational operators compare two parameters and return a [boolean](https://developer.roblox.com/en-us/articles/Boolean) `true` or `false`.

| Operator | Description              | Associated metamethod |
| -------- | ------------------------ | --------------------- |
| `==`     | Equal to                 | `__eq`                |
| `~=`     | Not equal to             |                       |
| `>`      | Greater than             |                       |
| `<`      | Less than                | `__lt`                |
| `>=`     | Greater than or equal to |                       |
| `<=`     | Less than or equal to    | `__le`                |

### Arithmetic <a href="#arithmetic" id="arithmetic"></a>

Lua supports the usual binary operators along with exponentiation, modulus, and unary negation.

| Operator | Description    | Example     | Associated metamethod |
| -------- | -------------- | ----------- | --------------------- |
| `+`      | Addition       | 1 + 1 = 2   | `__add`               |
| `-`      | Subtraction    | 1 - 1 = 0   | `__sub`               |
| `*`      | Multiplication | 5 \* 5 = 25 | `__mul`               |
| `/`      | Division       | 10 / 5 = 2  | `__div`               |
| `^`      | Exponentiation | 2 ^ 4 = 16  | `__pow`               |
| `%`      | Modulus        | 13 % 7 = 6  | `__mod`               |
| `-`      | Unary negation | -2 = 0 - 2  | `__unm`               |

### Miscellaneous <a href="#miscellaneous" id="miscellaneous"></a>

Miscellaneous operators include **concatenation** and **length**.

| Operator | Description                  | Associated metamethod |
| -------- | ---------------------------- | --------------------- |
| `..`     | Concatenates two strings     | `__concat`            |
| `#`      | Length of [table](tables.md) | `__len`               |

### Compound Assignment <a href="#compound-assignment" id="compound-assignment"></a>

Compound assignment operators are used to set a variable equal to the result of an operation where the first parameter is the variable’s current value.

{% hint style="info" %}
The expression on the left side of a compound assignment is only evaluated once. For example, if an expression generates a random index in a table, the same index is used for both the operation and the assignment.
{% endhint %}

| Operator | Operation      |
| -------- | -------------- |
| `+=`     | Addition       |
| `-=`     | Subtraction    |
| `*=`     | Multiplication |
| `/=`     | Division       |
| `%=`     | Modulus        |
| `^=`     | Exponentiation |
| `..=`    | Concatenation  |
