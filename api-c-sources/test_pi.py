"""
Test script for the Pi approximation C extension.
This script builds and tests the CFFI extension.
"""
import os
import sys

def build_extension():
    """Build the C extension."""
    print("Building the Pi approximation C extension...")
    import pi_extension_build
    print("Extension built successfully!")

def test_extension():
    """Test the built extension."""
    try:
        from _pi.lib import pi_approx
        
        print("\nTesting Pi approximation...")
        
        # Test with small number of iterations
        approx_small = pi_approx(10)
        print(f"Pi approximation with 10 iterations: {approx_small}")
        assert str(approx_small).startswith("3."), f"Expected result to start with '3.', got {approx_small}"
        
        # Test with larger number of iterations
        approx_large = pi_approx(10000)
        print(f"Pi approximation with 10000 iterations: {approx_large}")
        assert str(approx_large).startswith("3.1"), f"Expected result to start with '3.1', got {approx_large}"
        
        # Test with very large number of iterations for better accuracy
        approx_very_large = pi_approx(100000)
        print(f"Pi approximation with 100000 iterations: {approx_very_large}")
        
        print("All tests passed!")
        
    except ImportError as e:
        print(f"Error importing the extension: {e}")
        print("Make sure to build the extension first by running: python pi_extension_build.py")
        return False
    except Exception as e:
        print(f"Test failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test-only":
        # Only test, don't build
        test_extension()
    else:
        # Build and then test
        build_extension()
        print("\n" + "="*50)
        test_extension()
