#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="OpenModelicaCompiler",
    version="0.0.0a1",
    description="OpenModelica compiler (omc)  interface for Python3.x based on  OMPython",
    author="ijknabla",
    author_email="ijknabla@gmail.com",
    license="OSMC-PL 1.2",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    url="https://github.com/ijknabla/OpenModelicaCompilerForPython",
    packages=find_packages(),
    install_requires=[
        "ModelicaLanguage==0.0.0a6",  # fix to current alpha version
        "OMPython",
        "Arpeggio",
    ],
    python_requires='>=3.6',
)
