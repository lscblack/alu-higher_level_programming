#!/usr/bin/python3.8

import py_compile

def main():
    compiled_code = py_compile.compile("hidden_4.pyc")
    code = compiled_code.co_code

    names = compiled_code.co_names

    for name in sorted(names):
        if not name.startswith('__'):
            print(name)

if __name__ == "__main__":
    main()
