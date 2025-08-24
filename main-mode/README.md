# Pi Approximation CFFI Demo - Main Mode

This project demonstrates how to use Python CFFI (C Foreign Function Interface) to create a Python extension from C code. The example implements a Monte Carlo method to approximate the value of Pi.

## Project Structure

```
main-mode/
├── lib/
│   └── pi.c             # C source code with pi_approx function
├── include/
│   └── pi.h             # C header file
├── piapprox_build.py    # CFFI build script
├── test.py              # Test script to demonstrate the extension
└── README.md            # This file
```

## Files Description

- **`lib/pi.c`**: Contains the `pi_approx()` function that uses a Monte Carlo method to approximate Pi
- **`include/pi.h`**: Header file declaring the `pi_approx()` function
- **`piapprox_build.py`**: CFFI build script that compiles the C code into a Python extension
- **`test.py`**: Python test script that demonstrates how to use the compiled extension

## Prerequisites

- Python 3.x with CFFI installed (`pip install cffi`)
- Microsoft Visual Studio 2022 (Community edition or higher) with C++ build tools
- Windows operating system (this guide is Windows-specific)

## Build Process

You can build this project in three ways: using the direct CFFI approach, using setuptools, or as a shared library (DLL).

### Method 1: Direct CFFI Build (Manual)

#### Step 1: Set up Visual Studio Environment

Open a Command Prompt and set up the Visual Studio build environment:

```cmd
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
```

#### Step 2: Compile C Source to Object File

```cmd
cl /c lib\pi.c
```

This creates `pi.obj` from the C source code.

#### Step 3: Create Static Library

```cmd
lib /OUT:piapprox.lib pi.obj
```

This creates `piapprox.lib`, a static library that can be linked with the Python extension.

#### Step 4: Build Python Extension

```cmd
python piapprox_build.py
```

This uses CFFI to:
- Generate the C wrapper code (`_pi_cffi.c`)
- Compile the extension module (`_pi_cffi.cp3xx-win_amd64.pyd`)
- Link against the `piapprox.lib` library

### Method 2: Using setuptools (Recommended)

This method uses Python's standard build tools and is more suitable for distribution.

#### Step 1: Set up Visual Studio Environment

```cmd
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
```

#### Step 2: Build Prerequisites

```cmd
cl /c lib\pi.c
lib /OUT:piapprox.lib pi.obj
```

#### Step 3: Build Extension with setuptools

```cmd
python setup.py build_ext --inplace
```

This command:
- Reads the `setup.py` configuration
- Executes the CFFI build script (`piapprox_build.py`)
- Compiles and links the extension
- Places the compiled `.pyd` file in the current directory

#### Alternative setuptools commands:

```cmd
# Install in development mode (editable install)
pip install -e .

# Build distribution packages
python setup.py sdist bdist_wheel

# Install normally
pip install .
```

**Explanation of pip install options:**

- **`pip install .`** (Normal Installation):
  - Builds and installs the package into your Python environment permanently
  - Creates a copy of the compiled extension in your site-packages directory
  - If you make changes to the source code, you need to reinstall to see the changes
  - The package becomes available system-wide (or environment-wide)
  - Use this for final/production installations

- **`pip install -e .`** (Editable/Development Installation):
  - Creates a "link" to your source directory instead of copying files
  - Changes to Python source files are immediately reflected (no reinstall needed)
  - For C extensions, you still need to rebuild after changes to C code
  - Ideal for development and testing
  - The `-e` stands for "editable" mode
  - Your package is installed but points to your working directory

**When to use each:**
- Use `pip install -e .` during development when you're making frequent changes
- Use `pip install .` for final installation or when distributing to others

### Method 3: Shared Library (DLL) Approach

This method creates a reusable DLL that can be shared across multiple applications.

#### Quick Build with Batch Script

```cmd
build_dll.bat
```

#### Manual Build Steps

```cmd
# Set up Visual Studio environment
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

# Compile C source
cl /c lib\pi_dll.c /I include

# Create DLL
cl /LD pi_dll.obj /Fe:piapprox.dll

# Build Python extension
python piapprox_build_dll.py

# Test
python test_dll.py
```

**Advantages of DLL approach:**
- Reusable library that can be used by multiple applications
- Smaller Python extensions (logic is in the DLL)
- Can update the DLL independently of Python extensions
- Memory efficient (shared across processes)

**See `README_DLL.md` for detailed information about the shared library approach.**

## Running the Test

After successful compilation, run the test script:

```cmd
python test.py
```

Expected output:
```
Testing Pi Approximation Function
========================================
Iterations:     1000 | Pi approx: 3.144000 | Error: 0.002407
Iterations:    10000 | Pi approx: 3.141200 | Error: 0.000393
Iterations:   100000 | Pi approx: 3.141872 | Error: 0.000279
Iterations:  1000000 | Pi approx: 3.141836 | Error: 0.000243

Note: This is a Monte Carlo approximation, so results will vary each run.
Generally, more iterations should give better approximations.
```

## How It Works

### The C Algorithm

The `pi_approx()` function uses a Monte Carlo method:
1. Generate random points in a square
2. Check if each point falls inside a unit circle
3. The ratio of points inside the circle to total points approximates π/4
4. Multiply by 4 to get the Pi approximation

### CFFI Integration

1. **`ffibuilder.cdef()`**: Declares the C function signature that Python will use
2. **`ffibuilder.set_source()`**: Specifies the C source to include and libraries to link
3. **`ffibuilder.compile()`**: Builds the extension module

### Python Usage

The compiled extension is imported as `_pi_cffi` and the C function is accessed via `_pi_cffi.lib.pi_approx()`.

## Troubleshooting

### Common Issues

1. **"'cl' is not recognized"**: Visual Studio environment not set up
   - Solution: Run the vcvars64.bat script first

2. **"cannot open input file 'piapprox.lib'"**: Static library not built
   - Solution: Follow steps 1-3 to create the library first

3. **"No module named '_pi_cffi'"**: Extension not compiled
   - Solution: Run `python piapprox_build.py` or `python setup.py build_ext --inplace` after building the library

4. **"Cannot open include file: 'pi.h'"**: Header file not found during setup.py build
   - Solution: Ensure `include_dirs=['.']` is set in `piapprox_build.py` and you're running from the correct directory

5. **"'piapprox_build' does not name an existing file"**: Incorrect cffi_modules path in setup.py
   - Solution: Use `cffi_modules=["piapprox_build.py:ffibuilder"]` (include the `.py` extension)

### Setup.py Warnings

You may see these warnings when using setup.py - they don't affect functionality:

- **DeprecatedInstaller warning**: setuptools.installer is deprecated
- **SetuptoolsDeprecationWarning**: License classifiers are deprecated  

These are just warnings about future changes to setuptools and can be ignored.

### Build Dependencies

The build process creates these intermediate files:
- `pi.obj` - Object file from C compilation
- `piapprox.lib` - Static library
- `_pi_cffi.c` - Generated CFFI wrapper code
- `_pi_cffi.cp3xx-win_amd64.pyd` - Final Python extension module

## Complete Build Scripts

### Manual Build Script (build.bat)

For the direct CFFI approach:

```batch
@echo off
echo Setting up Visual Studio environment...
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

echo Compiling C source...
cl /c pi.c

echo Creating static library...
lib /OUT:piapprox.lib pi.obj

echo Building Python extension...
python piapprox_build.py

echo Build complete! Run 'python test.py' to test.
```

### Setuptools Build Script (build_setuptools.bat)

For the setuptools approach:

```batch
@echo off
echo Setting up Visual Studio environment...
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

echo Building prerequisites...
cl /c pi.c
lib /OUT:piapprox.lib pi.obj

echo Building Python extension with setuptools...
python setup.py build_ext --inplace

echo Build complete! Run 'python test.py' to test.
```

## Cleanup Scripts

To clean up build artifacts, use one of the provided cleanup scripts:

### Windows Batch Script
```cmd
cleanup.bat
```
or for comprehensive cleanup:
```cmd
cleanup_all.bat
```

### PowerShell Script
```powershell
.\cleanup.ps1
```

These scripts will delete:
- Object files (`*.obj`)
- Library files (`*.lib`, `*.dll`)
- Generated CFFI files (`_pi_cffi.c`)
- Python extension modules (`*.pyd`)
- Build directories (`Release/`, `build/`, `__pycache__/`)
- Distribution directories (`dist/`, `*.egg-info/`) - created by setuptools
- Temporary files (`*.exp`, `*.ilk`, `*.pdb`, `*.manifest`)

## Notes

- The Monte Carlo method produces different results each run due to random number generation
- More iterations generally produce better approximations, but take longer to compute
- This is a demonstration of CFFI's "main mode" where you compile C libraries and link them to Python extensions
