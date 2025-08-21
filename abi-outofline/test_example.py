"""
Test script for the out-of-line ABI example
This script tests the build process and basic functionality.
"""

import os
import sys
import subprocess
import importlib.util

def test_build_process():
    """Test that the build script runs successfully."""
    print("Testing build process...")
    
    try:
        result = subprocess.run([sys.executable, "simple_example_build.py"], 
                              capture_output=True, text=True, check=True)
        print("✓ Build script executed successfully")
        print(f"Build output: {result.stdout}")
        
        # Check if the generated file exists
        if os.path.exists("_simple_example.py"):
            print("✓ Generated _simple_example.py file found")
            return True
        else:
            print("✗ Generated _simple_example.py file not found")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"✗ Build script failed: {e}")
        print(f"Error output: {e.stderr}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def test_ffi_module():
    """Test that the generated FFI module can be imported."""
    print("\nTesting FFI module import...")
    
    try:
        # Try to import the generated module
        spec = importlib.util.spec_from_file_location("_simple_example", "_simple_example.py")
        if spec is None:
            print("✗ Could not load module spec")
            return False
            
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Check if ffi object is available
        if hasattr(module, 'ffi'):
            print("✓ FFI module imported successfully")
            print(f"✓ FFI object available: {type(module.ffi)}")
            return True
        else:
            print("✗ FFI object not found in module")
            return False
            
    except Exception as e:
        print(f"✗ Failed to import FFI module: {e}")
        return False

def test_usage_example():
    """Test that the usage example runs without errors."""
    print("\nTesting usage example...")
    
    try:
        result = subprocess.run([sys.executable, "usage_example.py"], 
                              capture_output=True, text=True, check=True, timeout=30)
        print("✓ Usage example executed successfully")
        print("Sample output:")
        print(result.stdout[:500] + ("..." if len(result.stdout) > 500 else ""))
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Usage example failed: {e}")
        print(f"Error output: {e.stderr}")
        return False
    except subprocess.TimeoutExpired:
        print("✗ Usage example timed out")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def main():
    print("=== Out-of-line ABI Example Test Suite ===\n")
    
    # Change to the abi-outofline directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    tests_passed = 0
    total_tests = 3
    
    # Run tests
    if test_build_process():
        tests_passed += 1
    
    if test_ffi_module():
        tests_passed += 1
    
    if test_usage_example():
        tests_passed += 1
    
    # Summary
    print(f"\n=== Test Results ===")
    print(f"Passed: {tests_passed}/{total_tests} tests")
    
    if tests_passed == total_tests:
        print("🎉 All tests passed! The example is working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Check the output above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
