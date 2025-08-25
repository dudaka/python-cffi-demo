# Pi Approximation CFFI Demo - CMake Edition

This project demonstrates how to use Python CFFI (C Foreign Function Interface) with CMake build system to create Python extensions from C code. The example implements a Monte Carlo method to approximate the value of Pi.

## Project Structure

```
main-mode/
├── .gitignore               # Git ignore file for build artifacts
├── CMakeLists.txt           # Main CMake configuration
├── README_CMAKE.md          # This file
├── include/                 # Header files
│   ├── pi.h                # Standard C header
│   └── pi_dll.h            # DLL-enabled header with export macros
├── src/                    # C source files
│   ├── pi.c                # Standard implementation
│   └── pi_dll.c            # DLL implementation with export declarations
├── python/                 # Python CFFI build scripts and tests
│   ├── piapprox_build.py   # CFFI build script for static library
│   ├── piapprox_build_dll.py # CFFI build script for shared library
│   ├── test.py             # Test script for static version
│   └── test_dll.py         # Test script for DLL version
├── scripts/                # Build automation scripts
│   ├── build.bat           # Windows build script
│   ├── build.sh            # Linux/macOS build script
│   ├── build_static.bat    # Windows static library build
│   └── clean.bat           # Cleanup script
├── build/                  # Build output directory (created by CMake)
└── legacy/                 # Original files (moved for reference)
```

## Prerequisites

### Required:
- CMake 3.15 or higher
- Python 3.x with CFFI installed (`pip install cffi`)
- C compiler (Visual Studio 2019/2022 on Windows, GCC/Clang on Linux/macOS)

### Windows-specific:
- Microsoft Visual Studio 2019/2022 (Community edition or higher) with C++ build tools
- Or Microsoft Visual Studio Build Tools
- Or MinGW-w64 with GCC

### Linux/macOS:
- GCC or Clang compiler
- Development libraries (build-essential on Ubuntu, Xcode Command Line Tools on macOS)

## Quick Start

### Windows

1. **Easy Build (Recommended)**:
   ```cmd
   cd scripts
   build.bat
   ```

2. **Manual CMake Build**:
   ```cmd
   mkdir build
   cd build
   cmake .. -DCMAKE_BUILD_TYPE=Release
   cmake --build . --config Release
   ```

### Linux/macOS

1. **Easy Build**:
   ```bash
   cd scripts
   chmod +x build.sh
   ./build.sh
   ```

2. **Manual CMake Build**:
   ```bash
   mkdir build
   cd build
   cmake .. -DCMAKE_BUILD_TYPE=Release
   cmake --build .
   ```

## Build Options

CMake provides several build options that can be configured:

```bash
# Build as shared library (DLL on Windows)
cmake .. -DBUILD_SHARED_LIB=ON

# Build as static library
cmake .. -DBUILD_SHARED_LIB=OFF

# Enable Python extension building
cmake .. -DBUILD_PYTHON_EXTENSION=ON

# Set build type
cmake .. -DCMAKE_BUILD_TYPE=Release        # Optimized build
cmake .. -DCMAKE_BUILD_TYPE=Debug          # Debug build with symbols
```

## Available Targets

After configuring with CMake, you can build specific targets:

```bash
# Build the C library only
cmake --build . --target piapprox

# Build Python CFFI extension
cmake --build . --target python_extension

# Run Python tests
cmake --build . --target test_python

# Clean all build files
cmake --build . --target clean_all
```

## Testing

### Test the C Library Directly
The CMake build creates either a static library (`piapprox.lib`) or shared library (`piapprox.dll` on Windows, `libpiapprox.so` on Linux).

### Test the Python Extension

1. **Using CMake target (Recommended)**:
   ```bash
   cmake --build . --target test_python
   ```

2. **Manual testing**:
   ```bash
   cd build
   python ../python/test.py        # For static library version
   python ../python/test_dll.py    # For DLL version
   ```

**Note**: The Python scripts automatically detect the correct module path, so they work from the build directory.

## Development Workflow

1. **Make changes to C code** in `src/` directory
2. **Update headers** in `include/` directory if needed
3. **Rebuild**:
   ```bash
   cd build
   cmake --build .
   ```
4. **Test changes**:
   ```bash
   cmake --build . --target test_python
   ```

## CMake Features

This CMake configuration provides:

- **Cross-platform builds**: Works on Windows, Linux, and macOS
- **Multiple build types**: Debug, Release, MinSizeRel, RelWithDebInfo
- **Flexible library types**: Static or shared libraries
- **Automatic Python integration**: Builds and tests Python extensions
- **Clean build environment**: Separate build directory keeps source clean
- **Install support**: Can install libraries and headers system-wide

## Troubleshooting

### Python Extension Import Errors
If you get import errors when running Python tests:
1. Make sure the C library was built successfully
2. Check that the library is in the Python search path
3. Verify CFFI found the correct library during compilation

### CMake Configuration Errors
- Ensure CMake version is 3.15 or higher
- Check that a C compiler is available and in PATH
- On Windows, make sure Visual Studio or Build Tools are installed

### Build Errors
- Check that all required dependencies are installed
- Verify the compiler can find the header files
- Look at detailed error messages in the CMake output

## Comparison with Legacy Build

| Feature | Legacy (batch files) | CMake |
|---------|---------------------|--------|
| Cross-platform | Windows only | Windows/Linux/macOS |
| Build types | Release only | Debug/Release/etc |
| Dependency tracking | Manual | Automatic |
| Parallel builds | No | Yes |
| IDE integration | Limited | Full support |
| Install support | No | Yes |
| Clean builds | Manual scripts | Built-in |

## Next Steps

- **Add more C functions** to the library
- **Create unit tests** for the C code
- **Add packaging** with CPack
- **Set up continuous integration** with GitHub Actions
- **Add documentation** generation with Doxygen
