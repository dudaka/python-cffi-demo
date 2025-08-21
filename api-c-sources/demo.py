"""
Complete demonstration of CFFI API mode with C sources.
This script shows the complete workflow from C sources to Python usage.
"""

import os
import sys
import subprocess

def check_extension_exists():
    """Check if the C extension already exists."""
    return os.path.exists("_pi.c") and any(f.startswith("_pi.") and f.endswith(".pyd") for f in os.listdir("."))

def build_extension():
    """Build the C extension."""
    print("Building CFFI extension from C sources...")
    print("-" * 40)
    
    try:
        import pi_extension_build
        print("✓ Extension built successfully!")
        return True
    except Exception as e:
        print(f"✗ Failed to build extension: {e}")
        return False

def test_extension():
    """Test the built extension with various iteration counts."""
    try:
        from _pi.lib import pi_approx
        
        print("\nTesting the C extension:")
        print("-" * 40)
        
        test_cases = [
            (10, "Quick test"),
            (1000, "Small test"), 
            (10000, "Medium test"),
            (100000, "Large test")
        ]
        
        actual_pi = 3.141592653589793
        
        for iterations, description in test_cases:
            approx = pi_approx(iterations)
            error = abs(approx - actual_pi) 
            accuracy = (1 - error/actual_pi) * 100
            
            print(f"{description:12s}: {iterations:6d} iterations → Pi ≈ {approx:.6f} ({accuracy:.2f}% accurate)")
        
        print("✓ All tests completed successfully!")
        return True
        
    except ImportError as e:
        print(f"✗ Cannot import extension: {e}")
        return False
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False

def show_file_info():
    """Show information about the project files."""
    print("\nProject Structure:")
    print("-" * 40)
    
    files_info = [
        ("pi.c", "C source file with Monte Carlo Pi approximation"),
        ("pi.h", "C header file with function declaration"),
        ("pi_extension_build.py", "CFFI builder script"),
        ("test_pi.py", "Test script for the extension"),
        ("usage_example.py", "Simple usage demonstration"),
        ("demo.py", "This comprehensive demo script"),
        ("_pi.c", "Generated CFFI wrapper (after build)"),
        ("_pi.*.pyd", "Compiled Python extension (after build)")
    ]
    
    for filename, description in files_info:
        if filename.endswith("*"):
            # Check for .pyd files specifically
            exists = "✓" if any(f.startswith("_pi.") and f.endswith(".pyd") for f in os.listdir(".")) else " "
        else:
            exists = "✓" if os.path.exists(filename) else " "
        print(f"{exists} {filename:20s} - {description}")

def main():
    """Main demonstration function."""
    print("CFFI API Mode Demonstration")
    print("=" * 50)
    print("This demo shows how to use CFFI to call C sources from Python")
    print("on Windows using the Monte Carlo method for Pi approximation.")
    print()
    
    # Show project structure
    show_file_info()
    
    # Check if extension already exists
    if check_extension_exists():
        print("\n✓ Extension already built, proceeding to test...")
        test_extension()
    else:
        print("\nExtension not found. Building...")
        if build_extension():
            test_extension()
        else:
            print("Failed to build extension. Please check your setup.")
            return
    
    print("\n" + "=" * 50)
    print("Demo completed! You can now use the extension in your Python code:")
    print("  from _pi.lib import pi_approx")
    print("  result = pi_approx(10000)")
    print("  print(f'Pi approximation: {result}')")

if __name__ == "__main__":
    main()
