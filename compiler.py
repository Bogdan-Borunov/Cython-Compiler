import subprocess
import sys

subprocess.run([
    sys.executable,
    "PythonLibary/setup.py",
    "build_ext",
    "--inplace"
], check=True)