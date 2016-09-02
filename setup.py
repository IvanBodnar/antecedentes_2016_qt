import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

setup(
    name='Prueba',
    version='0.1',
    description='Prueba',
    options={},
    executables=[Executable('main.py', base=base)]
)