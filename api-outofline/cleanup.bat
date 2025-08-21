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
