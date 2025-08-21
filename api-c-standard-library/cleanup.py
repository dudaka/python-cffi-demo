#!/usr/bin/env python3
"""
Cross-platform cleanup script for CFFI build artifacts
Removes all generated files and build directories
"""

import os
import shutil
import glob
import sys

def remove_if_exists(path, description=""):
    """Safely remove a file or directory if it exists."""
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"✓ Deleted file: {path}")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"✓ Deleted directory: {path}")
        elif description:
            # Check if it's a glob pattern
            matches = glob.glob(path)
            if matches:
                for match in matches:
                    remove_if_exists(match)
            # else:
            #     print(f"  {description} not found")
    except OSError as e:
        print(f"✗ Failed to delete {path}: {e}")

def main():
    print("Cleaning CFFI build artifacts...")
    print("=" * 40)
    
    # Files to remove
    files_to_remove = [
        "_example.c",
        "_example.pyd", 
        "_example.so",  # Unix
        "_example.*.pyd",  # Pattern for versioned .pyd files
        "_example.*.so",   # Pattern for versioned .so files
    ]
    
    # Directories to remove  
    dirs_to_remove = [
        "build",
        "Release", 
        "__pycache__",
        "dist",
        ".pytest_cache"
    ]
    
    # Test files that might be left behind
    test_files = [
        "test_file.txt",
        "demo.txt", 
        "sample.txt",
        "small.txt",
        "medium.txt", 
        "empty.txt"
    ]
    
    # Remove specific files
    for file_pattern in files_to_remove:
        if '*' in file_pattern:
            matches = glob.glob(file_pattern)
            for match in matches:
                remove_if_exists(match)
        else:
            remove_if_exists(file_pattern)
    
    # Remove directories
    for directory in dirs_to_remove:
        remove_if_exists(directory)
    
    # Remove test files
    for test_file in test_files:
        remove_if_exists(test_file)
    
    # Remove .pyc files
    pyc_files = glob.glob("*.pyc")
    for pyc_file in pyc_files:
        remove_if_exists(pyc_file)
    
    # Remove egg-info directories
    egg_info_dirs = glob.glob("*.egg-info")
    for egg_dir in egg_info_dirs:
        remove_if_exists(egg_dir)
    
    print("\n" + "=" * 40)
    print("Cleanup completed!")
    print("\nRemaining files:")
    
    # List remaining files
    remaining_files = []
    for ext in ['.py', '.md', '.bat', '.ps1', '.txt']:
        remaining_files.extend(glob.glob(f"*{ext}"))
    
    remaining_files.sort()
    for f in remaining_files:
        print(f"  {f}")
    
    if not remaining_files:
        print("  (no files found)")

if __name__ == "__main__":
    main()
