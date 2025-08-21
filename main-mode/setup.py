from textwrap import dedent

from setuptools import find_packages, setup

setup(
    version="1.0.0",
    name="piapprox-cffi",
    description="CFFI-based Python bindings for Pi approximation using Monte Carlo method.",
    long_description=dedent(
        """\
        # Pi Approximation CFFI Demo

        This package provides CFFI-based Python bindings for a C implementation of Pi approximation
        using the Monte Carlo method.

        ## Features

        - Fast C implementation of Monte Carlo Pi approximation
        - Python bindings via CFFI for easy integration
        - Demonstrates CFFI main mode compilation with static libraries
        - Educational example of Python-C integration

        ## Usage

        ```python
        import _pi_cffi
        
        # Approximate Pi using 1 million iterations
        pi_estimate = _pi_cffi.lib.pi_approx(1000000)
        print(f"Pi approximation: {pi_estimate}")
        ```

        The Monte Carlo method generates random points and checks if they fall within a unit circle
        to estimate the value of Pi. More iterations generally provide better approximations.
        """
    ),
    long_description_content_type="text/markdown",
    author="Dung Ho",
    author_email="dungho@nmsu.edu",
    license="MIT",
    url="https://github.com/yourusername/piapprox-cffi",
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["piapprox_build.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"],
    packages=[],  # No Python packages, just the compiled extension
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: C",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: Microsoft :: Windows",
    ],
    keywords="pi approximation monte carlo cffi c extension mathematics",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/piapprox-cffi/issues",
        "Source": "https://github.com/yourusername/piapprox-cffi",
        "Documentation": "https://github.com/yourusername/piapprox-cffi/blob/main/README.md",
    },
)
