"""
Demo script showing how to build and install the package.
This demonstrates the setuptools integration for CFFI projects.
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and print its output."""
    print(f"\n{'='*50}")
    print(f"Running: {description}")
    print(f"Command: {cmd}")
    print('='*50)
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print("Output:")
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stderr:
            print("Error output:")
            print(e.stderr)
        return False

def main():
    print("CFFI Out-of-line ABI Mode - Setup.py Demonstration")
    print("This script demonstrates various setuptools operations")
    
    # Change to the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print(f"\nWorking directory: {os.getcwd()}")
    
    # 1. Build the package
    if run_command("python setup.py build", "Building the package"):
        print("✓ Package built successfully")
    else:
        print("✗ Package build failed")
        return 1
    
    # 2. Create source distribution
    if run_command("python setup.py sdist", "Creating source distribution"):
        print("✓ Source distribution created")
    else:
        print("✗ Source distribution failed")
    
    # 3. Create wheel distribution (if wheel is available)
    if run_command("python setup.py bdist_wheel", "Creating wheel distribution"):
        print("✓ Wheel distribution created")
    else:
        print("✗ Wheel distribution failed (wheel package might not be installed)")
    
    # 4. Show what files would be installed
    if run_command("python setup.py egg_info", "Generating egg info"):
        print("✓ Egg info generated")
    
    # 5. Run tests using setup.py
    if run_command("python setup.py test", "Running tests via setup.py"):
        print("✓ Tests completed")
    else:
        print("✗ Tests failed (this is expected if pytest is not configured)")
    
    # 6. Check the package
    if run_command("python setup.py check", "Checking package metadata"):
        print("✓ Package check completed")
    
    print(f"\n{'='*50}")
    print("Demonstration completed!")
    print("\nGenerated files:")
    
    # List generated files
    for item in ["build", "dist", "*.egg-info"]:
        if os.path.exists(item) or any(f.endswith('.egg-info') for f in os.listdir('.') if os.path.isdir(f)):
            print(f"  - {item}")
    
    print("\nTo install the package, you would run:")
    print("  pip install .")
    print("  or")
    print("  pip install dist/cffi-abi-outofline-example-1.0.0.tar.gz")
    
    print("\nTo install in development mode:")
    print("  pip install -e .")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
