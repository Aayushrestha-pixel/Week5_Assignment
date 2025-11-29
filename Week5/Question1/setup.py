# setup for cython build
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("revstr.pyx")
)