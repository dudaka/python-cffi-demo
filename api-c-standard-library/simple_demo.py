#!/usr/bin/env python3
"""
Simple demonstration of the CFFI Windows example
This shows the most basic usage patterns.
"""

def main():
    print("=== Simple CFFI Windows Demo ===\n")
    
    try:
        # Import the compiled module
        from _example import ffi, lib
        print("✓ CFFI module imported successfully!")
    except ImportError:
        print("✗ Failed to import CFFI module")
        print("Run: python example_build.py")
        return
    
    # Get current time
    time_ptr = lib.get_current_time_string()
    current_time = ffi.string(time_ptr).decode('utf-8')
    lib.free_string(time_ptr)
    print(f"Current time: {current_time}")
    
    # Get temp directory
    temp_ptr = lib.get_temp_path()
    temp_dir = ffi.string(temp_ptr).decode('utf-8')
    lib.free_string(temp_ptr)
    print(f"Temp directory: {temp_dir}")
    
    # Test file operations
    with open("demo.txt", "w") as f:
        f.write("CFFI Demo File")
    
    size = lib.get_file_size(b"demo.txt")
    print(f"Demo file size: {size} bytes")
    
    # Clean up
    import os
    os.remove("demo.txt")
    
    print("\n✓ Demo completed successfully!")

if __name__ == "__main__":
    main()
