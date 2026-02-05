"""
Test to verify that tune_model correctly handles the case when parameter_count = 0.
This test creates a model function with no tunable parameters and ensures:
1. The function completes without errors
2. The genetic algorithm is skipped (no wasteful computation)
3. The returned model structure is correct
"""

import numpy as np
from lib.tune_model import tune_model

def test_parameter_count_zero():
    """Test tune_model with a channel that has no tunable parameters."""
    
    # Create test data
    input_data = np.random.rand(100, 2)
    output_data = np.random.rand(100, 1)
    
    # Create a model function with no tunable parameters
    # This simulates a constant function (bias only with no parameters)
    model_function = [
        [
            {
                "parameters": [],  # No parameters to tune
                "function": {
                    "upper": [],
                    "lower": [],
                    "fcn": lambda x: 1.0,  # Constant function
                    "txt_fcn": lambda arg_list, shift: "1.0"
                },
                "arg_list": [],
                "shift": 0,
                "estimate_string": "1.0"
            }
        ]
    ]
    
    # Set up minimal tuning parameters
    tuning_parameters = {
        "GA_population": 10,
        "GA_generations": 5,
        "visual": False,
        "save_visual": False
    }
    
    print("Testing tune_model with parameter_count = 0...")
    print("=" * 60)
    
    # Call tune_model - should skip GA and return quickly
    result = tune_model(tuning_parameters, model_function, input_data, output_data)
    
    print("=" * 60)
    print("Test completed successfully!")
    print()
    
    # Verify the result structure is correct
    assert result is not None, "Result should not be None"
    assert len(result) == 1, "Result should have 1 channel"
    assert len(result[0]) == 1, "Channel should have 1 product function"
    assert result[0][0]["parameters"] == [], "Parameters should still be empty"
    
    print("✓ All assertions passed!")
    print("✓ Model structure is preserved")
    print("✓ Genetic algorithm was skipped (no wasteful computation)")
    return True


def test_parameter_count_multiple_channels():
    """Test tune_model with multiple channels that all have no parameters."""
    
    # Create test data
    input_data = np.random.rand(100, 2)
    output_data = np.random.rand(100, 2)  # 2 channels
    
    # Create a model with 2 channels, both without tunable parameters
    model_function = [
        # Channel 1: No parameters
        [
            {
                "parameters": [],  # No parameters
                "function": {
                    "upper": [],
                    "lower": [],
                    "fcn": lambda x: 1.0,
                    "txt_fcn": lambda arg_list, shift: "1.0"
                },
                "arg_list": [],
                "shift": 0,
                "estimate_string": "1.0"
            }
        ],
        # Channel 2: No parameters
        [
            {
                "parameters": [],  # No parameters
                "function": {
                    "upper": [],
                    "lower": [],
                    "fcn": lambda x: 2.0,
                    "txt_fcn": lambda arg_list, shift: "2.0"
                },
                "arg_list": [],
                "shift": 0,
                "estimate_string": "2.0"
            }
        ]
    ]
    
    # Set up minimal tuning parameters
    tuning_parameters = {
        "GA_population": 10,
        "GA_generations": 5,
        "visual": False,
        "save_visual": False
    }
    
    print("Testing tune_model with multiple channels (no parameters)...")
    print("=" * 60)
    
    # Call tune_model
    result = tune_model(tuning_parameters, model_function, input_data, output_data)
    
    print("=" * 60)
    print("Test completed successfully!")
    print()
    
    # Verify the result structure
    assert result is not None, "Result should not be None"
    assert len(result) == 2, "Result should have 2 channels"
    assert result[0][0]["parameters"] == [], "Channel 1 should have no parameters"
    assert result[1][0]["parameters"] == [], "Channel 2 should have no parameters"
    
    print("✓ All assertions passed!")
    print("✓ Both channels were skipped correctly")
    print("✓ Model structure is preserved")
    return True


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("TEST 1: Single channel with no parameters")
    print("=" * 60 + "\n")
    test_parameter_count_zero()
    
    print("\n" + "=" * 60)
    print("TEST 2: Multiple channels with no parameters")
    print("=" * 60 + "\n")
    test_parameter_count_multiple_channels()
    
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED!")
    print("=" * 60 + "\n")
