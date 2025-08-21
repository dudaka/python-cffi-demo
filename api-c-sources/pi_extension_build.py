from cffi import FFI
import sys
import os

ffibuilder = FFI()

ffibuilder.cdef("float pi_approx(int n);")

# Windows-specific configuration
libraries = []
if sys.platform == "win32":
    # On Windows, math functions are built into the C runtime
    libraries = []
else:
    # On Unix-like systems, link with the math library
    libraries = ['m']

ffibuilder.set_source("_pi",  # name of the output C extension
"""
    #include "pi.h"
""",
    sources=['pi.c'],   # includes pi.c as additional sources
    libraries=libraries)  # platform-specific libraries

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
