# Fitting Functions Library

This document lists all the template fitting functions (`fcn_` functions) available in `fitting_functions.py`. These functions are used for curve fitting in the equation generation framework.

## Polynomial Functions (1 variable)

### fcn_poly1_1(x, a)
Linear function: $ax_0$

### fcn_poly2_1(x, a, b)
Quadratic polynomial: $ax_0^2 + bx_0$

### fcn_squared_1(x, a)
Pure squared term: $ax_0^2$

### fcn_poly3_1(x, a, b, c)
Cubic polynomial: $ax_0^3 + bx_0^2 + cx_0$

### fcn_cubed_1(x, a)
Pure cubic term: $ax_0^3$

### fcn_poly4_1(x, a, b, c, d)
Quartic polynomial: $ax_0^4 + bx_0^3 + cx_0^2 + dx_0$

### fcn_poly5_1(x, a, b, c, d, e)
Quintic polynomial: $ax_0^5 + bx_0^4 + cx_0^3 + dx_0^2 + ex_0$

## Polynomial Functions (2 variables)

### fcn_poly22_2(x, a)
Bilinear term: $ax_0x_1$

### fcn_poly33_2(x, a, b, c)
Second-order bivariate polynomial:

$ax_0x_1 + bx_0^2x_1 + cx_0x_1^2$

### fcn_poly44_2(x, a, b, c, d, e, f)
Third-order bivariate polynomial:

$ax_0x_1 + bx_0^2x_1 + cx_0x_1^2 + dx_0^3x_1 + ex_0^2x_1^2 + fx_0x_1^3$

### fcn_poly55_2(x, a, b, c, d, e, f, g, h, i, j)
Fourth-order bivariate polynomial:

$ax_0x_1 + bx_0^2x_1 + cx_0x_1^2 + dx_0^3x_1 + ex_0^2x_1^2 + fx_0x_1^3 + gx_0^4x_1 + hx_0^3x_1^2 + ix_0^2x_1^3 + jx_0x_1^4$

## Multilinear Functions

### fcn_linear_3(x, a)
Three-variable product: $ax_0x_1x_2$

### fcn_linear_4(x, a)
Four-variable product: $ax_0x_1x_2x_3$

### fcn_linear_5(x, a)
Five-variable product: $ax_0x_1x_2x_3x_4$

## Exponential Functions

### fcn_exp_1(x, a, b)
Exponential function: $a(e^{bx_0} - 1)$

### fcn_exp_lin12_2(x, a)
Linear-exponential product: $ax_0(e^{x_1} - 1)$

### fcn_exp_lin21_2(x, a)
Linear-exponential product (reversed): $ax_1(e^{x_0} - 1)$

## Trigonometric and Hyperbolic Functions

### fcn_sin_1(x, a, b, c)
Sinusoidal function: $a\sin(bx_0 + c) - a\sin(c)$

### fcn_tanh_1(x, a, b)
Hyperbolic tangent: $a\tanh(bx_0)$

### fcn_tanhx_1(x, a, b, c, d)
Extended hyperbolic tangent with linear term:

$a\tanh(b(x_0 + c)) + d(x_0 + c) - (a\tanh(bc) + dc)$

### fcn_tanh12_2(x, a, b, c, d, e)
Product of two hyperbolic tangents:

$a\tanh(bx_0 - c)\tanh(dx_1 - e) - a\tanh(-c)\tanh(-e)$

### fcn_tanh21_2(x, a, b, c, d, e)
Product of two hyperbolic tangents (reversed order):

$a\tanh(bx_1 - c)\tanh(dx_0 - e) - a\tanh(-c)\tanh(-e)$

## Using the fitting_functions() Function

The `fitting_functions()` function returns a dictionary that organizes all available template functions by the number of input variables they accept. This dictionary is used by the equation generation framework to select appropriate functions during the curve fitting process.

### Structure

The function returns a dictionary with the following structure:

```python
{
    1: [list of 1-variable functions],
    2: [list of 2-variable functions],
    3: [list of 3-variable functions],
    4: [list of 4-variable functions],
    5: [list of 5-variable functions]
}
```

Each function in the lists is represented as a dictionary with the following keys:

- **`txt`**: A string representation of the function for display purposes
- **`txt_fcn`**: The corresponding `txt_` function that generates formatted text output
- **`fcn`**: The actual computational function (the `fcn_` function)
- **`upper`**: List of upper bounds for the function parameters during optimization
- **`lower`**: List of lower bounds for the function parameters during optimization
- **`weight`**: A weighting factor used in the selection process (lower values = less frequently selected)

### Example Function Entry

```python
dct_poly2_1 = {
    "txt": "a*x1^2 + b*x1",
    "txt_fcn": txt_poly2_1,
    "fcn": fcn_poly2_1,
    "upper": [10, 10],
    "lower": [-10, -10],
    "weight": 0.55
}
```

## Adding Custom Product Functions

To add your own custom product function to the library:

### Step 1: Define the Computational Function

Create a function that takes `x` (list of input variables) and parameter values:

```python
def fcn_custom_1(x, a, b):
    return a * np.exp(x[0]) + b * x[0]**2
```

### Step 2: Define the Text Generation Function

Create a corresponding function to generate text representation:

```python
def txt_custom_1(argList, argShift, a, b):
    if all(shift == 0 for shift in argShift):
        return "{:.2e}*e^(x{:d}[k-{:d}]) + {:.2e}*x{:d}[k-{:d}]^2".format(
            a, argList[0]["input_channel"]+1, argList[0]["delay"],
            b, argList[0]["input_channel"]+1, argList[0]["delay"])
    else:
        return "{:.2e}*e^(x{:d}[k-{:d}]-{:.2e}) + {:.2e}*(x{:d}[k-{:d}]-{:.2e})^2".format(
            a, argList[0]["input_channel"]+1, argList[0]["delay"], argShift[0],
            b, argList[0]["input_channel"]+1, argList[0]["delay"], argShift[0])
```

### Step 3: Create the Dictionary Entry

Add your function to the `fitting_functions()` function:

```python
dct_custom_1 = {
    "txt": "a*e^(x1) + b*x1^2",
    "txt_fcn": txt_custom_1,
    "fcn": fcn_custom_1,
    "upper": [10, 10],      # Upper bounds for parameters a and b
    "lower": [-10, -10],    # Lower bounds for parameters a and b
    "weight": 0.5           # Selection weight (0 < weight ≤ 1)
}
```

### Step 4: Add to Appropriate List

Add your dictionary to the appropriate input list based on the number of variables:

```python
input_1_list = [dct_poly1_1,
                dct_poly2_1,
                # ... other functions ...
                dct_custom_1,  # Add your custom function here
                ]
```

### Tips for Custom Functions

- **Parameter Bounds**: Choose bounds that are appropriate for your problem domain. Wider bounds allow more flexibility but may slow convergence.
- **Weight Selection**: Lower weights make the function less likely to be selected. Use lower weights for more complex or specialized functions.
- **Variable Indexing**: Remember that `x` is a list, so use `x[0]`, `x[1]`, etc., not `x0`, `x1`.
- **Mean Centering**: The `argShift` parameter in `txt_` functions handles mean-centering of inputs. Include both shifted and non-shifted versions in your text generation.
- **Naming Convention**: Follow the pattern `fcn_<type>_<nvars>` and `txt_<type>_<nvars>` for consistency.

## Notes

- Each function has a corresponding `txt_` function that generates a text representation of the fitted equation.
- The functions support optional argument shifts (`argShift`) for mean-centering.
- The naming convention indicates:
  - The function type (poly, exp, sin, tanh, etc.)
  - The number or degree (1-5)
  - The number of input variables (1-5) as a suffix
