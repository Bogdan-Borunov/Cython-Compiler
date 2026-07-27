from setuptools import setup
from Cython.Build import cythonize
from languges import *

def compile(file_name, lan):
    setup(
        ext_modules=cythonize(file_name)
    )

    print(SuccessfulCompilation[lan])

def ccompile(file_name, lan):
    with open(f"{file_name}.pyx", "w", encoding="utf-8") as file:
        file.write(f"print('{HelloCython[lan]}')")

    setup(
        ext_modules=cythonize(f"{file_name}.pyx")
    )

    print(SuccessfulCompilation[lan])