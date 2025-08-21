"""
Wrapper script for the CFFI ABI out-of-line example.
This ensures the FFI module is built and available before running the main example.
"""

import os
import sys
import importlib.util

def ensure_ffi_module():
    """Ensure the FFI module is built and available."""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Check if _simple_example.py exists
    ffi_module_path = os.path.join(script_dir, "_simple_example.py")
    
    if not os.path.exists(ffi_module_path):
        print("FFI module not found. Building it...")
        
        # Import and run the build script
        build_script_path = os.path.join(script_dir, "simple_example_build.py")
        if os.path.exists(build_script_path):
            # Add the script directory to sys.path temporarily
            if script_dir not in sys.path:
                sys.path.insert(0, script_dir)
            
            try:
                # Import the build script and run it
                spec = importlib.util.spec_from_file_location("simple_example_build", build_script_path)
                build_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(build_module)
                
                if hasattr(build_module, 'ffibuilder'):
                    print("Building FFI module...")
                    build_module.ffibuilder.compile(verbose=False)
                    print("FFI module built successfully!")
                else:
                    print("Warning: No ffibuilder found in build script")
            except Exception as e:
                print(f"Error building FFI module: {e}")
                sys.exit(1)
        else:
            print(f"Build script not found at: {build_script_path}")
            sys.exit(1)
    
    # Ensure the script directory is in sys.path
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)

def run_example():
    """Run the main usage example."""
    ensure_ffi_module()
    
    # Now import and run the usage example
    try:
        import usage_example
        if hasattr(usage_example, 'main'):
            return usage_example.main()
        else:
            print("No main function found in usage_example")
            return 1
    except Exception as e:
        print(f"Error running example: {e}")
        return 1

def run_test():
    """Run the test example."""
    ensure_ffi_module()
    
    # Import and run the test example
    try:
        import test_example
        if hasattr(test_example, 'main'):
            return test_example.main()
        else:
            print("No main function found in test_example")
            return 1
    except Exception as e:
        print(f"Error running test: {e}")
        return 1

if __name__ == "__main__":
    # Determine which function to call based on script name
    script_name = os.path.basename(sys.argv[0])
    if 'test' in script_name.lower():
        sys.exit(run_test())
    else:
        sys.exit(run_example())
