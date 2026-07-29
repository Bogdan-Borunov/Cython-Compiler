from setuptools import setup
from Cython.Build import cythonize
from CompilerFunction import *
from languges import *
from pathlib import Path
import os
import sys
import importlib
import traceback

lan = 0 # 0 - English, 1 - Русский

print(run[lan])

print(commands[lan])

while True:
    s = str(input("We: "))

    if s == "/help" or s == "help":
        print(commands[lan])
    elif s == "/github" or s == "github":
        print("https://github.com/Bogdan-Borunov/Cython-Compiler")
    elif s == "/start" or s == "start":
        file_name = str(input(StartCompile[lan]))
        compile(file_name, lan)
    elif s == "/create" or s == "create":
        name_file = str(input(WritePYXname[lan]))
        ccompile(name_file, lan)
    elif s == "/import" or s == "import":
        name_file = str(input(WritePYXname[lan]))
        PythonImport(name_file, lan)
    elif s == "/run" or s == "run":
        pass
    elif s == "/exit" or s == "exit":
        break
    else:
        print(NotFound[lan])