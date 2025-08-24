@echo off
echo Cleaning up DLL build artifacts...

:: Remove compiled files
if exist *.obj del *.obj
if exist *.dll del *.dll
if exist *.lib del *.lib
if exist *.exp del *.exp

:: Remove Python CFFI generated files
if exist _pi_cffi_dll.c del _pi_cffi_dll.c
if exist _pi_cffi_dll.*.pyd del _pi_cffi_dll.*.pyd

:: Remove Python cache
if exist __pycache__ rmdir /s /q __pycache__

echo Cleanup complete!
