from setuptools import setup
from Cython.Build import cythonize
from languges import *

def PythonImport(file_name, lan):
    with open("import.py", "w", encoding="utf-8") as file:
        file.write(f"from {file_name} import *")
        
    print(SuccessfulCompilation[lan])

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