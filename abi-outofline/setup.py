"""
Setup script for the out-of-line ABI mode example.
This demonstrates how to distribute a CFFI project using setuptools.
"""

from setuptools import setup, find_packages

# Read the README file for the long description
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "Out-of-line ABI mode example for CFFI"

setup(
    name="cffi-abi-outofline-example",
    version="1.0.0",
    author="CFFI Example",
    author_email="example@example.com",
    description="A demonstration of CFFI's out-of-line ABI mode",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/cffi-abi-outofline-example",
    
    # Find all Python packages
    packages=find_packages(),
    
    # Include the build script and generated module
    py_modules=[
        "simple_example_build",
        "usage_example", 
        "test_example",
        "cli_wrapper"
    ],
    
    # CFFI-specific configuration
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["simple_example_build.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"],
    
    # Python version requirement
    python_requires=">=3.7",
    
    # Classifiers for PyPI
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
    ],
    
    # Entry points for command-line usage
    entry_points={
        "console_scripts": [
            "cffi-abi-example=cli_wrapper:run_example",
            "cffi-abi-test=cli_wrapper:run_test",
        ],
    },
    
    # Include additional files
    include_package_data=True,
    
    # Keywords for easier discovery
    keywords="cffi, abi, ffi, c, windows, example, demonstration",
    
    # Project URLs
    project_urls={
        "Bug Reports": "https://github.com/example/cffi-abi-outofline-example/issues",
        "Source": "https://github.com/example/cffi-abi-outofline-example",
        "Documentation": "https://cffi.readthedocs.io/",
    },
)
