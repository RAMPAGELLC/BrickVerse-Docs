# bit32

## bit32

This library is a back-ported [feature from Lua 5.2](https://www.lua.org/manual/5.2/manual.html#6.7) which provides functions to perform bitwise operations.

| number **bit32.arshift** ( number x, number disp )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <p>Returns the number <code>x</code> shifted <code>disp</code> bits to the right. The number <code>disp</code> may be any representable integer. Negative displacements shift to the left.</p><p>This shift operation is what is called arithmetic shift. Vacant bits on the left are filled with copies of the higher bit of <code>x</code>; vacant bits on the right are filled with zeros. In particular, displacements with absolute values higher than 31 result in zero or 0xFFFFFFFF (all original bits are shifted out).</p> |

| number **bit32.band** ( Tuple numbers )    |
| ------------------------------------------ |
| Returns the bitwise _and_ of its operands. |

| number **bit32.bnot** ( number x )                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Returns the bitwise negation of <code>x</code>. For any integer <code>x</code>, the following identity holds:</p><p></p><pre><code>assert(bit32.bnot(x) == (-1 - x) % 2^32)
</code></pre> |

| number **bit32.bor** ( Tuple numbers )    |
| ----------------------------------------- |
| Returns the bitwise _or_ of its operands. |

| boolean **bit32.btest** ( Tuple numbers )                                                      |
| ---------------------------------------------------------------------------------------------- |
| Returns a boolean signalling whether the bitwise _and_ of its operands is different from zero. |

| number **bit32.bxor** ( Tuple numbers )             |
| --------------------------------------------------- |
| Returns the bitwise _exclusive or_ of its operands. |

| number **bit32.extract** ( number n, number field, number width = 1 )                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Returns the unsigned number formed by the bits `field` to `field + width - 1` from `n`. Bits are numbered from 0 (least significant) to 31 (most significant). All accessed bits must be in the range \[0, 31]. The default for `width` is 1. |

| number **bit32.replace** ( number n, number v, number field, number width = 1 )                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Returns a copy of `n` with the bits `field` to `field + width - 1` replaced by the value `v`. See `bit32.extract` for details about `field` and `width`. |

| number **bit32.lrotate** ( number x, number disp )                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Returns the number <code>x</code> rotated <code>disp</code> bits to the left. The number <code>disp</code> may be any representable integer. For any valid displacement, the following identity holds:</p><p></p><pre><code>assert(bit32.lrotate(x, disp) == bit32.lrotate(x, disp % 32))
</code></pre><p>In particular, negative displacements rotate to the right.</p> |

| number **bit32.lshift** ( number x, number disp )                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Returns the number <code>x</code> shifted <code>disp</code> bits to the left. The number <code>disp</code> may be any representable integer. Negative displacements shift to the right. In any direction, vacant bits are filled with zeros. In particular, displacements with absolute values higher than 31 result in zero (all bits are shifted out).</p><p>For positive displacements, the following equality holds:</p><p></p><pre><code>assert(bit32.lshift(b, disp) == (b * 2^disp) % 2^32)
</code></pre> |

| number **bit32.rrotate** ( number x, number disp )                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Returns the number <code>x</code> rotated <code>disp</code> bits to the right. The number <code>disp</code> may be any representable integer.</p><p>For any valid displacement, the following identity holds:</p><p></p><pre><code>assert(bit32.rrotate(x, disp) == bit32.rrotate(x , disp % 32))
</code></pre><p>In particular, negative displacements rotate to the left.</p> |

| number **bit32.rshift** ( number x, number disp )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Returns the number <code>x</code> shifted <code>disp</code> bits to the right. The number <code>disp</code> may be any representable integer. Negative displacements shift to the left. In any direction, vacant bits are filled with zeros. In particular, displacements with absolute values higher than 31 result in zero (all bits are shifted out).</p><p>For positive displacements, the following equality holds:</p><p></p><pre><code>assert(bit32.rshift(b, disp) == math.floor(b % 2^32 / 2^disp))
</code></pre><p>This shift operation is what is called logical shift.</p> |
