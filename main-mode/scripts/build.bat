@echo off
REM CMake build script for Pi Approximation CFFI Demo
REM This script configures and builds the project using CMake

echo Building Pi Approximation CFFI Demo with CMake
echo =============================================

REM Check if CMake is available
cmake --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: CMake is not installed or not in PATH
    echo Please install CMake from https://cmake.org/download/
    pause
    exit /b 1
)

REM Create build directory if it doesn't exist
if not exist "build" mkdir build
cd build

REM Configure the project
echo.
echo Step 1: Configuring CMake project...
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIB=ON -DBUILD_PYTHON_EXTENSION=ON

if errorlevel 1 (
    echo ERROR: CMake configuration failed
    pause
    exit /b 1
)

REM Build the project
echo.
echo Step 2: Building the project...
cmake --build . --config Release

if errorlevel 1 (
    echo ERROR: Build failed
    pause
    exit /b 1
)

echo.
echo Build completed successfully!
echo.
echo Available targets:
echo - piapprox.dll (shared library)
echo - Python CFFI extension (use: cmake --build . --target python_extension)
echo - Test Python extension (use: cmake --build . --target test_python)

pause
