from setuptools import setup
from Cython.Build import cythonize
from languges import *

def ChangeLanFunction(lan):
    try:
        lans = int(lan)

        writeLan = input(ChangeLan[lans])

        with open("languges.txt", "w", encoding="utf-8") as file:
            file.write(writeLan)

        if int(writeLan) > 1 or int(writeLan) < 0:
            print(NotFound[lan])
            with open("languges.txt", "w", encoding="utf-8") as file:
                file.write("0")
        else:
            print(SuccessfulCompilation[lans])

    except Exception as e:
        print("Ошибка:", e)

        with open("languges.txt", "w", encoding="utf-8") as file:
            file.write("0")

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
    with open(f"{file_name}", "w", encoding="utf-8") as file:
        file.write(f"print('{HelloCython[lan]}')")

    setup(
        ext_modules=cythonize(f"{file_name}")
    )

    print(SuccessfulCompilation[lan])