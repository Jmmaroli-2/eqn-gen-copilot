# Define the template product functions.
# This file dynamically imports all template product functions from the fcns folder.

import os
import importlib

def fitting_functions():
    """
    Returns a dictionary of template product functions organized by input count.
    
    This function dynamically imports all template product function modules from
    the fcns folder and makes their dct_* dictionaries available.
    
    Returns:
        dict: A dictionary where keys are input counts (1-5) and values are lists
              of dictionaries containing template product function definitions.
    """
    
    # Dynamically import all dct_* dictionaries from fcns modules
    fcns_dir = os.path.join(os.path.dirname(__file__), 'fcns')
    dct_dict = {}
    
    # Import all Python files in the fcns directory (except __init__.py)
    for filename in os.listdir(fcns_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Remove .py extension
            module = importlib.import_module(f'.fcns.{module_name}', package='lib')
            
            # Look for dct_* variable in the module
            for attr_name in dir(module):
                if attr_name.startswith('dct_'):
                    dct_dict[attr_name] = getattr(module, attr_name)
    
    # Extract the dictionaries we need (maintaining order)
    dct_poly1_1 = dct_dict.get('dct_poly1_1')
    dct_poly2_1 = dct_dict.get('dct_poly2_1')
    dct_squared_1 = dct_dict.get('dct_squared_1')
    dct_poly3_1 = dct_dict.get('dct_poly3_1')
    dct_cubed_1 = dct_dict.get('dct_cubed_1')
    dct_poly4_1 = dct_dict.get('dct_poly4_1')
    dct_poly5_1 = dct_dict.get('dct_poly5_1')
    dct_exp_1 = dct_dict.get('dct_exp_1')
    dct_sin_1 = dct_dict.get('dct_sin_1')
    dct_tanh_1 = dct_dict.get('dct_tanh_1')
    dct_tanhx_1 = dct_dict.get('dct_tanhx_1')
    dct_poly22_2 = dct_dict.get('dct_poly22_2')
    dct_poly33_2 = dct_dict.get('dct_poly33_2')
    dct_poly44_2 = dct_dict.get('dct_poly44_2')
    dct_poly55_2 = dct_dict.get('dct_poly55_2')
    dct_exp_lin12_2 = dct_dict.get('dct_exp_lin12_2')
    dct_exp_lin21_2 = dct_dict.get('dct_exp_lin21_2')
    dct_tanh12_2 = dct_dict.get('dct_tanh12_2')
    dct_tanh21_2 = dct_dict.get('dct_tanh21_2')
    dct_linear_3 = dct_dict.get('dct_linear_3')
    dct_linear_4 = dct_dict.get('dct_linear_4')
    dct_linear_5 = dct_dict.get('dct_linear_5')
    
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
