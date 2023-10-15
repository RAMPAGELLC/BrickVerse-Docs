# Numbers

A **number** in Lua is a double precision floating point number (or just **double**). For instance:

* 5
* 9.12761656
* \-1927

In Lua, numbers can range from -1.7 × 10308 to 1.7 × 10308 (around 15 digits, positive or negative).

### Signed and Unsigned <a href="#signed-and-unsigned" id="signed-and-unsigned"></a>

The sign of the number indicates whether it’s positive or negative. A signed number can be positive or negative, but an unsigned number cannot be negative. In Lua, `-0` is distinct from `0`.

### Notation <a href="#notation" id="notation"></a>

Numbers are notated with the most significant digits first (big-endian). There are multiple ways to notate number literals in Roblox Lua:

* [Decimal (base-10)](https://en.wikipedia.org/wiki/Decimal) — Write the digits of the number normally using digits 0–9 with a single optional decimal point, for example `7`, `1.25`, or `-22.5`.
* [Scientific notation](https://en.wikipedia.org/wiki/Scientific\_notation) — Write a decimal number followed by `e` or `e+`, then an integer to raise the decimal number to a power of 10. For instance, `12e3` is 12 × 10^3 (12,000).
* [Hexadecimal (base-16)](https://en.wikipedia.org/wiki/Hexadecimal) — Begin the number with `0x` followed by digits 0–9 or A–F (capitalization ignored). For example, `0xF` is 15 and `0x3FC` is 1020.
* [Binary (base-2)](https://en.wikipedia.org/wiki/Binary\_number) — Begin the number with `0b` followed by 0s or 1s, for instance `0b1100` (12 in decimal format).

{% hint style="info" %}
To aid in the readability of long numbers, underscores can be included anywhere within a number literal without changing the value, **except** at the beginning (in which case it would become an identifier). For example, `1_234_567` is the same as `1234567`, both of which are equal to 1,234,567.
{% endhint %}

### Operations <a href="#operations" id="operations"></a>

Lua math and relational [operators](https://developer.roblox.com/en-us/articles/Operators) can be used on numbers to manipulate and compare them. Mathematical functions such as `math.sqrt()` and `math.exp()` can be found in the [math](https://developer.roblox.com/en-us/api-reference/lua-docs/math) library and, for bitwise operations, the [bit32](bit32.md) library has been back-ported.

### Number Classifications <a href="#number-classifications" id="number-classifications"></a>

In Roblox Lua, there is no technical difference between the following types of numbers. However, number classifications are used in documentation to indicate which kind of number is involved with an API member.

#### int <a href="#int" id="int"></a>

The `int` number type refers to a number without a fractional portion (integer) like 0, 60, or -42. Properties and functions that expect integers may automatically round or raise errors when provided with non-integers.

When working with integers in Lua, note the following:

* The fractional portion of a number can be trimmed by rounding down with `math.floor()`.
* You can determine if a number is an integer by comparing `math.floor(x) == x`.
* To [round](https://en.wikipedia.org/wiki/Rounding#Rounding\_to\_the\_nearest\_integer) a number to the nearest integer (half up), use `math.floor(x + 0.5)`.

#### int64 <a href="#int64" id="int64"></a>

The `int64` number type refers to a signed 64-bit integer. This type is often used for methods which use ID numbers from the Roblox website, such as [`MarketplaceService:PromptPurchase()`](https://developer.roblox.com/en-us/api-reference/function/MarketplaceService/PromptPurchase) — in these cases, a signed 64-bit integer is expected (-263 to 263 - 1).

#### float <a href="#float" id="float"></a>

The `float` number type refers to a [single-precision (32-bit) floating point number](https://en.wikipedia.org/wiki/Single-precision\_floating-point\_format). This type isn’t as precise as normal numbers, but the difference typically won’t matter.
