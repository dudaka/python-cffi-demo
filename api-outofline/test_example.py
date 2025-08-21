# test_example.py
# Test script for the API out-of-line example

import unittest
import sys
import os

# Add current directory to path to import the extension
sys.path.insert(0, os.path.dirname(__file__))

try:
    from _example import ffi, lib
    EXTENSION_AVAILABLE = True
except ImportError:
    EXTENSION_AVAILABLE = False
    print("Warning: Extension not built. Run 'python example_build.py' first.")

@unittest.skipUnless(EXTENSION_AVAILABLE, "Extension not built")
class TestCExtension(unittest.TestCase):
    """Test the compiled C extension functions."""
    
    def test_array_sum_small(self):
        """Test array sum with small array."""
        size = 5
        buffer_in = ffi.new("int[]", size)
        
        # Initialize with values 1, 2, 3, 4, 5
        for i in range(size):
            buffer_in[i] = i + 1
        
        result = lib.array_sum(buffer_in, size)
        expected = sum(range(1, size + 1))  # 1+2+3+4+5 = 15
        
        self.assertEqual(result, expected)
    
    def test_array_sum_large(self):
        """Test array sum with larger array."""
        size = 1000
        buffer_in = ffi.new("int[]", size)
        
        for i in range(size):
            buffer_in[i] = i + 1
        
        result = lib.array_sum(buffer_in, size)
        expected = sum(range(1, size + 1))  # Sum of 1 to 1000
        
        self.assertEqual(result, expected)
    
    def test_array_multiply(self):
        """Test array multiplication."""
        size = 10
        multiplier = 3
        
        buffer_in = ffi.new("int[]", size)
        buffer_out = ffi.new("int[]", size)
        
        # Initialize input buffer
        for i in range(size):
            buffer_in[i] = i + 1
        
        # Perform multiplication
        lib.array_multiply(buffer_in, buffer_out, size, multiplier)
        
        # Check results
        for i in range(size):
            expected = (i + 1) * multiplier
            self.assertEqual(buffer_out[i], expected)
    
    def test_fibonacci_base_cases(self):
        """Test fibonacci base cases."""
        self.assertEqual(lib.fibonacci(0), 0)
        self.assertEqual(lib.fibonacci(1), 1)
    
    def test_fibonacci_known_values(self):
        """Test fibonacci with known values."""
        # Known fibonacci values: F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5, F(6)=8
        known_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        
        for i, expected in enumerate(known_values):
            result = lib.fibonacci(i)
            self.assertEqual(result, expected, f"fibonacci({i}) should be {expected}, got {result}")
    
    def test_fibonacci_larger_value(self):
        """Test fibonacci with a larger value."""
        # F(20) = 6765
        result = lib.fibonacci(20)
        expected = 6765
        self.assertEqual(result, expected)
    
    def test_buffer_types(self):
        """Test that we can work with CFFI buffer types."""
        size = 5
        buffer_in = ffi.new("int[]", size)
        
        # Test that we can assign and read values
        for i in range(size):
            buffer_in[i] = i * 2
        
        for i in range(size):
            self.assertEqual(buffer_in[i], i * 2)

class TestBuildSystem(unittest.TestCase):
    """Test that the build system works correctly."""
    
    def test_build_script_exists(self):
        """Test that the build script exists."""
        self.assertTrue(os.path.exists("example_build.py"))
    
    def test_usage_script_exists(self):
        """Test that the usage script exists."""
        self.assertTrue(os.path.exists("example.py"))
    
    def test_readme_exists(self):
        """Test that documentation exists."""
        self.assertTrue(os.path.exists("README.md"))

if __name__ == "__main__":
    if not EXTENSION_AVAILABLE:
        print("\nTo run all tests, first build the extension:")
        print("python example_build.py")
        print("\nRunning basic tests only...\n")
    
    unittest.main(verbosity=2)
