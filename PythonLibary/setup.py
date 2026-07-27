from setuptools import setup
from Cython.Build import cythonize
from CompilerFunction import *
from languges import *
from pathlib import Path
import importlib

lan = 0 # 0 - English, 1 - Русский

print(run[lan])

print(commands[lan])

def RunFile():
    print("---- IN DEVELOPMENT ----")

    # name = str(input(WritePYXname[lan]))

    # module_name = Path(name).stem

    # module = importlib.import_module(module_name)

while True:
    s = str(input("We: "))

    if s == "/help" or s == "help":
        print(commands[lan])
    elif s == "/github" or s == "github":
        pass
    elif s == "/start" or s == "start":
        file_name = str(input(StartCompile[lan]))
        compile(file_name, lan)
    elif s == "/create" or s == "create":
        name_file = str(input(WritePYXname[lan]))
        ccompile(name_file, lan)
    elif s == "/run" or s == "run":
        RunFile()
    elif s == "/exit" or s == "exit":
        break
    else:
        print(NotFound[lan])