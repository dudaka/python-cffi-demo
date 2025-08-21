# CFFI API Out-of-line Mode Example

This example demonstrates CFFI's API out-of-line mode, where C code is written directly in the build script and compiled into a Python extension module for maximum performance.

## What is API Out-of-line Mode?

In API out-of-line mode:
- C code is written directly in the build script (`example_build.py`)
- The code is compiled once into a `.pyd` file (on Windows)
- Python code imports and uses the compiled extension like any other module
- This provides maximum performance since the C code is compiled with optimizations

## Files in this Example

- `example_build.py`: Build script that defines C functions and compiles them
- `example.py`: Python script that uses the compiled C extension
- `README.md`: This documentation file
- `cleanup.bat`: Windows batch script to clean build artifacts

## Prerequisites

You need a C compiler installed on Windows:

### Option 1: Visual Studio Build Tools (Recommended)
1. Download "Build Tools for Visual Studio" from Microsoft
2. Install with "C++ build tools" workload
3. Make sure "MSVC v143" and "Windows 10/11 SDK" are selected

### Option 2: Full Visual Studio
- Install Visual Studio Community/Professional with C++ support

### Option 3: MinGW-w64
- Install MinGW-w64 and add it to your PATH

## How to Run

1. **Build the extension** (do this once):
   ```cmd
   python example_build.py
   ```

2. **Run the example**:
   ```cmd
   python example.py
   ```

3. **Clean up build artifacts** (optional):
   ```cmd
   cleanup.bat          # Windows batch script
   cleanup.ps1          # PowerShell script  
   python cleanup.py    # Cross-platform Python script
   ```

## Cleanup Scripts

Three cleanup options are provided to remove all generated files:

- **`cleanup.bat`** - Windows batch script
- **`cleanup.ps1`** - PowerShell script with detailed progress reporting
- **`cleanup.py`** - Cross-platform Python script with comprehensive cleanup

All scripts remove:
- Compiled extensions (`.pyd` files)
- Generated C source (`_example.c`)
- Build directories (`build/`, `Release/`)
- Visual Studio artifacts (`.obj`, `.lib`, `.exp`, `.pdb`, `.ilk`)
- Python cache files (`__pycache__/`, `*.pyc`)
- Distribution artifacts (`dist/`, `*.egg-info/`)

## What the Example Demonstrates

The example includes three C functions that are significantly faster than Python equivalents:

1. **Array Sum**: Sums all elements in an integer array
2. **Array Multiplication**: Multiplies each element by a factor
3. **Fibonacci**: Calculates Fibonacci numbers iteratively

Each function demonstrates:
- How to pass arrays between Python and C
- Performance benefits of C code
- Proper memory management with CFFI

## Expected Output

When you run `python example.py`, you should see:
- Performance comparisons between C and Python implementations
- Verification that results are correct
- Speedup measurements showing C performance benefits

## Build Output

The build process creates:
- `_example.cp312-win_amd64.pyd`: The compiled extension (filename may vary based on Python version)
- `build/` directory with intermediate files
- `_example.c`: Generated C source file

## Troubleshooting

**Import Error**: If you get an import error when running `example.py`, make sure you've run `example_build.py` first.

**Build Error**: If the build fails:
1. Verify you have a C compiler installed
2. Make sure Python development headers are available
3. Check that cffi is installed: `pip install cffi`

**Performance**: The C functions should be significantly faster than Python equivalents, especially for larger data sets.
