# math

This library provides an interface to the standard C lua math library, encapsulating all functions within the `math` global.

**Summary**

**Functions**

**abs(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the absolute value of (x).

**acos(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the arc cosine of (x).

**asin(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the arc sine of (x).

**atan(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the arc tangent of (x) (in radians).

**atan2(y, x)**: (\mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R})

* Returns the arc tangent of (y/x) (in radians), using the signs of both parameters to determine the quadrant of the result.

**ceil(x)**: (\mathbb{R} \rightarrow \mathbb{Z})

* Returns the smallest integer larger than or equal to (x).

**clamp(x, min, max)**: (\mathbb{R} \times \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R})

* Returns a number within the range (\[min, max]).

**cos(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the cosine of (x) (assumed to be in radians).

**cosh(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the hyperbolic cosine of (x).

**deg(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the angle (x) (in radians) in degrees.

**exp(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the value (e^x).

**floor(x)**: (\mathbb{R} \rightarrow \mathbb{Z})

* Returns the largest integer smaller than or equal to (x).

**fmod(x, y)**: (\mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R})

* Returns the remainder of the division of (x) by (y) that rounds the quotient towards zero.

**frexp(x)**: (\mathbb{R} \rightarrow \mathbb{R} \times \mathbb{Z})

* Returns (m) and (e) such that (x = m \times 2^e), (e) is an integer, and the absolute value of (m) is in the range (\[0.5, 1)) (or zero when (x) is zero).

**ldexp(x, e)**: (\mathbb{R} \times \mathbb{Z} \rightarrow \mathbb{R})

* Returns (x \times 2^e).

**log(x, base)**: (\mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R})

* Returns the logarithm of (x) using the given base, or the mathematical constant (e) if no base is provided (natural logarithm).

**log10(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the base-10 logarithm of (x).

**max(x, ...)**: (\mathbb{R} \times \mathbb{R}^\* \rightarrow \mathbb{R})

* Returns the maximum value among the numbers passed to the function.

**min(x, ...)**: (\mathbb{R} \times \mathbb{R}^\* \rightarrow \mathbb{R})

* Returns the minimum value among the numbers passed to the function.

**modf(x)**: (\mathbb{R} \rightarrow \mathbb{Z} \times \mathbb{R})

* Returns two numbers, the integral part of (x) and the fractional part of (x).

**noise(x, y, z)**: (\mathbb{R} \times \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R})

* Returns a Perlin noise value.

**pow(x, y)**: (\mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R})

* Returns (x^y).

**rad(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the angle (x) (in degrees) in radians.

**random(m, n)**: (\mathbb{Z} \times \mathbb{Z} \rightarrow \mathbb{Z})

* Returns a random number within the range provided.

**randomseed(x)**: (\mathbb{Z} \rightarrow \emptyset)

* Sets (x) as the seed for the pseudo-random generator.

**round(x)**: (\mathbb{R} \rightarrow \mathbb{Z})

* Returns the integer with the smallest difference between it and the given number.

**sign(x)**: (\mathbb{R} \rightarrow {-1, 0, 1})

* Returns (-1) if (x < 0), (0) if (x = 0), or (1) if (x > 0).

**sin(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the sine of (x) (assumed to be in radians).

**sinh(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the hyperbolic sine of (x).

**sqrt(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the square root of (x).

**tan(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the tangent of (x) (assumed to be in radians).

**tanh(x)**: (\mathbb{R} \rightarrow \mathbb{R})

* Returns the hyperbolic tangent of (x).

**Properties**

1. **huge**: (\mathbb{R})
   * Returns the value (HUGE\_VAL), a value larger than or equal to any other numerical value (about (2^{1024})).
2. **pi**: (\mathbb{R})
   * The value of (\pi).
