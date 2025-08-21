@echo off
echo Cleaning up CFFI build artifacts...

REM Remove compiled extension files
if exist "_example*.pyd" (
    del "_example*.pyd"
    echo Removed .pyd files
)

REM Remove generated C source
if exist "_example.c" (
    del "_example.c"
    echo Removed generated C source
)

REM Remove build directory
if exist "build" (
    rmdir /s /q "build"
    echo Removed build directory
)

REM Remove Release directory and all contents
if exist "Release" (
    rmdir /s /q "Release"
    echo Removed Release directory
)

REM Remove Visual Studio build artifacts
if exist "*.exp" (
    del "*.exp"
    echo Removed .exp files
)

if exist "*.lib" (
    del "*.lib"
    echo Removed .lib files
)

if exist "*.obj" (
    del "*.obj"
    echo Removed .obj files
)

if exist "*.pdb" (
    del "*.pdb"
    echo Removed .pdb files
)

if exist "*.ilk" (
    del "*.ilk"
    echo Removed .ilk files
)

REM Remove setuptools/distutils artifacts
if exist "dist" (
    rmdir /s /q "dist"
    echo Removed dist directory
)

for /d %%i in (*.egg-info) do (
    if exist "%%i" (
        rmdir /s /q "%%i"
        echo Removed %%i directory
    )
)

REM Remove __pycache__ directories
if exist "__pycache__" (
    rmdir /s /q "__pycache__"
    echo Removed __pycache__
)

REM Remove .pyc files
for /r %%i in (*.pyc) do (
    del "%%i" >nul 2>&1
)

echo Cleanup complete!
