#!/usr/bin/python3
import py_compile
import marshal

if __name__ == "__main":
    compiled_code = open("hidden_4.pyc", "rb").read()
    code = marshal.loads(compiled_code[12:])
    names = code.co_names

    for name in sorted(names):
        if not name.startswith('__'):
            print(name)