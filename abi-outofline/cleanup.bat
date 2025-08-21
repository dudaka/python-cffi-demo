@echo off
REM Cleanup script for out-of-line ABI example

echo Cleaning up generated files...

REM Remove generated FFI module
if exist "_simple_example.py" (
    del "_simple_example.py"
    echo Deleted _simple_example.py
)

REM Remove Python cache directories
if exist "__pycache__" (
    rmdir /s /q "__pycache__"
    echo Deleted __pycache__ directory
)

REM Remove setuptools build directory
if exist "build" (
    rmdir /s /q "build"
    echo Deleted build directory
)

REM Remove distribution directory
if exist "dist" (
    rmdir /s /q "dist"
    echo Deleted dist directory
)

REM Remove egg-info directory
for /d %%i in (*.egg-info) do (
    if exist "%%i" (
        rmdir /s /q "%%i"
        echo Deleted %%i directory
    )
)

REM Remove compiled Python files
if exist "*.pyc" (
    del "*.pyc"
    echo Deleted .pyc files
)

REM Remove wheel build artifacts
if exist "*.egg-info" (
    del "*.egg-info"
    echo Deleted .egg-info files
)

REM Remove any temporary setup files
if exist "setup.cfg" (
    del "setup.cfg"
    echo Deleted setup.cfg
)

echo Cleanup complete!
