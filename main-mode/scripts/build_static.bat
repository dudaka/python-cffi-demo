@echo off
REM Build static library version
echo Building Pi Approximation as Static Library
echo ==========================================

if not exist "build" mkdir build
cd build

echo Configuring for static library build...
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIB=OFF -DBUILD_PYTHON_EXTENSION=ON

if errorlevel 1 (
    echo ERROR: CMake configuration failed
    pause
    exit /b 1
)

echo Building static library...
cmake --build . --config Release

if errorlevel 1 (
    echo ERROR: Build failed
    pause
    exit /b 1
)

echo Static library build completed!
pause
