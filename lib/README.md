# Fitting Functions Library

This document lists all the template fitting functions (`fcn_` functions) available in `fitting_functions.py`. These functions are used for curve fitting in the equation generation framework.

## Polynomial Functions (1 variable)

### fcn_poly1_1(x, a)
Linear function: `a*x[0]`

### fcn_poly2_1(x, a, b)
Quadratic polynomial: `a*x[0]^2 + b*x[0]`

### fcn_squared_1(x, a)
Pure squared term: `a*x[0]^2`

### fcn_poly3_1(x, a, b, c)
Cubic polynomial: `a*x[0]^3 + b*x[0]^2 + c*x[0]`

### fcn_cubed_1(x, a)
Pure cubic term: `a*x[0]^3`

### fcn_poly4_1(x, a, b, c, d)
Quartic polynomial: `a*x[0]^4 + b*x[0]^3 + c*x[0]^2 + d*x[0]`

### fcn_poly5_1(x, a, b, c, d, e)
Quintic polynomial: `a*x[0]^5 + b*x[0]^4 + c*x[0]^3 + d*x[0]^2 + e*x[0]`

## Polynomial Functions (2 variables)

### fcn_poly22_2(x, a)
Bilinear term: `a*x[0]*x[1]`

### fcn_poly33_2(x, a, b, c)
Second-order bivariate polynomial:
```
a*x[0]*x[1] + b*x[0]^2*x[1] + c*x[0]*x[1]^2
```

### fcn_poly44_2(x, a, b, c, d, e, f)
Third-order bivariate polynomial:
```
a*x[0]*x[1] + b*x[0]^2*x[1] + c*x[0]*x[1]^2
+ d*x[0]^3*x[1] + e*x[0]^2*x[1]^2 + f*x[0]*x[1]^3
```

### fcn_poly55_2(x, a, b, c, d, e, f, g, h, i, j)
Fourth-order bivariate polynomial:
```
a*x[0]*x[1] + b*x[0]^2*x[1] + c*x[0]*x[1]^2
+ d*x[0]^3*x[1] + e*x[0]^2*x[1]^2 + f*x[0]*x[1]^3
+ g*x[0]^4*x[1] + h*x[0]^3*x[1]^2 + i*x[0]^2*x[1]^3 + j*x[0]*x[1]^4
```

## Multilinear Functions

### fcn_linear_3(x, a)
Three-variable product: `a*x[0]*x[1]*x[2]`

### fcn_linear_4(x, a)
Four-variable product: `a*x[0]*x[1]*x[2]*x[3]`

### fcn_linear_5(x, a)
Five-variable product: `a*x[0]*x[1]*x[2]*x[3]*x[4]`

## Exponential Functions

### fcn_exp_1(x, a, b)
Exponential function: `a*(exp(b*x[0]) - 1)`

### fcn_exp_lin12_2(x, a)
Linear-exponential product: `a*x[0]*(exp(x[1]) - 1)`

### fcn_exp_lin21_2(x, a)
Linear-exponential product (reversed): `a*x[1]*(exp(x[0]) - 1)`

## Trigonometric and Hyperbolic Functions

### fcn_sin_1(x, a, b, c)
Sinusoidal function: `a*sin(b*x[0] + c) - a*sin(c)`

### fcn_tanh_1(x, a, b)
Hyperbolic tangent: `a*tanh(b*x[0])`

### fcn_tanhx_1(x, a, b, c, d)
Extended hyperbolic tangent with linear term:
```
a*tanh(b*(x[0] + c)) + d*(x[0] + c) - (a*tanh(b*c) + d*c)
```

### fcn_tanh12_2(x, a, b, c, d, e)
Product of two hyperbolic tangents:
```
a*tanh(b*x[0] - c)*tanh(d*x[1] - e) - a*tanh(-c)*tanh(-e)
```

### fcn_tanh21_2(x, a, b, c, d, e)
Product of two hyperbolic tangents (reversed order):
```
a*tanh(b*x[1] - c)*tanh(d*x[0] - e) - a*tanh(-c)*tanh(-e)
```

## Notes

- Each function has a corresponding `txt_` function that generates a text representation of the fitted equation.
- The functions support optional argument shifts (`argShift`) for mean-centering.
- The naming convention indicates:
  - The function type (poly, exp, sin, tanh, etc.)
  - The number or degree (1-5)
  - The number of input variables (1-5) as a suffix
