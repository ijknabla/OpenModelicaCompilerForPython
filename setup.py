#!/usr/bin/env python3

from pathlib import Path
from setuptools import setup, find_packages


setup(
    name="OpenModelicaCompiler",
    version="0.0.0",
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
    packages=[
        "omc4py",
        "omc4py.parser",
    ],
    install_requires=[
        "ModelicaLanguage==0.0.0a6",  # fix to current alpha version
        "PyZMQ",
        "Arpeggio",
        "numpy",
        "typing_extensions",
    ],
    python_requires='>=3.6',
)
