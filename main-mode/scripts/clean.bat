@echo off
REM Clean all build artifacts
echo Cleaning all build artifacts...
echo ==============================

if exist "build" (
    echo Removing build directory...
    rmdir /s /q build
)

if exist "*.dll" del /q *.dll
if exist "*.lib" del /q *.lib
if exist "*.obj" del /q *.obj
if exist "*.exp" del /q *.exp
if exist "*.pdb" del /q *.pdb

REM Clean Python build artifacts
if exist "python\*.pyd" del /q python\*.pyd
if exist "python\*.dll" del /q python\*.dll
if exist "python\*.so" del /q python\*.so
if exist "python\__pycache__" rmdir /s /q python\__pycache__

echo Cleanup completed!
pause
