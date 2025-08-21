# API Mode - C Sources Example

This folder demonstrates CFFI's API mode when calling C sources instead of a compiled library.

## Files

- `pi.c` - C source file with the Pi approximation function
- `pi.h` - Header file declaring the function
- `pi_extension_build.py` - CFFI builder script that creates the Python extension
- `test_pi.py` - Test script that builds and tests the extension
- `README.md` - This file

## How it works

This example shows how to use CFFI to create a Python extension from C source files:

1. **C Source Files**: `pi.c` and `pi.h` contain a simple Monte Carlo method for approximating Pi
2. **CFFI Builder**: `pi_extension_build.py` uses CFFI to compile the C sources into a Python extension
3. **Python Usage**: Once built, you can import and use the C function from Python

## Building and Testing

### Method 1: Build and test in one step
```cmd
python test_pi.py
```

### Method 2: Manual steps
```cmd
# Build the extension
python pi_extension_build.py

# Test the extension
python test_pi.py --test-only
```

## Windows Compatibility

This example has been configured to work properly on Windows:

- No external math library linking required (math functions are built into the Windows C runtime)
- Uses proper Windows-compatible file paths and build settings
- Should work with both MinGW and MSVC compilers

## Expected Output

The test should show Pi approximations like:
```
Pi approximation with 10 iterations: 3.2 (or similar)
Pi approximation with 10000 iterations: 3.14... (closer to actual Pi)
Pi approximation with 100000 iterations: 3.141... (even closer)
```

Note: Since this uses a Monte Carlo method with random numbers, the exact values will vary between runs.

## Generated Files

After building, you'll see these generated files:
- `_pi.c` - Generated C wrapper code
- `_pi.*.pyd` - The compiled Python extension (Windows DLL)
- Build artifacts in temporary directories

## Cleanup

To clean up generated files, you can manually delete:
- `_pi.c`
- `_pi.*.pyd`
- `__pycache__/` directories
- Any temporary build directories
