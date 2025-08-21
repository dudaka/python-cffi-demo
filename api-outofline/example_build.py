# file "example_build.py"
# API out-of-line mode example - Build script
# This demonstrates compiling C code directly in the build script for performance

from cffi import FFI
import os

ffibuilder = FFI()

# Define the C function signature that will be available to Python
ffibuilder.cdef("""
    int array_sum(int *buffer_in, int size);
    void array_multiply(int *buffer_in, int *buffer_out, int size, int multiplier);
    int fibonacci(int n);
""")

# Set the source code - this C code will be compiled into the extension
ffibuilder.set_source("_example",
r"""
    // Fast array sum implementation in C
    static int array_sum(int *buffer_in, int size)
    {
        int sum = 0;
        for (int i = 0; i < size; i++) {
            sum += buffer_in[i];
        }
        return sum;
    }
    
    // Array multiplication - multiply each element and store in output buffer
    static void array_multiply(int *buffer_in, int *buffer_out, int size, int multiplier)
    {
        for (int i = 0; i < size; i++) {
            buffer_out[i] = buffer_in[i] * multiplier;
        }
    }
    
    // Fast fibonacci calculation using iterative approach
    static int fibonacci(int n)
    {
        if (n <= 1) return n;
        
        int a = 0, b = 1, temp;
        for (int i = 2; i <= n; i++) {
            temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
""")

if __name__ == "__main__":
    print("Building C extension module...")
    print("This requires a C compiler (Visual Studio Build Tools or similar)")
    
    try:
        ffibuilder.compile(verbose=True)
        print("\nBuild successful!")
        print("You can now run 'python example.py' to test the extension.")
    except Exception as e:
        print(f"\nBuild failed: {e}")
        print("\nMake sure you have a C compiler installed:")
        print("- Visual Studio Build Tools")
        print("- Or full Visual Studio with C++ support")
        print("- Or MinGW-w64")
