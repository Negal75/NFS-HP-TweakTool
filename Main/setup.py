# setup.py
from cx_Freeze import setup, Executable

setup(
    name="Need For Speed Hot Pursuit TweakTool",
    version="0.1",
    description="Tweaks for Hot Pursuit",
    executables=[Executable("main.py", base="Win32GUI")]
)
