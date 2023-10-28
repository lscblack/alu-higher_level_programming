#!/usr/bin/python3
import py_compile

if __name__ == "__main":
    py_compile.compile("hidden_4.py")
    names = dir()
    for name in sorted(names):
        if not name.startswith('__'):
            print(name)
