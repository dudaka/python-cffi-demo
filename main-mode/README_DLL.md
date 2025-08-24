# Pi Approximation CFFI Demo - Shared Library (DLL) Version

This demonstrates how to build the Pi approximation example as a shared library (DLL) that can be used by multiple applications.

## Additional Files for DLL Version

- **`lib/pi_dll.c`**: C source with DLL export declarations
- **`include/pi_dll.h`**: Header with Windows DLL import/export macros
- **`piapprox_build_dll.py`**: CFFI build script for DLL version
- **`test_dll.py`**: Test script for the DLL version
- **`build_dll.bat`**: Automated build script

## Building the Shared Library Version

### Method 1: Using the Batch Script (Recommended)

Simply run the automated build script:

```cmd
build_dll.bat
```

This script will:
1. Set up the Visual Studio environment
2. Compile the C source to object file
3. Create the DLL (piapprox.dll)
4. Build the CFFI Python extension
5. Run the test

### Method 2: Manual Build Steps

#### Step 1: Set up Visual Studio Environment

```cmd
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
```

#### Step 2: Compile C Source to Object File

```cmd
cl /c lib\pi_dll.c
```

#### Step 3: Create Shared Library (DLL)

```cmd
cl /LD pi_dll.obj /Fe:piapprox.dll
```

This creates:
- `piapprox.dll` - The shared library
- `piapprox.lib` - Import library for linking
- `piapprox.exp` - Export file

#### Step 4: Build Python Extension

```cmd
python piapprox_build_dll.py
```

#### Step 5: Test the Extension

```cmd
python test_dll.py
```

## Key Differences from Static Library Version

### 1. DLL Export/Import Declarations

The header file (`pi_dll.h`) includes Windows-specific macros:

```c
#ifdef _WIN32
    #ifdef BUILDING_PI_DLL
        #define PI_API __declspec(dllexport)  // When building the DLL
    #else
        #define PI_API __declspec(dllimport)  // When using the DLL
    #endif
#else
    #define PI_API  // For other platforms
#endif
```

### 2. Compilation Flags

- **Static version**: `cl /c pi.c` then `lib /OUT:piapprox.lib pi.obj`
- **DLL version**: `cl /LD pi_dll.obj /Fe:piapprox.dll`

The `/LD` flag tells the compiler to create a DLL.

### 3. Runtime Behavior

- **Static library**: Code is embedded in the Python extension
- **DLL version**: Python extension loads the DLL at runtime

## Advantages of the DLL Approach

1. **Modularity**: The DLL can be updated independently of Python extensions
2. **Reusability**: Multiple Python modules or applications can use the same DLL
3. **Memory efficiency**: Only one copy of the DLL is loaded in memory
4. **Distribution**: Easier to distribute updates to the C library

## Disadvantages

1. **Deployment complexity**: Must distribute both the Python extension and the DLL
2. **Path dependencies**: The DLL must be in the system PATH or same directory
3. **Version management**: Need to manage DLL versions carefully

## Files Created After Build

- `piapprox.dll` - The shared library containing pi_approx function
- `piapprox.lib` - Import library for linking
- `piapprox.exp` - Export definitions
- `_pi_cffi_dll.*.pyd` - Python extension that uses the DLL
- `pi_dll.obj` - Object file from compilation

## Testing

The DLL version should produce the same results as the static version:

```
Testing Pi Approximation Function (DLL Version)
==================================================
Iterations:     1000 | Pi approx: 3.144000 | Error: 0.002407
Iterations:    10000 | Pi approx: 3.141200 | Error: 0.000393
Iterations:   100000 | Pi approx: 3.141872 | Error: 0.000279
Iterations:  1000000 | Pi approx: 3.141836 | Error: 0.000243
```
