# cython: language_level=3
from setuptools import setup
from Cython.Build import cythonize

setup(
    name = 'cfib',
    ext_modules = cythonize("cfib.pyx"),
    zip_safe = False,
)

