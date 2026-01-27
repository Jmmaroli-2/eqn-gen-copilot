# Define the template product functions.
# This file now imports all template product functions from the fcns folder.

from .fcns import (
    # 1-variable functions
    dct_poly1_1, dct_poly2_1, dct_squared_1, dct_poly3_1, dct_cubed_1,
    dct_poly4_1, dct_poly5_1, dct_exp_1, dct_sin_1, dct_tanh_1, dct_tanhx_1,
    # 2-variable functions
    dct_poly22_2, dct_poly33_2, dct_poly44_2, dct_poly55_2,
    dct_exp_lin12_2, dct_exp_lin21_2, dct_tanh12_2, dct_tanh21_2,
    # 3+ variable functions
    dct_linear_3, dct_linear_4, dct_linear_5
)

def fitting_functions():
    """
    Returns a dictionary of template product functions organized by input count.
    
    Returns:
        dict: A dictionary where keys are input counts (1-5) and values are lists
              of dictionaries containing template product function definitions.
    """
    
    #=========================================================================#
    # Functions of 1 variable.
    #=========================================================================#
    input_1_list = [dct_poly1_1,
                    dct_poly2_1,
                    dct_poly3_1,
                    dct_poly4_1,
                    dct_poly5_1,
                    dct_squared_1,
                    dct_cubed_1,
                    dct_exp_1,
                    dct_sin_1,
                    dct_tanh_1,
                    dct_tanhx_1,
                    ]
    
    #=========================================================================#
    # Functions of 2 variables.
    #=========================================================================#
    input_2_list = [dct_poly22_2,
                    dct_poly33_2,
                    dct_poly44_2,
                    dct_poly55_2,
                    dct_exp_lin12_2,
                    dct_exp_lin21_2,
                    dct_tanh12_2,
                    dct_tanh21_2,
                    ]
    
    #=========================================================================#
    # Functions of 3+ variables.
    #=========================================================================#
    input_3_list = [dct_linear_3]
    
    input_4_list = [dct_linear_4]
    
    input_5_list = [dct_linear_5]

    functionDictionary = {
        1: input_1_list,
        2: input_2_list,
        3: input_3_list,
        4: input_4_list,
        5: input_5_list
    }
    
    return functionDictionary
