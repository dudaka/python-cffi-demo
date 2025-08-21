#!/usr/bin/env python3
"""
Clean CFFI API Mode Example for Windows
Minimal demonstration of key features without verbose output.
"""

from _example import ffi, lib
import os

def main():
    # Get current time
    time_ptr = lib.get_current_time_string()
    current_time = ffi.string(time_ptr).decode('utf-8')
    lib.free_string(time_ptr)
    print(f"Time: {current_time}")
    
    # Get temp directory  
    temp_ptr = lib.get_temp_path()
    temp_dir = ffi.string(temp_ptr).decode('utf-8')
    lib.free_string(temp_ptr)
    print(f"Temp: {temp_dir}")
    
    # File operations
    with open("sample.txt", "w") as f:
        f.write("Hello CFFI")
    
    file_size = lib.get_file_size(b"sample.txt")
    print(f"File size: {file_size} bytes")
    os.remove("sample.txt")
    
    # Memory operations
    text = "Hello from C"
    buffer = lib.malloc(len(text) + 1)
    char_buf = ffi.cast("char*", buffer)
    lib.strcpy(char_buf, text.encode('utf-8'))
    result = ffi.string(char_buf).decode('utf-8')
    lib.free(buffer)
    print(f"Memory test: {result}")

if __name__ == "__main__":
    main()
