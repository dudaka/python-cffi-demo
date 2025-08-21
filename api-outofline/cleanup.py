#!/usr/bin/env python3
"""
Cross-platform cleanup script for API out-of-line example.
Removes all generated files and build artifacts.
"""

import os
import shutil
import sys
import glob
from pathlib import Path

def remove_safely(path, description):
    """Safely remove a file or directory."""
    try:
        path = Path(path)
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()
            print(f"✓ Deleted {description}")
            return True
        else:
            print(f"  {description} not found (already clean)")
            return True
    except Exception as e:
        print(f"✗ Failed to delete {description}: {e}")
        return False

def main():
    """Main cleanup function."""
    print("🧹 Cleaning up CFFI API out-of-line build artifacts...")
    print("=" * 60)
    
    # Get the script directory
    script_dir = Path(__file__).parent
    original_cwd = Path.cwd()
    
    # Change to script directory
    os.chdir(script_dir)
    
    success_count = 0
    total_count = 0
    
    # List of files/directories to remove
    cleanup_targets = [
        ("_example.c", "generated C source"),
        ("build", "build directory"),
        ("Release", "Release directory"),
        ("dist", "distribution directory"),
        ("__pycache__", "__pycache__ directory"),
        ("setup.cfg", "setup.cfg file"),
        (".coverage", "coverage data file"),
        (".pytest_cache", "pytest cache directory"),
        (".tox", "tox directory"),
    ]
    
    # Remove specific files/directories
    for target, description in cleanup_targets:
        total_count += 1
        if remove_safely(target, description):
            success_count += 1
    
    # Remove compiled extension files with wildcards
    pyd_files = glob.glob("_example*.pyd")
    for pyd_file in pyd_files:
        total_count += 1
        if remove_safely(pyd_file, f"compiled extension ({pyd_file})"):
            success_count += 1
    
    # Remove Visual Studio build artifacts
    vs_artifacts = ["*.exp", "*.lib", "*.obj", "*.pdb", "*.ilk"]
    for pattern in vs_artifacts:
        artifact_files = glob.glob(pattern)
        for artifact_file in artifact_files:
            total_count += 1
            if remove_safely(artifact_file, f"VS build artifact ({artifact_file})"):
                success_count += 1
    
    # Remove egg-info directories (pattern matching)
    egg_info_dirs = glob.glob("*.egg-info")
    for egg_dir in egg_info_dirs:
        total_count += 1
        if remove_safely(egg_dir, f"egg-info directory ({egg_dir})"):
            success_count += 1
    
    # Remove compiled Python files
    pyc_files = glob.glob("**/*.pyc", recursive=True)
    for pyc_file in pyc_files:
        total_count += 1
        if remove_safely(pyc_file, f"compiled Python file ({pyc_file})"):
            success_count += 1
    
    # Remove wheel files that might be left in root
    wheel_files = glob.glob("*.whl")
    for wheel_file in wheel_files:
        total_count += 1
        if remove_safely(wheel_file, f"wheel file ({wheel_file})"):
            success_count += 1
    
    # Remove egg files
    egg_files = glob.glob("*.egg")
    for egg_file in egg_files:
        total_count += 1
        if remove_safely(egg_file, f"egg file ({egg_file})"):
            success_count += 1
    
    print("=" * 60)
    print(f"🎯 Cleanup results: {success_count}/{total_count} items processed successfully")
    
    if success_count == total_count:
        print("✅ All generated files cleaned up successfully!")
    else:
        print(f"⚠️  {total_count - success_count} items could not be cleaned up")
    
    # Show remaining non-source files
    print("\n📁 Remaining files in directory:")
    source_extensions = {'.py', '.md', '.txt', '.bat', '.ps1'}
    source_files = set()
    
    remaining_artifacts = []
    for item in Path('.').iterdir():
        if item.name.startswith('.'):
            continue
        if item.suffix not in source_extensions and item.name not in source_files:
            remaining_artifacts.append(item.name)
    
    if remaining_artifacts:
        print("   Build artifacts still present:")
        for artifact in sorted(remaining_artifacts):
            print(f"   ⚠️  {artifact}")
    else:
        print("   ✅ Only source files remain")
    
    # Restore original directory
    os.chdir(original_cwd)
    
    return 0 if success_count == total_count else 1

if __name__ == "__main__":
    sys.exit(main())
