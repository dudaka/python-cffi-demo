"""
Simple usage example of the Pi approximation CFFI extension.
This demonstrates how to use the compiled C extension from Python.
"""

from _pi.lib import pi_approx

def main():
    print("Pi Approximation using Monte Carlo Method")
    print("="*40)
    
    test_cases = [10, 100, 1000, 10000, 50000, 100000]
    
    for n in test_cases:
        approx = pi_approx(n)
        error = abs(approx - 3.141592653589793)
        print(f"Iterations: {n:6d} | Pi ≈ {approx:.6f} | Error: {error:.6f}")

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("Error: The C extension is not built yet.")
        print("Please run: python pi_extension_build.py")
        print("Or run: python test_pi.py")
