from setuptools import setup
from Cython.Build import cythonize
from languges import *
from pathlib import Path
import tkinter as tk
from tkinter import filedialog


def select_folder():
    root = tk.Tk()
    root.withdraw()

    folder = filedialog.askdirectory(
        title="Select folder project: "
    )

    root.destroy()

    if not folder:
        return None

    return Path(folder).resolve()

def ChangeLanFunction(lan):
    try:
        lans = int(lan)

        writeLan = input(ChangeLan[lans])

        with open("languges.txt", "w", encoding="utf-8") as file:
            file.write(writeLan)

        if int(writeLan) > 1 or int(writeLan) < 0:
            print(NotFound[lan])
            with open("txt_files/languges.txt", "w", encoding="utf-8") as file:
                file.write("0")
        else:
            print(SuccessfulCompilation[lans])

    except Exception as e:
        print("Ошибка:", e)

        with open("languges.txt", "w", encoding="utf-8") as file:
            file.write("0")

def options(lan):
    with open("txt_files/SavePath.txt", "r", encoding="utf-8") as file:
        sp = file.read()

    if not sp:
        sp = none[lan]

    print(SavePath[lan], sp, "\n" * 2, RenamePathMessage[lan])

def PythonImport(file_name, lan):
    fn = file_name

    if ".pyx" in fn:
        fn = fn.replace(".pyx", "")

    with open("txt_files/SavePath.txt", "r", encoding="utf-8") as file:
        sp = file.read()

    with open(f"{sp}import.py", "w", encoding="utf-8") as file:
        file.write(f"from {fn} import *")
        
    print(SuccessfulCompilation[lan])

def compile(file_name, lan):
    with open("txt_files/SavePath.txt", "r", encoding="utf-8") as file:
        sp = file.read()

    setup(
        ext_modules=cythonize(sp, file_name)
    )

    print(SuccessfulCompilation[lan])

def selected_folder(lan):
    project_path = str(select_folder())

    if project_path is not None:
        with open("txt_files/SavePath.txt", "w", encoding="utf-8") as file:
            file.write(project_path)

    print(SuccessfulCompilation[lan])

def ccompile(file_name, lan):
    with open("txt_files/SavePath.txt", "r", encoding="utf-8") as file:
        sp = file.read()

    with open(f"{sp}{file_name}", "w", encoding="utf-8") as file:
        file.write(f"print('{HelloCython[lan]}')")

    setup(
        ext_modules=cythonize(f"{sp}{file_name}")
    )

    print(SuccessfulCompilation[lan])