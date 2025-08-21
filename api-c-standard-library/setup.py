#!/usr/bin/env python3
"""
setup.py for Windows-compatible CFFI API example
This demonstrates how to integrate CFFI with setuptools for distribution.
"""

from setuptools import setup

setup(
    name="cffi-windows-example",
    version="1.0.0",
    description="Windows-compatible CFFI API mode example",
    author="CFFI Demo",
    packages=[],
    
    # CFFI integration
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["example_build.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"],
    
    # Include the test script
    py_modules=["test_example"],
    
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6",
)
