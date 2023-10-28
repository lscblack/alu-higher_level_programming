#!/usr/bin/python3
if __name__ == "__main":
    with open("variable_load_5.py", "r") as file:
        code = compile(file.read(), "variable_load_5.py", 'exec')
        exec(code)
    print(a)