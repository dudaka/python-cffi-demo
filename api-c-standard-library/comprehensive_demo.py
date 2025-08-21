#!/usr/bin/env python3
"""
Comprehensive Windows CFFI Example
Demonstrates all key features of the API mode example.
"""

import os
import sys

def demonstrate_cffi_features():
    """Comprehensive demonstration of CFFI features."""
    
    print("=" * 60)
    print("CFFI API Mode - Windows Example")
    print("=" * 60)
    
    # Try to import the compiled module
    try:
        from _example import ffi, lib
        print("✓ Successfully imported CFFI module '_example'")
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        print("\nTo fix this, run:")
        print("  python example_build.py")
        print("or")
        print("  python setup.py build_ext --inplace")
        return False
    
    print(f"✓ FFI object type: {type(ffi).__name__}")
    print(f"✓ Python version: {sys.version}")
    print()
    
    # Feature 1: Time operations
    print("1. TIME OPERATIONS")
    print("-" * 20)
    time_ptr = lib.get_current_time_string()
    if time_ptr != ffi.NULL:
        current_time = ffi.string(time_ptr).decode('utf-8')
        print(f"   Current system time: {current_time}")
        lib.free_string(time_ptr)
    else:
        print("   Failed to get system time")
    
    # Feature 2: System path operations
    print("\n2. SYSTEM PATH OPERATIONS")
    print("-" * 30)
    temp_ptr = lib.get_temp_path()
    if temp_ptr != ffi.NULL:
        temp_path = ffi.string(temp_ptr).decode('utf-8')
        print(f"   System temp directory: {temp_path}")
        
        # Test if directory exists
        if os.path.exists(temp_path):
            print(f"   ✓ Directory exists and is accessible")
        else:
            print(f"   ✗ Directory not accessible")
        
        lib.free_string(temp_ptr)
    else:
        print("   Failed to get temp directory")
    
    # Feature 3: File I/O operations
    print("\n3. FILE I/O OPERATIONS")
    print("-" * 25)
    
    test_files = [
        ("small.txt", "Small test file"),
        ("medium.txt", "This is a medium-sized test file.\nIt contains multiple lines.\nAnd some additional content."),
        ("empty.txt", "")
    ]
    
    for filename, content in test_files:
        # Create test file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Get size using C function
        c_size = lib.get_file_size(filename.encode('utf-8'))
        py_size = os.path.getsize(filename)
        
        print(f"   File: {filename}")
        print(f"     C function size: {c_size} bytes")
        print(f"     Python size: {py_size} bytes")
        
        if c_size == py_size:
            print(f"     ✓ Sizes match")
        else:
            print(f"     ✗ Size mismatch!")
        
        # Clean up
        os.remove(filename)
    
    # Feature 4: Memory management
    print("\n4. MEMORY MANAGEMENT")
    print("-" * 25)
    
    test_strings = [
        "Hello, World!",
        "CFFI on Windows",
        "Memory management test",
        "Unicode test: héllo wörld! 🌍"
    ]
    
    for test_str in test_strings:
        try:
            # Allocate memory
            buffer_size = len(test_str.encode('utf-8')) + 1
            buffer = lib.malloc(buffer_size)
            
            if buffer == ffi.NULL:
                print(f"   ✗ Failed to allocate {buffer_size} bytes")
                continue
            
            # Cast to char* for string operations
            char_buffer = ffi.cast("char*", buffer)
            
            # Copy string to buffer
            lib.strcpy(char_buffer, test_str.encode('utf-8'))
            
            # Read back
            result = ffi.string(char_buffer).decode('utf-8')
            length = lib.strlen(char_buffer)
            
            print(f"   String: '{test_str}'")
            print(f"     Length: {length} bytes")
            print(f"     Round-trip: {'✓' if result == test_str else '✗'}")
            
            # Free memory
            lib.free(buffer)
            
        except Exception as e:
            print(f"   ✗ Error with '{test_str}': {e}")
    
    # Feature 5: Error handling
    print("\n5. ERROR HANDLING")
    print("-" * 20)
    
    # Test file operations with non-existent file
    nonexistent_size = lib.get_file_size(b"nonexistent_file.txt")
    print(f"   Size of non-existent file: {nonexistent_size}")
    print(f"   ✓ Properly returns -1 for errors" if nonexistent_size == -1 else "   ✗ Error handling failed")
    
    # Test memory allocation edge cases
    try:
        # Allocate zero bytes
        zero_buffer = lib.malloc(0)
        print(f"   malloc(0) result: {'NULL' if zero_buffer == ffi.NULL else 'non-NULL'}")
        if zero_buffer != ffi.NULL:
            lib.free(zero_buffer)
    except:
        print("   malloc(0) caused exception")
    
    print("\n" + "=" * 60)
    print("COMPREHENSIVE TEST COMPLETED")
    print("=" * 60)
    
    return True

def show_usage_examples():
    """Show common usage patterns."""
    
    print("\nCOMMON USAGE PATTERNS:")
    print("-" * 30)
    
    code_examples = [
        ("Import the module", "from _example import ffi, lib"),
        ("Get current time", "time_ptr = lib.get_current_time_string()\ntime_str = ffi.string(time_ptr).decode('utf-8')\nlib.free_string(time_ptr)"),
        ("Allocate memory", "buffer = lib.malloc(size)\nchar_buf = ffi.cast('char*', buffer)\n# ... use buffer ...\nlib.free(buffer)"),
        ("Check file size", "size = lib.get_file_size(b'filename.txt')"),
        ("Get temp directory", "temp_ptr = lib.get_temp_path()\ntemp_dir = ffi.string(temp_ptr).decode('utf-8')\nlib.free_string(temp_ptr)")
    ]
    
    for description, code in code_examples:
        print(f"\n{description}:")
        for line in code.split('\n'):
            print(f"  {line}")

if __name__ == "__main__":
    success = demonstrate_cffi_features()
    
    if success:
        show_usage_examples()
        print("\n✓ All demonstrations completed successfully!")
    else:
        print("\n✗ Demonstration failed - module not available")
        sys.exit(1)
