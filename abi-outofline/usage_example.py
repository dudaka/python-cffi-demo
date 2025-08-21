"""
Out-of-line ABI mode example - Usage script
This script demonstrates how to use the generated FFI module.
"""

import sys
import ctypes.util
from _simple_example import ffi

def main():
    print("=== Out-of-line ABI Mode Example ===\n")
    
    # Method 1: Open the C runtime library on Windows
    print("1. Using C runtime library:")
    try:
        # Find and load the C runtime library
        c_lib_name = ctypes.util.find_library("c")
        if c_lib_name:
            lib_c = ffi.dlopen(c_lib_name)
            print(f"   Loaded C library: {c_lib_name}")
        else:
            # Fallback for Windows - try msvcrt
            lib_c = ffi.dlopen("msvcrt.dll")
            print("   Loaded msvcrt.dll")
            
        # Use printf function
        lib_c.printf(b"   Hello from printf! Number: %d\n", ffi.cast("int", 42))
        
        # Use puts function
        lib_c.puts(b"   Hello from puts!")
        
        # Use getenv function
        env_var = lib_c.getenv(b"PATH")
        if env_var != ffi.NULL:
            path_str = ffi.string(env_var).decode('utf-8', errors='ignore')
            print(f"   PATH environment variable length: {len(path_str)} characters")
        else:
            print("   PATH environment variable not found")
            
    except Exception as e:
        print(f"   Error loading C library: {e}")
    
    print()
    
    # Method 2: Use Windows-specific functions
    print("2. Using Windows kernel32.dll:")
    try:
        kernel32 = ffi.dlopen("kernel32.dll")
        print("   Loaded kernel32.dll")
        
        # Get standard output handle
        STD_OUTPUT_HANDLE = ffi.cast("DWORD", -11)
        stdout_handle = kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        
        if stdout_handle != ffi.NULL:
            print(f"   Got stdout handle: {stdout_handle}")
            
            # Try to set console color (this might not work in all terminals)
            try:
                # Set text to bright green (color code 10)
                kernel32.SetConsoleTextAttribute(stdout_handle, 10)
                print("   This text should be green!")
                # Reset to default color (color code 7)
                kernel32.SetConsoleTextAttribute(stdout_handle, 7)
            except:
                print("   Color change not supported in this terminal")
        else:
            print("   Could not get stdout handle")
            
    except Exception as e:
        print(f"   Error using Windows functions: {e}")
    
    print()
    print("=== Example completed successfully! ===")

if __name__ == "__main__":
    main()
