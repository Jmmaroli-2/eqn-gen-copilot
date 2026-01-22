# Reproducibility Notes

## Random Seed Configuration

This codebase now includes comprehensive random seed configuration to ensure reproducible results across multiple runs.

### Seeds Set

The following random number generators are properly seeded:

1. **NumPy Random**: Set in three locations
   - `run_example.py` line 60: `np.random.seed(1234)` - for data generation
   - `lib/analyze_model.py` line 33: `np.random.seed(seed)` - for model analysis
   - `lib/tune_model.py` line 23: `np.random.seed(seed)` - for genetic algorithm

2. **Python Random**: Set in one location
   - `lib/tune_model.py` line 22: `random.seed(seed)` - for genetic algorithm operations

3. **PyTorch Random**: Set in one location
   - `lib/create_model.py` line 70: `torch.manual_seed(seed)` - for model initialization

4. **PyTorch CUDA Random**: Set in one location (when CUDA is enabled)
   - `lib/create_model.py` lines 74-75: `torch.cuda.manual_seed(seed)` and `torch.cuda.manual_seed_all(seed)`

5. **CUDA Determinism**: Set in one location (when CUDA is enabled)
   - `lib/create_model.py` lines 77-78: 
     - `torch.backends.cudnn.deterministic = True`
     - `torch.backends.cudnn.benchmark = False`

### Default Seed Values

- Data generation: `1234` (hardcoded in `run_example.py`)
- Model training: `1111` (from `model_parameters["seed"]`)
- Analysis: `1111` (from `analysis_parameters["seed"]`)
- Genetic algorithm tuning: `1111` (from `analysis_parameters["seed"]`)

### Testing Reproducibility

To verify reproducibility, run the same example multiple times:

```bash
python run_example.py 4
python run_example.py 4
```

The output should be identical across runs.

### Performance Note

When CUDA is enabled, the deterministic settings (`cudnn.deterministic=True` and `cudnn.benchmark=False`) may reduce performance slightly in exchange for reproducibility. This is the recommended configuration for ensuring consistent results.
