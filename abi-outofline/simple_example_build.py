"""
Out-of-line ABI mode example - Build script
This script generates the FFI module that can be imported later.
"""

from cffi import FFI

ffibuilder = FFI()

# Note that the actual source is None for ABI mode
ffibuilder.set_source("_simple_example", None)

# Define the C functions we want to use
# For Windows compatibility, we'll use both C library and Windows-specific functions
ffibuilder.cdef("""
    // Standard C library functions
    int printf(const char *format, ...);
    int puts(const char *s);
    char* getenv(const char *name);
    
    // Windows-specific functions for demonstration
    typedef void* HANDLE;
    typedef unsigned long DWORD;
    
    HANDLE GetStdHandle(DWORD nStdHandle);
    int GetConsoleScreenBufferInfo(HANDLE hConsoleOutput, void* lpConsoleScreenBufferInfo);
    int SetConsoleTextAttribute(HANDLE hConsoleOutput, unsigned short wAttributes);
""")

if __name__ == "__main__":
    print("Building FFI module...")
    ffibuilder.compile(verbose=True)
    print("FFI module built successfully!")
    print("You can now run the usage example.")
