# file "example.py"
# API out-of-line mode example - Usage script
# This demonstrates using the compiled C extension

import sys
import time

try:
    from _example import ffi, lib
except ImportError as e:
    print(f"Error importing _example: {e}")
    print("\nYou need to build the extension first:")
    print("Run: python example_build.py")
    print("\nMake sure you have a C compiler installed.")
    sys.exit(1)

def demonstrate_array_operations():
    """Demonstrate fast array operations using C code."""
    print("=== Array Operations Demo ===")
    
    # Create input buffer with some test data
    size = 1000
    buffer_in = ffi.new("int[]", size)
    
    # Initialize buffer_in with some values
    print(f"Initializing array with {size} elements...")
    for i in range(size):
        buffer_in[i] = i + 1  # Values 1, 2, 3, ..., 1000
    
    # Test array sum
    print("\nTesting array sum...")
    start_time = time.time()
    result = lib.array_sum(buffer_in, size)
    c_time = time.time() - start_time
    
    # Compare with Python implementation
    start_time = time.time()
    python_result = sum(range(1, size + 1))
    python_time = time.time() - start_time
    
    print(f"C result: {result}")
    print(f"Python result: {python_result}")
    print(f"Results match: {result == python_result}")
    print(f"C time: {c_time:.6f}s")
    print(f"Python time: {python_time:.6f}s")
    if python_time > 0:
        speedup = python_time / c_time if c_time > 0 else float('inf')
        print(f"Speedup: {speedup:.2f}x")
    
    # Test array multiplication
    print(f"\nTesting array multiplication...")
    buffer_out = ffi.new("int[]", size)
    multiplier = 3
    
    lib.array_multiply(buffer_in, buffer_out, size, multiplier)
    
    # Verify first few results
    print(f"First 5 original values: {[buffer_in[i] for i in range(5)]}")
    print(f"First 5 multiplied by {multiplier}: {[buffer_out[i] for i in range(5)]}")
    
    # Verify correctness
    correct = all(buffer_out[i] == buffer_in[i] * multiplier for i in range(min(10, size)))
    print(f"Multiplication correct (first 10 elements): {correct}")

def demonstrate_fibonacci():
    """Demonstrate fast fibonacci calculation."""
    print("\n=== Fibonacci Demo ===")
    
    test_values = [10, 20, 30, 35]
    
    for n in test_values:
        print(f"\nCalculating fibonacci({n})...")
        
        # C implementation
        start_time = time.time()
        c_result = lib.fibonacci(n)
        c_time = time.time() - start_time
        
        # Python implementation for comparison
        def python_fibonacci(n):
            if n <= 1:
                return n
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b
        
        start_time = time.time()
        python_result = python_fibonacci(n)
        python_time = time.time() - start_time
        
        print(f"C result: {c_result}")
        print(f"Python result: {python_result}")
        print(f"Results match: {c_result == python_result}")
        print(f"C time: {c_time:.6f}s")
        print(f"Python time: {python_time:.6f}s")
        if python_time > 0 and c_time > 0:
            speedup = python_time / c_time
            print(f"Speedup: {speedup:.2f}x")

def main():
    print("CFFI API Out-of-line Mode Example")
    print("==================================")
    print("This example demonstrates compiling C code directly")
    print("in the build script for maximum performance.")
    
    try:
        demonstrate_array_operations()
        demonstrate_fibonacci()
        
        print("\n=== Summary ===")
        print("✓ Successfully called C functions from Python")
        print("✓ Demonstrated performance benefits of C code")
        print("✓ Used CFFI's out-of-line API mode")
        
    except Exception as e:
        print(f"\nError during execution: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
