#!/usr/bin/env python3
"""
Minimal CFFI API Example - Windows
Shows the basic pattern for using CFFI API mode.
"""

# Import the compiled module
from _example import ffi, lib

# Use C functions
time_ptr = lib.get_current_time_string()
time_str = ffi.string(time_ptr).decode('utf-8')
lib.free_string(time_ptr)

print(f"Current time: {time_str}")

# Memory management
buffer = lib.malloc(20)
char_buf = ffi.cast("char*", buffer) 
lib.strcpy(char_buf, b"Hello CFFI!")
result = ffi.string(char_buf)
lib.free(buffer)

print(f"Result: {result.decode('utf-8')}")
