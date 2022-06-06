#!/usr/bin/env python3
from io import open
from setuptools import setup
from os import path


here = path.abspath(path.dirname(__file__))


# get the long description from the README.rst
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="openapi3v1",
    version="0.0.2",
    description="Client and Validator of OpenAPI 3 Specifications. Forked from dorthu/openapi3 ad modifications made on top of it",
    long_description=long_description,
    author="Anchit Arnav",
    url="https://github.com/anchitarnav/openapi3",
    packages=["openapi3"],
    license="BSD 3-Clause License",
    install_requires=["PyYaml", "requests"],
    extras_require={
        "test": ["pytest", "pytest-asyncio==0.16", "uvloop", "hypercorn", "pydantic", "fastapi"],
    },
)
