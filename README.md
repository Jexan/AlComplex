# AlComplex

A Complex Number library. It uses its own complex number implementation. Its main goal it's to provide a more complete API, compared to the default complex number implementation in Python.

It's as simple as:

```
>>> from AlComplex import I, AlComplex, pi
>>> 2 + 3*I
2.0 + 3.0i
>>> AlComplex(2,3)
2.0 + 3.0i
>>> AlComplex(1)
1.0 + 0.0i
>>> # You can also use Polar Coordinates
>>> AlComplex.polar(2, pi)
0 - 2i
``` 

## Installation

Just run

``` pip install AlComplex ```

It has no external dependencies. 

## Details

Basic operations with complex and real numbers are supported

```
>>> -I + 4 + 3*I
4 + 2i
>>> (25+35*I)/5
5.0 + 7.0i
>>> (-8 + 14*I)/(2+3*I)
2.0000000000000018 + 4.000000000000001i
>>> I**I
.20787957635076193 + 0.0i
```

Note that since Floats behave weirdly, we use relative equality. Two Complex numbers are equal if their real and imaginary parts are close by at least ```1e-14```.

```
>>> (-8 + 14*I)/(2+3*I)
2.0000000000000018 + 4.000000000000001i
>>> (-8 + 14*I)/(2+3*I) == 2 + 4*I
True
```

AlComplex objects have a basic but complete API:

```
>>> z = 1 + I
>>> z.real
1.0
>>> z.imag
1.0
>>> z.abs()
1.4142135623730951
>>> z.phase()
0.7853981633974483
>>> z.to_polar()
(1.4142135623730951, 0.7853981633974483)
>>> z.to_rect_coord()
(1,1)
>>> z.conjugate()
1 - i
```

Note that there many aliases and ways to get the same value: 

```python 
from AlComplex import phase, module, conjugate, real, imaginary
z.phase() == z.arg() == z.angle() == phase(z)
z.abs() == z.magnitude() == z.module() == abs(z) == module(z)
z.real == real(z)
z.imag == imaginary(z)
z.conjugate() == conjugate(z)
``` 

There's also basic math functions, optimized for Complex objects. 

```
>>> from AlComplex import sin, exp, Ln
>>> from math import pi
>>> exp(2*pi*I)
1.0 + 0.0i
>>> sin(2*pi)
0.0 + 0.0i
>>> sin(2 + I)
1.4031192506220411 - 0.48905625904129324i
>>> Ln(exp(I)) 
0.0 + 1.0*I
``` 

Note that these functions work differently to ```cmath``` functions, since very small numbers are rounded to zero automatically.

```
>>> import cmath
>>> import AlComplex
>>> from math import pi
>>> cmath.sin(2*pi)
(-2.4492935982947064e-16+0j)
>>> AlComplex.sin(2*pi)
0.0 + 0.0i
>>> cmath.sin(2*pi) == 0
False
>>> AlComplex.sin(2*pi) == 0
True
```

The functions available are ```sin```, ```cos```, ```tan```, ```sec```, ```csc```, ```cot```, ```asin```, ```acos```, ```atan```, ```sinh```, ```cosh```, ```tanh```, ```sech```, ```csch```, ```coth```, ```asinh```, ```acosh```, ```atanh```, ```exp```, ```Ln```, ```sqrt``` and ```inverse```.

You can set representation of complex numbers with j, if you prefer.

```
>>> from AlComplex import J, use_j
>>> J
0.0 + 1.0i
>>> use_j(True)
>>> 2 + J
2.0 + 1.0j
>>> use_j(False)
>>> 2 + J
2.0 + 1.0i
```

There's also partial support for multiple valued functions. They all create generators.

```
>>> from AlComplex import int_roots, ln_values
>>> from math import pi
>>> list(int_roots(I, 3))
[0.866025403784439 + 0.5i, -0.866025403784438 + 0.5i, 0.0 - 1.0i]
>>> # Gives log(z.abs()) + (z.phase() + 2*pi*n)*I, where n takes the values from 0 to 2
>>> list(ln_values(I, 0, 3))
[0.0 + 1.5707963267948966i, 0.0 + 7.853981633974483i, 0.0 + 14.137166941154069i]
```

Currently only int_roots of a function and complex logarithm are supported. More to come. 

You can also get the n-th value of the log directly

```
>>> from AlComplex import ln_n_branch
>>> ln_n_branch(I, 2)
0.0 + 14.137166941154069i
```