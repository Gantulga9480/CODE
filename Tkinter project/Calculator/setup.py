from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Calculator.py", base=base)]

packages = ["idna", "math", "tkinter"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<Calculator>",
    options = options,
    version = "2.0",
    description = "Gantulga-2020",
    executables = executables
)
