@echo off
echo Comprehensive cleanup of all build artifacts...
echo.

REM Clean current directory
echo Cleaning current directory...
call :cleanup_directory "."

REM Clean parent directory if we're in main-mode
if "%CD:~-9%"=="main-mode" (
    echo Cleaning parent directory...
    call :cleanup_directory ".."
)

echo.
echo All cleanup completed!
echo.
pause
goto :eof

:cleanup_directory
echo Cleaning %~1...
pushd %~1

REM Delete object files
if exist *.obj (
    echo   Deleting object files...
    del *.obj
)

REM Delete static libraries
if exist *.lib (
    echo   Deleting library files...
    del *.lib
)

REM Delete DLL files
if exist *.dll (
    echo   Deleting DLL files...
    del *.dll
)

REM Delete generated CFFI C files
if exist _pi_cffi.c (
    echo   Deleting _pi_cffi.c...
    del _pi_cffi.c
)

REM Delete Python extension modules
for %%f in (_pi_cffi.*.pyd) do (
    if exist "%%f" (
        echo   Deleting %%f...
        del "%%f"
    )
)

REM Also check for .pyd without version suffix
if exist _pi_cffi.pyd (
    echo   Deleting _pi_cffi.pyd...
    del _pi_cffi.pyd
)

REM Delete export files
if exist *.exp (
    echo   Deleting export files...
    del *.exp
)

REM Delete incremental linker files
if exist *.ilk (
    echo   Deleting incremental linker files...
    del *.ilk
)

REM Delete debug files
if exist *.pdb (
    echo   Deleting debug files...
    del *.pdb
)

REM Delete manifest files
if exist *.manifest (
    echo   Deleting manifest files...
    del *.manifest
)

REM Delete build directories
if exist build (
    echo   Deleting build directory...
    rmdir /s /q build
)

if exist Release (
    echo   Deleting Release directory...
    rmdir /s /q Release
)

if exist __pycache__ (
    echo   Deleting __pycache__ directory...
    rmdir /s /q __pycache__
)

REM Delete setuptools distribution directories
if exist dist (
    echo   Deleting dist directory...
    rmdir /s /q dist
)

REM Delete .egg-info directories
for /d %%d in (*.egg-info) do (
    if exist "%%d" (
        echo   Deleting %%d directory...
        rmdir /s /q "%%d"
    )
)

popd
goto :eof
