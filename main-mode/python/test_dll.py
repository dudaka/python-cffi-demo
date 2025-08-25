#!/usr/bin/env python3
"""
Test script for Pi Approximation DLL Extension

This script demonstrates the usage of the pi_approx function
from a C shared library (DLL) via Python CFFI.
"""

import sys
import os

# Add current directory to path for importing the extension
sys.path.insert(0, '.')
sys.path.insert(0, os.path.dirname(__file__))

try:
    from _pi_cffi_dll import lib
    print("Testing Pi Approximation Function (DLL Version)")
    print("=" * 50)
    
    # Test different iteration counts
    test_values = [1000, 10000, 100000, 1000000]
    
    for iterations in test_values:
        pi_estimate = lib.pi_approx(iterations)
        error = abs(pi_estimate - 3.14159265359)
        print(f"Iterations: {iterations:8d} | Pi approx: {pi_estimate:.6f} | Error: {error:.6f}")
    
    print("\nNote: This is a Monte Carlo approximation, so results will vary each run.")
    print("The DLL (piapprox.dll) is loaded dynamically and can be shared by other applications.")
    
except ImportError as e:
    print(f"Error importing the extension: {e}")
    print("Make sure you have built the extension by running:")
    print("1. cmake --build . --target python_extension")
    print("2. Or manually: python piapprox_build_dll.py")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python path: {sys.path[:3]}")
except Exception as e:
    print(f"Error running the test: {e}")
