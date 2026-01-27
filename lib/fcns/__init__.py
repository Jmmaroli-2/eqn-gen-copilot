# Import all template product functions
# Each module contains fcn_, txt_, and dct_ for a template product function

from .poly1_1 import fcn_poly1_1, txt_poly_1, dct_poly1_1
from .poly2_1 import fcn_poly2_1, txt_poly2_1, dct_poly2_1
from .squared_1 import fcn_squared_1, txt_squared_1, dct_squared_1
from .poly3_1 import fcn_poly3_1, txt_poly3_1, dct_poly3_1
from .cubed_1 import fcn_cubed_1, txt_cubed_1, dct_cubed_1
from .poly4_1 import fcn_poly4_1, txt_poly4_1, dct_poly4_1
from .poly5_1 import fcn_poly5_1, txt_poly5_1, dct_poly5_1
from .poly22_2 import fcn_poly22_2, txt_poly22_2, dct_poly22_2
from .poly33_2 import fcn_poly33_2, txt_poly33_2, dct_poly33_2
from .poly44_2 import fcn_poly44_2, txt_poly44_2, dct_poly44_2
from .poly55_2 import fcn_poly55_2, txt_poly55_2, dct_poly55_2
from .linear_3 import fcn_linear_3, txt_linear_3, dct_linear_3
from .linear_4 import fcn_linear_4, txt_linear_4, dct_linear_4
from .linear_5 import fcn_linear_5, txt_linear_5, dct_linear_5
from .exp_1 import fcn_exp_1, txt_exp_1, dct_exp_1
from .exp_lin12_2 import fcn_exp_lin12_2, txt_exp_lin12_2, dct_exp_lin12_2
from .exp_lin21_2 import fcn_exp_lin21_2, txt_exp_lin21_2, dct_exp_lin21_2
from .sin_1 import fcn_sin_1, txt_sin_1, dct_sin_1
from .tanh_1 import fcn_tanh_1, txt_tanh_1, dct_tanh_1
from .tanhx_1 import fcn_tanhx_1, txt_tanhx_1, dct_tanhx_1
from .tanh12_2 import fcn_tanh12_2, txt_tanh12_2, dct_tanh12_2
from .tanh21_2 import fcn_tanh21_2, txt_tanh21_2, dct_tanh21_2

__all__ = [
    # 1-variable functions
    'fcn_poly1_1', 'txt_poly_1', 'dct_poly1_1',
    'fcn_poly2_1', 'txt_poly2_1', 'dct_poly2_1',
    'fcn_squared_1', 'txt_squared_1', 'dct_squared_1',
    'fcn_poly3_1', 'txt_poly3_1', 'dct_poly3_1',
    'fcn_cubed_1', 'txt_cubed_1', 'dct_cubed_1',
    'fcn_poly4_1', 'txt_poly4_1', 'dct_poly4_1',
    'fcn_poly5_1', 'txt_poly5_1', 'dct_poly5_1',
    'fcn_exp_1', 'txt_exp_1', 'dct_exp_1',
    'fcn_sin_1', 'txt_sin_1', 'dct_sin_1',
    'fcn_tanh_1', 'txt_tanh_1', 'dct_tanh_1',
    'fcn_tanhx_1', 'txt_tanhx_1', 'dct_tanhx_1',
    
    # 2-variable functions
    'fcn_poly22_2', 'txt_poly22_2', 'dct_poly22_2',
    'fcn_poly33_2', 'txt_poly33_2', 'dct_poly33_2',
    'fcn_poly44_2', 'txt_poly44_2', 'dct_poly44_2',
    'fcn_poly55_2', 'txt_poly55_2', 'dct_poly55_2',
    'fcn_exp_lin12_2', 'txt_exp_lin12_2', 'dct_exp_lin12_2',
    'fcn_exp_lin21_2', 'txt_exp_lin21_2', 'dct_exp_lin21_2',
    'fcn_tanh12_2', 'txt_tanh12_2', 'dct_tanh12_2',
    'fcn_tanh21_2', 'txt_tanh21_2', 'dct_tanh21_2',
    
    # 3+ variable functions
    'fcn_linear_3', 'txt_linear_3', 'dct_linear_3',
    'fcn_linear_4', 'txt_linear_4', 'dct_linear_4',
    'fcn_linear_5', 'txt_linear_5', 'dct_linear_5',
]
