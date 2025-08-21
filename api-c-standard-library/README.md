# CFFI API Mode Example for Windows

This example demonstrates how to use CFFI in API mode on Windows, calling C standard library functions and custom wrapper functions.

## Features

This example shows how to:
- Use C standard library functions (`malloc`, `free`, `strcpy`, `strlen`)
- Create custom C wrapper functions
- Handle Windows-specific APIs (getting temp directory path)
- Work with strings and memory management between Python and C
- Get current time using C time functions
- Check file sizes using C file I/O

## Files

- `example_build.py` - CFFI builder script that generates the extension module
- `test_example.py` - Python script demonstrating usage of the compiled module
- `setup.py` - Setuptools integration for distribution
- `clean_demo.py` - Clean, minimal usage example
- `simple_demo.py` - Basic demonstration script
- `comprehensive_demo.py` - Full-featured demonstration with all features
- `cleanup.bat` - Windows batch script to clean build artifacts
- `cleanup.ps1` - PowerShell script to clean build artifacts  
- `cleanup.py` - Cross-platform Python script to clean build artifacts
- `README.md` - This file

## Requirements

- Python 3.6+
- CFFI library (`pip install cffi`)
- A C compiler (Visual Studio Build Tools, MinGW, or similar)

## Quick Start

### Method 1: Direct compilation

1. Install CFFI:
   ```cmd
   pip install cffi
   ```

2. Compile the extension module:
   ```cmd
   python example_build.py
   ```

3. Run the test script:
   ```cmd
   python test_example.py
   ```

### Method 2: Using setuptools

1. Install in development mode:
   ```cmd
   pip install -e .
   ```

2. Run the test script:
   ```cmd
   python test_example.py
   ```

## What happens when you run example_build.py?

1. CFFI generates C source code that bridges Python and C
2. The C compiler compiles this into an extension module (`.pyd` file on Windows)
3. The module exports `ffi` and `lib` objects for use in Python

## Key Differences from Unix Examples

- Uses Windows-compatible headers (`windows.h` instead of `pwd.h`)
- Includes cross-platform code that works on both Windows and Unix
- Uses `GetTempPathA()` Windows API function for getting temp directory
- Handles memory management properly with custom wrapper functions

## C Functions Available

- `get_current_time_string()` - Returns current time as string
- `get_file_size(filename)` - Returns size of a file in bytes
- `get_temp_path()` - Returns system temporary directory path
- `free_string(str)` - Frees memory allocated for strings
- Standard C library functions: `malloc`, `free`, `strcpy`, `strlen`

## Memory Management

The example demonstrates proper memory management:
- Custom functions that allocate memory return pointers
- Python code must call `free_string()` or `free()` to clean up
- The `ffi.string()` function copies C strings to Python strings safely

## Error Handling

The example includes basic error handling:
- File operations return -1 on error
- Memory allocation is checked for NULL pointers
- Cross-platform compatibility is maintained with `#ifdef` preprocessor directives

## Cleaning Up

To remove all generated files and build artifacts, use one of the cleanup scripts:

### Windows Batch Script
```cmd
cleanup.bat
```

### PowerShell Script
```powershell
.\cleanup.ps1
```

### Cross-platform Python Script
```cmd
python cleanup.py
```

All cleanup scripts remove:
- Compiled extension modules (`.pyd`, `.so` files)
- Generated C source files
- Build directories (`build`, `Release`)
- Test files and Python cache

## Extending the Example

You can easily extend this example by:
1. Adding more C functions to the `set_source()` call
2. Declaring them in the `cdef()` section
3. Using them in your Python code via the `lib` object

The API mode is more portable than ABI mode because it doesn't depend on exact C struct layouts or calling conventions.
