@echo off
echo Building Pi Approximation as Shared Library (DLL)
echo =================================================

echo.
echo Step 1: Set up Visual Studio Environment
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

echo.
echo Step 2: Compile C source to object file
cl /c lib\pi_dll.c /I include

echo.
echo Step 3: Create DLL (shared library)
cl /LD pi_dll.obj /Fe:piapprox.dll

echo.
echo Step 4: Build Python CFFI extension that links to the DLL
python piapprox_build_dll.py

echo.
echo Step 5: Test the extension
python test_dll.py

pause
