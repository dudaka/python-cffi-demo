#!/usr/bin/env python3
"""
Test script for the Pi approximation CFFI extension.
This script demonstrates how to use the compiled C extension.
"""

import sys
import os

# Add current directory to path for importing the extension
sys.path.insert(0, '.')
sys.path.insert(0, os.path.dirname(__file__))

try:
    import _pi_cffi

    def test_pi_approximation():
        """Test the pi_approx function with different iteration counts."""
        
        print("Testing Pi Approximation Function (Static Library Version)")
        print("=" * 55)
        
        # Test with different numbers of iterations
        test_cases = [1000, 10000, 100000, 1000000]
        
        for n in test_cases:
            result = _pi_cffi.lib.pi_approx(n)
            error = abs(result - 3.14159265)
            print(f"Iterations: {n:8d} | Pi approx: {result:.6f} | Error: {error:.6f}")
        
        print("\nNote: This is a Monte Carlo approximation, so results will vary each run.")
        print("Generally, more iterations should give better approximations.")

    if __name__ == "__main__":
        test_pi_approximation()

except ImportError as e:
    print(f"Error importing the extension: {e}")
    print("Make sure you have built the extension by running:")
    print("1. cmake --build . --target python_extension")
    print("2. Or manually: python piapprox_build.py")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python path: {sys.path[:3]}")
except Exception as e:
    print(f"Error running the test: {e}")
