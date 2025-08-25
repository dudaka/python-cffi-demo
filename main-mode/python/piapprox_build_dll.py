from cffi import FFI
import os

ffibuilder = FFI()

# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("""
    float pi_approx(int n);
""")

# For shared library approach, we'll link against the DLL
ffibuilder.set_source("_pi_cffi_dll",
"""
     #include "pi_dll.h"   // the C header of the library
""",
     libraries=['piapprox'],           # library name, for the linker (looks for piapprox.dll)
     library_dirs=['.', '../build', '../build/Release', '../build/Debug'],  # look for library in build directories
     include_dirs=['../include'])     # look for headers

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
