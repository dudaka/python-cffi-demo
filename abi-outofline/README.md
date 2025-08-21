# Out-of-line ABI Mode Example

This example demonstrates CFFI's out-of-line ABI mode, which allows you to:
- Use ABI mode without needing a C compiler at runtime
- Reduce import times by pre-compiling the FFI interface
- Work with both standard C library and Windows-specific functions

## Files

- `simple_example_build.py` - Build script that generates the FFI module
- `usage_example.py` - Main script that uses the generated FFI module

## How to run

1. First, run the build script to generate the FFI module:
```cmd
python simple_example_build.py
```

This will create a `_simple_example.py` file containing the compiled FFI interface.

2. Then run the usage example:
```cmd
python usage_example.py
```

## What it demonstrates

- Loading the C runtime library on Windows (msvcrt.dll)
- Using standard C functions like `printf`, `puts`, and `getenv`
- Loading Windows-specific libraries (kernel32.dll)
- Using Windows API functions for console manipulation
- Proper error handling for cross-platform compatibility

## Key differences from in-line ABI mode

- The FFI interface is pre-compiled, reducing import time
- No need to parse C headers at runtime
- Better for complex applications with many C declarations
- Generated module can be distributed without the build script

## Distribution with setuptools

The example includes a complete `setup.py` configuration that demonstrates how to distribute CFFI projects:

```cmd
python setup.py build
python setup.py sdist
python setup.py bdist_wheel
```

### Key setuptools features:

- Uses `cffi_modules=["simple_example_build.py:ffibuilder"]` to automatically build the FFI module
- Includes `setup_requires=["cffi>=1.0.0"]` for build-time dependencies
- Provides console script entry points for easy command-line usage
- Properly handles package metadata and dependencies

### Installation:

```cmd
pip install .
```

Or in development mode:
```cmd
pip install -e .
```

### Testing the setup

Run the setup demonstration script:

```cmd
python setup_demo_simple.py
```

This script demonstrates:

- Building the package with `python setup.py build`
- Creating source distribution with `python setup.py sdist`
- Creating wheel distribution with `python setup.py bdist_wheel`
- Automatic CFFI module generation during build process
- Proper packaging for PyPI distribution

### Cleanup

To clean up all generated files, use one of the provided cleanup scripts:

**Windows (Batch):**
```cmd
cleanup.bat
```

**Windows (PowerShell):**
```cmd
cleanup.ps1
```

**Cross-platform (Python):**
```cmd
python cleanup.py
```

These scripts remove:
- Generated FFI module (`_simple_example.py`)
- Build directories (`build/`, `dist/`)
- Package metadata (`.egg-info/`)
- Python cache files (`__pycache__/`, `*.pyc`)
- Temporary setup files

## Windows-specific notes- Uses `ctypes.util.find_library("c")` to locate the C library
- Falls back to `msvcrt.dll` if the generic approach fails
- Demonstrates Windows console API usage for color output
- Handles cases where terminal doesn't support color changes
