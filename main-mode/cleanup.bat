@echo off
echo Cleaning up build output files and directories...
echo.

REM Delete object files
if exist pi.obj (
    echo Deleting pi.obj...
    del pi.obj
)

REM Delete static library
if exist piapprox.lib (
    echo Deleting piapprox.lib...
    del piapprox.lib
)

REM Delete DLL files
if exist piapprox.dll (
    echo Deleting piapprox.dll...
    del piapprox.dll
)

REM Delete generated CFFI C file
if exist _pi_cffi.c (
    echo Deleting _pi_cffi.c...
    del _pi_cffi.c
)

REM Delete Python extension modules (*.pyd files)
for %%f in (_pi_cffi.*.pyd) do (
    if exist "%%f" (
        echo Deleting %%f...
        del "%%f"
    )
)

REM Also check for .pyd without version suffix
if exist _pi_cffi.pyd (
    echo Deleting _pi_cffi.pyd...
    del _pi_cffi.pyd
)

REM Delete import library files
for %%f in (_pi_cffi.*.lib) do (
    if exist "%%f" (
        echo Deleting %%f...
        del "%%f"
    )
)

REM Delete build directories
if exist build (
    echo Deleting build directory...
    rmdir /s /q build
)

if exist Release (
    echo Deleting Release directory...
    rmdir /s /q Release
)

if exist __pycache__ (
    echo Deleting __pycache__ directory...
    rmdir /s /q __pycache__
)

REM Delete distribution directories (setuptools)
if exist dist (
    echo Deleting dist directory...
    rmdir /s /q dist
)

if exist *.egg-info (
    echo Deleting .egg-info directories...
    for /d %%d in (*.egg-info) do rmdir /s /q "%%d"
)

REM Delete temporary files
if exist *.exp (
    echo Deleting export files...
    del *.exp
)

if exist *.ilk (
    echo Deleting incremental linker files...
    del *.ilk
)

if exist *.pdb (
    echo Deleting debug files...
    del *.pdb
)

if exist *.manifest (
    echo Deleting manifest files...
    del *.manifest
)

echo.
echo Cleanup completed!
echo.
pause
