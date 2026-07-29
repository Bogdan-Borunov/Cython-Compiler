import subprocess
import sys

subprocess.run([
    sys.executable,
    "setup.py",
    "build_ext",
    "--inplace"
], check=True)