@echo off
echo Cleaning up generated CFFI files...

if exist "_pi.c" (
    echo Deleting _pi.c
    del "_pi.c"
)

if exist "_pi.*.pyd" (
    echo Deleting _pi.*.pyd
    del "_pi.*.pyd"
)

if exist "__pycache__" (
    echo Deleting __pycache__ directory
    rmdir /s /q "__pycache__"
)

for /d %%i in (build_*) do (
    if exist "%%i" (
        echo Deleting build directory %%i
        rmdir /s /q "%%i"
    )
)

if exist "build" (
    echo Deleting build directory
    rmdir /s /q "build"
)

echo Cleanup complete!
