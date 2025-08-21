# file "example_build.py"
# Windows-compatible example using C standard library functions

# Note: we instantiate the same 'cffi.FFI' class as in the previous
# example, but call the result 'ffibuilder' now instead of 'ffi';
# this is to avoid confusion with the other 'ffi' object you get below

from cffi import FFI
ffibuilder = FFI()

ffibuilder.set_source("_example",
   r""" // passed to the real C compiler,
        // contains implementation of things declared in cdef()
        #include <stdio.h>
        #include <stdlib.h>
        #include <string.h>
        #include <time.h>
        #ifdef _WIN32
        #include <windows.h>
        #include <io.h>
        #else
        #include <unistd.h>
        #endif

        // Custom wrapper functions for demonstration
        static char* get_current_time_string(void) {
            time_t raw_time;
            struct tm *time_info;
            char *buffer = malloc(26);
            
            time(&raw_time);
            time_info = localtime(&raw_time);
            strcpy(buffer, asctime(time_info));
            
            // Remove newline character
            buffer[strlen(buffer) - 1] = '\0';
            return buffer;
        }

        static int get_file_size(const char* filename) {
            FILE* file = fopen(filename, "r");
            if (!file) return -1;
            
            fseek(file, 0, SEEK_END);
            int size = ftell(file);
            fclose(file);
            return size;
        }

        static char* get_temp_path(void) {
            char* buffer = malloc(512);
            #ifdef _WIN32
            DWORD result = GetTempPathA(512, buffer);
            if (result == 0) {
                strcpy(buffer, "C:\\temp\\");
            }
            #else
            strcpy(buffer, "/tmp/");
            #endif
            return buffer;
        }

        // Memory management helper
        static void free_string(char* str) {
            if (str) free(str);
        }
    """,
    libraries=[])   # or a list of libraries to link with
    # (more arguments like setup.py's Extension class:
    # include_dirs=[..], extra_objects=[..], and so on)

ffibuilder.cdef("""
    // declarations that are shared between Python and C
    
    // C standard library functions
    char* get_current_time_string(void);
    int get_file_size(const char* filename);
    char* get_temp_path(void);
    void free_string(char* str);
    
    // Standard C library functions
    void* malloc(size_t size);
    void free(void* ptr);
    char* strcpy(char* dest, const char* src);
    size_t strlen(const char* str);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)