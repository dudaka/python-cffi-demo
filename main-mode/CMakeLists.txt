cmake_minimum_required(VERSION 3.15)
project(PiApproxCFFI VERSION 1.0.0 LANGUAGES C)

# Set C standard
set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Add compiler flags for debug/release
if(MSVC)
    set(CMAKE_C_FLAGS_DEBUG "/Od /Zi /MDd")
    set(CMAKE_C_FLAGS_RELEASE "/O2 /DNDEBUG /MD")
else()
    set(CMAKE_C_FLAGS_DEBUG "-g -O0 -Wall -Wextra")
    set(CMAKE_C_FLAGS_RELEASE "-O3 -DNDEBUG")
endif()

# Set default build type to Release if not specified
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
    set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release" "MinSizeRel" "RelWithDebInfo")
endif()

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# Source files
set(PI_SOURCES
    src/pi.c
)

set(PI_DLL_SOURCES
    src/pi_dll.c
)

# Option to build shared library (DLL on Windows)
option(BUILD_SHARED_LIB "Build as shared library (DLL)" ON)
option(BUILD_PYTHON_EXTENSION "Build Python CFFI extension" ON)

# Create the pi library
if(BUILD_SHARED_LIB)
    # Build as shared library
    add_library(piapprox SHARED ${PI_DLL_SOURCES})
    target_compile_definitions(piapprox PRIVATE BUILDING_PI_DLL)
    
    # Set output name for DLL
    set_target_properties(piapprox PROPERTIES
        OUTPUT_NAME "piapprox"
        PREFIX ""
    )
    
    # Install DLL
    install(TARGETS piapprox
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib
    )
else()
    # Build as static library
    add_library(piapprox STATIC ${PI_SOURCES})
    
    # Install static library
    install(TARGETS piapprox
        ARCHIVE DESTINATION lib
    )
endif()

# Install headers
install(FILES 
    ${CMAKE_CURRENT_SOURCE_DIR}/include/pi.h
    ${CMAKE_CURRENT_SOURCE_DIR}/include/pi_dll.h
    DESTINATION include
)

# Custom target for Python CFFI extension
if(BUILD_PYTHON_EXTENSION)
    find_program(PYTHON_EXECUTABLE python)
    
    if(PYTHON_EXECUTABLE)
        if(BUILD_SHARED_LIB)
            set(BUILD_SCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/python/piapprox_build_dll.py)
            set(TEST_SCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/python/test_dll.py)
        else()
            set(BUILD_SCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/python/piapprox_build.py)
            set(TEST_SCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/python/test.py)
        endif()
        
        add_custom_target(python_extension
            COMMAND ${CMAKE_COMMAND} -E copy_if_different $<TARGET_FILE:piapprox> .
            COMMAND ${PYTHON_EXECUTABLE} ${BUILD_SCRIPT}
            DEPENDS piapprox
            WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
            COMMENT "Building Python CFFI extension"
        )
        
        add_custom_target(test_python
            COMMAND ${PYTHON_EXECUTABLE} ${TEST_SCRIPT}
            DEPENDS python_extension
            WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
            COMMENT "Testing Python CFFI extension"
        )
    else()
        message(WARNING "Python executable not found. Python targets will not be available.")
    endif()
endif()

# Add custom targets for cleanup
add_custom_target(clean_all
    COMMAND ${CMAKE_COMMAND} -E remove_directory ${CMAKE_CURRENT_BINARY_DIR}
    COMMENT "Cleaning all build files"
)

# Display build information
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "Build shared library: ${BUILD_SHARED_LIB}")
message(STATUS "Build Python extension: ${BUILD_PYTHON_EXTENSION}")
message(STATUS "C compiler: ${CMAKE_C_COMPILER}")
