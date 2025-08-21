@echo off
REM Clean script to remove all CFFI generated files and build artifacts
REM Run this to clean up after building the CFFI extension

echo Cleaning CFFI build artifacts...

REM Remove compiled extension modules
if exist "_example.pyd" (
    del "_example.pyd"
    echo Deleted _example.pyd
)

if exist "_example.cp*.pyd" (
    del "_example.cp*.pyd"
    echo Deleted _example.cp*.pyd
)

REM Remove generated C source
if exist "_example.c" (
    del "_example.c"
    echo Deleted _example.c
)

REM Remove build directory
if exist "build" (
    rmdir /s /q "build"
    echo Deleted build directory
)

REM Remove Release directory artifacts
if exist "Release" (
    rmdir /s /q "Release"
    echo Deleted Release directory
)

REM Remove any test files that might be left behind
if exist "test_file.txt" (
    del "test_file.txt"
    echo Deleted test_file.txt
)

if exist "demo.txt" (
    del "demo.txt"
    echo Deleted demo.txt
)

if exist "sample.txt" (
    del "sample.txt"
    echo Deleted sample.txt
)

if exist "small.txt" (
    del "small.txt"
    echo Deleted small.txt
)

if exist "medium.txt" (
    del "medium.txt"
    echo Deleted medium.txt
)

if exist "empty.txt" (
    del "empty.txt"
    echo Deleted empty.txt
)

REM Remove Python cache
if exist "__pycache__" (
    rmdir /s /q "__pycache__"
    echo Deleted __pycache__ directory
)

REM Remove any .pyc files
if exist "*.pyc" (
    del "*.pyc"
    echo Deleted .pyc files
)

REM Remove egg-info if it exists
if exist "*.egg-info" (
    rmdir /s /q "*.egg-info"
    echo Deleted egg-info directory
)

echo.
echo Cleanup completed!
echo.
echo Remaining files:
dir *.py *.md *.bat 2>nul
