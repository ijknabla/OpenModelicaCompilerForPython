#!/usr/bin/env python3

import builtins

from pathlib import Path
from setuptools import setup, find_packages

try:
    builtins.__OMC4PY_SETUP__ = True  # type: ignore
    from omc4py import __version__ as omc4py_version
except ImportError:
    raise


setup(
    name="OpenModelicaCompiler",
    version=omc4py_version,
    description="OpenModelica compiler (omc) interface for Python>=3.6",
    long_description=(Path(__file__).parent/"README.md").read_text(),
    long_description_content_type="text/markdown",
    author="ijknabla",
    author_email="ijknabla@gmail.com",
    license="OSMC-PL 1.2",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: User Interfaces",
    ],
    url="https://github.com/ijknabla/OpenModelicaCompilerForPython",
    packages=find_packages(
        include=["omc4py*"],
    ),
    install_requires=[
        "ModelicaLanguage==0.0.0a6",  # fix to current alpha version
        "PyZMQ",
        "Arpeggio",
        "numpy",
        "typing_extensions",
    ],
    python_requires='>=3.6',
)
