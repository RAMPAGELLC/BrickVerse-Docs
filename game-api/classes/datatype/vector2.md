# Vector2

In BrickVerse, the `Vector2` datatype is often used in working with GUI elements and 2D mouse positions.

### Constructors <a href="#constructors" id="constructors"></a>

| **Vector2.new** ( number x, number y )               |
| ---------------------------------------------------- |
| Returns a Vector2 from the given x and y components. |

### Properties <a href="#properties" id="properties"></a>

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td>Vector2 <strong>Vector2.zero</strong></td></tr><tr><td><p>A Vector2 with a magnitude of zero.</p><p>This API member is a <strong>constant</strong>, and must be accessed through the <code>Vector2</code> global as opposed to an individual <code>Vector2</code> object.</p><p></p><pre><code>print(Vector2.zero) --> 0, 0
</code></pre></td></tr></tbody></table>

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td>Vector2 <strong>Vector2.one</strong></td></tr><tr><td><p>A Vector2 with a value of 1 on every axis.</p><p>This API member is a <strong>constant</strong>, and must be accessed through the <code>Vector2</code> global as opposed to an individual <code>Vector2</code> object.</p><p></p><pre><code>print(Vector2.one) --> 1, 1
</code></pre></td></tr></tbody></table>

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td>Vector2 <strong>Vector2.xAxis</strong></td></tr><tr><td><p>A Vector2 with a value of 1 on the X axis.</p><p>This API member is a <strong>constant</strong>, and must be accessed through the <code>Vector2</code> global as opposed to an individual <code>Vector2</code> object.</p><p></p><pre><code>print(Vector2.xAxis) --> 1, 0
</code></pre></td></tr></tbody></table>

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td>Vector2 <strong>Vector2.yAxis</strong></td></tr><tr><td><p>A Vector2 with a value of 1 on the Y axis.</p><p>This API member is a <strong>constant</strong>, and must be accessed through the <code>Vector2</code> global as opposed to an individual <code>Vector2</code> object.</p><p></p><pre><code>print(Vector2.yAxis) --> 0, 1
</code></pre></td></tr></tbody></table>

| number **Vector2.X**             |
| -------------------------------- |
| The x-coordinate of the Vector2. |

| number **Vector2.Y**             |
| -------------------------------- |
| The y-coordinate of the Vector2. |

| number **Vector2.Magnitude** |
| ---------------------------- |
| The length of the vector.    |

| Vector2 **Vector2.Unit**         |
| -------------------------------- |
| A normalized copy of the vector. |

### Functions <a href="#functions" id="functions"></a>

| number **Vector2:Cross** ( Vector2 other )    |
| --------------------------------------------- |
| Returns the cross product of the two vectors. |

| number **Vector2:Dot** ( Vector2 v )             |
| ------------------------------------------------ |
| Returns a scalar dot product of the two vectors. |

| Vector2 **Vector2:Lerp** ( Vector2 v, number alpha )                                     |
| ---------------------------------------------------------------------------------------- |
| Returns a Vector2 linearly interpolated between this Vector2 and v by the fraction alpha |

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td>Vector2 <strong>Vector2:Max</strong> ( Tuple others... )</td></tr><tr><td><p>Returns a <code>Vector2</code> where each component is the highest among the respective components of the provided <code>Vector2</code>s.</p><p></p><pre class="language-lua"><code class="lang-lua">local a = Vector2.new(1, 2)
local b = Vector2.new(2, 1) 
print(a:Max(b)) -- Vector2.new(2, 2)
</code></pre></td></tr></tbody></table>

<table data-header-hidden><thead><tr><th></th></tr></thead><tbody><tr><td>Vector2 <strong>Vector2:Min</strong> ( Tuple others... )</td></tr><tr><td><p>Returns a <code>Vector2</code> where each component is the lowest among the respective components of the provided <code>Vector2</code>s.</p><p></p><pre class="language-lua"><code class="lang-lua">local a = Vector2.new(1, 2)local b = Vector2.new(2, 1) 
print(a:Min(b)) -- Vector2.new(1, 1)
</code></pre></td></tr></tbody></table>
