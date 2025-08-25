#!/bin/bash
# CMake build script for Pi Approximation CFFI Demo (Linux/macOS)

echo "Building Pi Approximation CFFI Demo with CMake"
echo "=============================================="

# Check if CMake is available
if ! command -v cmake &> /dev/null; then
    echo "ERROR: CMake is not installed"
    echo "Please install CMake using your package manager"
    exit 1
fi

# Create build directory if it doesn't exist
mkdir -p build
cd build

# Configure the project
echo
echo "Step 1: Configuring CMake project..."
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIB=ON -DBUILD_PYTHON_EXTENSION=ON

if [ $? -ne 0 ]; then
    echo "ERROR: CMake configuration failed"
    exit 1
fi

# Build the project
echo
echo "Step 2: Building the project..."
cmake --build . --config Release

if [ $? -ne 0 ]; then
    echo "ERROR: Build failed"
    exit 1
fi

echo
echo "Build completed successfully!"
echo
echo "Available targets:"
echo "- libpiapprox.so (shared library)"
echo "- Python CFFI extension (use: cmake --build . --target python_extension)"
echo "- Test Python extension (use: cmake --build . --target test_python)"
