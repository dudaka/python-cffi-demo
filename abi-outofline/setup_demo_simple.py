"""
Simple demonstration of setup.py installation and distribution.
This shows the key features without complex console script handling.
"""

import subprocess
import sys
import os
import tempfile
import shutil

def run_command(cmd, description, cwd=None):
    """Run a command and return success status."""
    print(f"\n{'='*50}")
    print(f"Running: {description}")
    print(f"Command: {cmd}")
    print('='*50)
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, 
                              text=True, cwd=cwd or os.getcwd())
        if result.stdout:
            print("Output:")
            print(result.stdout)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stderr:
            print("Error output:")
            print(e.stderr)
        return False, e.stderr

def main():
    print("=== CFFI Setup.py Demonstration ===")
    print("This demonstrates the key features of setuptools integration for CFFI")
    
    # Get the current directory
    original_dir = os.getcwd()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print(f"\nWorking in: {os.getcwd()}")
    
    # 1. Show the setup.py configuration
    print(f"\n{'='*50}")
    print("Setup.py Configuration Highlights:")
    print('='*50)
    print("Key features:")
    print("- setup_requires=['cffi>=1.0.0']  # Build-time dependency")
    print("- cffi_modules=['simple_example_build.py:ffibuilder']  # Auto-build FFI")
    print("- install_requires=['cffi>=1.0.0']  # Runtime dependency")
    print("- Includes all necessary Python modules")
    print("- Proper metadata for PyPI distribution")
    
    # 2. Build the package
    success, output = run_command("python setup.py build", 
                                 "Building package with setuptools")
    if not success:
        print("Build failed - this is required for distribution")
        return 1
    
    # 3. Create source distribution
    success, output = run_command("python setup.py sdist", 
                                 "Creating source distribution")
    if success:
        print("✓ Source distribution created successfully")
        print("  This creates a .tar.gz file that can be uploaded to PyPI")
    
    # 4. Create wheel distribution
    success, output = run_command("python setup.py bdist_wheel", 
                                 "Creating wheel distribution")
    if success:
        print("✓ Wheel distribution created successfully")
        print("  This creates a .whl file for faster installation")
    else:
        print("  Note: wheel package may not be installed")
    
    # 5. Show what was created
    print(f"\n{'='*50}")
    print("Generated Distribution Files:")
    print('='*50)
    
    if os.path.exists("dist"):
        for file in os.listdir("dist"):
            file_path = os.path.join("dist", file)
            file_size = os.path.getsize(file_path)
            print(f"  {file} ({file_size:,} bytes)")
    
    # 6. Test installation from distribution
    print(f"\n{'='*50}")
    print("Testing Installation from Distribution:")
    print('='*50)
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Testing installation in temporary directory: {temp_dir}")
        
        # Find the source distribution
        dist_files = [f for f in os.listdir("dist") if f.endswith(".tar.gz")]
        if dist_files:
            dist_file = os.path.join("dist", dist_files[0])
            print(f"Installing from: {dist_file}")
            
            # Install in the temp directory (dry run)
            cmd = f"pip install --dry-run {dist_file}"
            success, output = run_command(cmd, "Testing pip install (dry run)")
            
            if success:
                print("✓ Package is installable via pip")
            else:
                print("✗ Package has installation issues")
        else:
            print("No source distribution found to test")
    
    # 7. Show the CFFI integration
    print(f"\n{'='*50}")
    print("CFFI Integration Summary:")
    print('='*50)
    print("The setup.py demonstrates these CFFI features:")
    print("1. Automatic FFI module generation during build")
    print("2. Proper handling of build and runtime dependencies")
    print("3. Distribution of both source and generated FFI modules")
    print("4. Cross-platform compatibility")
    print("5. Integration with standard Python packaging tools")
    
    print(f"\n{'='*50}")
    print("Manual Usage:")
    print('='*50)
    print("After building, you can:")
    print("1. python usage_example.py  # Run the example directly")
    print("2. python test_example.py   # Run the test suite")
    print("3. pip install .            # Install the package locally")
    print("4. Upload dist/* to PyPI    # Distribute to others")
    
    # Restore original directory
    os.chdir(original_dir)
    
    print(f"\n{'='*50}")
    print("✓ Setup.py demonstration completed successfully!")
    print('='*50)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
