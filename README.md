"# Python CFFI Demo Collection

A comprehensive collection of examples demonstrating Python's **CFFI (C Foreign Function Interface)** library across different modes and use cases. This repository provides practical, working examples for each CFFI mode with Windows-specific implementations and cross-platform compatibility.

## 🎯 Overview

CFFI provides multiple ways to interface with C code from Python. This collection demonstrates:

- **ABI Mode**: Direct interface with existing compiled libraries (no C compiler needed)
- **API Mode**: Compile C code with Python integration (requires C compiler)
- **Inline vs Out-of-line**: Different approaches to defining the interface
- **Distribution**: How to package and distribute CFFI-based projects

## 📁 Repository Structure

```
python-cffi-demo/
├── abi-inline/              # ABI mode with inline definitions
├── abi-outofline/           # ABI mode with separate build script
├── api-c-sources/           # API mode with custom C sources
├── api-c-standard-library/  # API mode with standard C library
├── api-outofline/           # API mode with separate build script
├── main-mode/               # Main mode for direct execution
└── README.md               # This file
```

## 🔧 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dudaka/python-cffi-demo.git
   cd python-cffi-demo
   ```

2. **Install CFFI:**
   ```bash
   pip install cffi
   ```

3. **Choose a demo and follow its README:**
   Each directory contains its own README.md with specific instructions.

## 📋 Demo Descriptions

### 🟦 ABI Mode Examples

**ABI (Application Binary Interface) Mode** - Interface with existing compiled libraries without needing a C compiler at runtime.

#### `abi-outofline/` - Out-of-line ABI Mode ⭐ **Recommended**
- **What it demonstrates:** Pre-compiled FFI interface for better performance
- **Key features:**
  - Setuptools integration with `cffi_modules`
  - Windows-specific library loading (msvcrt.dll, kernel32.dll)
  - Complete packaging solution with setup.py
  - Multiple cleanup scripts (batch, PowerShell, Python)
  - Console color output using Windows API
- **Best for:** Production applications needing fast import times
- **Files:** Build script, usage example, comprehensive tests, distribution setup

#### `abi-inline/`
- **What it demonstrates:** Basic ABI mode concepts
- **Key features:** Jupyter notebook with inline examples
- **Best for:** Learning and experimentation
- **Files:** Interactive notebook

### 🟩 API Mode Examples

**API Mode** - Compile C code together with Python, providing better integration and performance.

#### `api-c-sources/` - Custom C Sources
- **What it demonstrates:** Building Python extensions from custom C code
- **Key features:**
  - Pi calculation using Leibniz formula
  - Custom C source compilation
  - Mathematical computation examples
- **Best for:** Projects with custom mathematical or computational C code
- **Files:** C sources, Python wrapper, build scripts

#### `api-c-standard-library/` - Standard Library Integration
- **What it demonstrates:** Interfacing with standard C library functions
- **Key features:**
  - Multiple demo complexity levels (minimal, simple, comprehensive)
  - Cross-platform C library access
  - Error handling and edge cases
- **Best for:** Learning API mode fundamentals
- **Files:** Progressive examples from minimal to comprehensive

#### `api-outofline/` - Out-of-line API Mode
- **What it demonstrates:** Separate build process for API mode
- **Key features:**
  - Build-time compilation
  - Modular development approach
- **Best for:** Larger projects with complex C integration
- **Files:** Separate build and usage scripts

### 🟨 Special Modes

#### `main-mode/` - Main Mode Execution
- **What it demonstrates:** Direct execution of CFFI code
- **Key features:** 
  - Mathematical computations (Pi approximation)
  - Direct C integration
- **Best for:** Simple scripts and direct execution scenarios
- **Files:** Self-contained examples

## 🚀 Usage Examples

### Basic ABI Mode (Recommended Start)
```bash
cd abi-outofline
python simple_example_build.py  # Build the FFI module
python usage_example.py         # Run the example
```

### API Mode with Custom C Code
```bash
cd api-c-sources
python pi_extension_build.py    # Build the extension
python usage_example.py         # Run Pi calculation
```

### Standard Library Integration
```bash
cd api-c-standard-library
python minimal_example.py       # Start with basics
python comprehensive_demo.py    # Advanced features
```

## 🛠️ Requirements

**⚠️ Currently Windows Only**: These examples have been developed and tested on Windows. Cross-platform compatibility testing for Linux and macOS is planned for future releases.

### Windows Requirements:
- **Python 3.7+**
- **CFFI 1.0.0+** (`pip install cffi`)
- **C Compiler** (for API mode examples):
  - **Recommended**: Visual Studio Build Tools 2019 or newer
  - **Alternative**: Visual Studio Community/Professional with C++ support
  - **Alternative**: MinGW-w64 (may require additional configuration)

### Future Platform Support:
- **Linux**: Planned (will require GCC and testing)
- **macOS**: Planned (will require Xcode Command Line Tools and testing)

**Note**: While CFFI itself is cross-platform, these specific examples use Windows-specific libraries (msvcrt.dll, kernel32.dll) and have Windows-specific build configurations that will need adaptation for other platforms.

## 🏗️ Building and Distribution

The `abi-outofline` example demonstrates complete packaging:

```bash
cd abi-outofline
python setup.py build          # Build package
python setup.py sdist          # Create source distribution
python setup.py bdist_wheel    # Create wheel distribution
pip install .                  # Install locally
```

## 🧹 Cleanup

Each demo includes cleanup scripts to remove generated files:

```bash
# Windows
cleanup.bat

# Cross-platform
python cleanup.py
```

## 🔍 Key Concepts Demonstrated

| Concept | Examples | Description |
|---------|----------|-------------|
| **ABI vs API Mode** | All directories | Different approaches to C integration |
| **Inline vs Out-of-line** | abi-inline vs abi-outofline | Interface definition strategies |
| **Library Loading** | abi-outofline | Platform-specific library access |
| **Custom C Sources** | api-c-sources | Compiling custom C code |
| **Standard Library** | api-c-standard-library | Using existing C libraries |
| **Packaging** | abi-outofline | Distribution and setup.py integration |
| **Testing** | Multiple examples | Unit tests and validation |
| **Cleanup** | All directories | Managing generated files |

## 🌟 Recommended Learning Path

1. **Start with:** `api-c-standard-library/minimal_example.py` - Learn basics
2. **Progress to:** `abi-outofline/` - Understand production patterns
3. **Explore:** `api-c-sources/` - Custom C integration
4. **Advanced:** `abi-outofline/setup.py` - Distribution and packaging

## 🐛 Troubleshooting

### Common Issues

**"No module named '_example'"**
- Run the build script first (e.g., `python simple_example_build.py`)

**"Microsoft Visual C++ 14.0 is required"** (Windows)
- Install Visual Studio Build Tools or use Windows SDK

**Library not found errors**
- Check platform-specific library names in the code
- Ensure required libraries are installed on your system

### Platform-Specific Notes

**Windows (Currently Supported):**
- Uses `msvcrt.dll` for C runtime functions
- Demonstrates Windows API calls (kernel32.dll)
- Includes batch file and PowerShell cleanup scripts
- Tested with Visual Studio Build Tools
- All examples verified to work on Windows 10/11

**Linux/macOS (Future Support Planned):**
- Will require adaptation for standard C library loading
- Different library file extensions (.so vs .dll)
- Shell script cleanup equivalents will be provided
- Build system configurations will need platform-specific adjustments
- Library loading mechanisms may need updates for different platforms

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new examples
4. Update documentation
5. Submit a pull request

## 📚 Further Reading

- [CFFI Documentation](https://cffi.readthedocs.io/)
- [Python C API](https://docs.python.org/3/extending/)
- [Setuptools Integration](https://setuptools.pypa.io/)

## 📄 License

This project is licensed under the MIT License - see individual demo directories for specific details.

## 🏷️ Tags

`python` `cffi` `c-extension` `ffi` `windows` `windows-api` `api` `abi` `setuptools` `packaging` `visual-studio`
