#!/usr/bin/env python3
"""
Test script for the Windows-compatible CFFI API example.
This script demonstrates how to use the compiled extension module.
"""

import os
import tempfile

# Import the compiled module
try:
    from _example import ffi, lib
    print("✓ Successfully imported _example module")
except ImportError as e:
    print(f"✗ Failed to import _example module: {e}")
    print("Make sure to run 'python example_build.py' first to compile the module.")
    exit(1)

def main():
    print("=== CFFI API Mode Example for Windows ===\n")
    
    # Test 1: Get current time
    print("1. Testing get_current_time_string():")
    time_ptr = lib.get_current_time_string()
    if time_ptr != ffi.NULL:
        time_str = ffi.string(time_ptr).decode('utf-8')
        print(f"   Current time: {time_str}")
        lib.free_string(time_ptr)  # Clean up memory
    else:
        print("   Failed to get current time")
    
    # Test 2: Get temporary directory path
    print("\n2. Testing get_temp_path():")
    temp_ptr = lib.get_temp_path()
    if temp_ptr != ffi.NULL:
        temp_path = ffi.string(temp_ptr).decode('utf-8')
        print(f"   Temporary directory: {temp_path}")
        lib.free_string(temp_ptr)  # Clean up memory
    else:
        print("   Failed to get temporary directory")
    
    # Test 3: Create a test file and check its size
    print("\n3. Testing get_file_size():")
    test_filename = "test_file.txt"
    test_content = "Hello, CFFI on Windows!\nThis is a test file.\n"
    
    # Create test file with binary mode to control line endings
    with open(test_filename, 'wb') as f:
        f.write(test_content.encode('utf-8'))
    
    # Get actual file size
    import os
    actual_size = os.path.getsize(test_filename)
    
    # Get file size using our C function
    file_size = lib.get_file_size(test_filename.encode('utf-8'))
    
    print(f"   Created test file: {test_filename}")
    print(f"   File size from C function: {file_size} bytes")
    print(f"   Actual file size: {actual_size} bytes")
    
    if file_size == actual_size:
        print("   ✓ File size matches!")
    else:
        print("   ✗ File size mismatch!")
    
    # Clean up test file
    try:
        os.remove(test_filename)
        print(f"   Cleaned up test file: {test_filename}")
    except OSError:
        pass
    
    # Test 4: Test direct C standard library functions
    print("\n4. Testing direct C standard library calls:")
    
    # Allocate memory and copy string
    test_string = "Hello from C!"
    string_len = len(test_string)
    
    # Allocate memory
    buffer = lib.malloc(string_len + 1)
    if buffer != ffi.NULL:
        # Cast to char* for string operations
        char_buffer = ffi.cast("char*", buffer)
        
        # Copy string
        lib.strcpy(char_buffer, test_string.encode('utf-8'))
        
        # Read it back
        result = ffi.string(char_buffer).decode('utf-8')
        print(f"   Original: {test_string}")
        print(f"   From C buffer: {result}")
        
        # Check length
        c_length = lib.strlen(char_buffer)
        print(f"   String length from C: {c_length}")
        
        # Free memory
        lib.free(buffer)
        print("   ✓ Memory allocated, used, and freed successfully!")
    else:
        print("   ✗ Failed to allocate memory")
    
    print("\n=== All tests completed ===")

if __name__ == "__main__":
    main()
