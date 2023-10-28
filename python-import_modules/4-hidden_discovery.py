#!/usr/bin/python3.8

import marshal

def main():
    with open("hidden_4.pyc", "rb") as file:
        file.read(8)  # Skip the first 8 bytes
        code = marshal.load(file)

    names = code.co_names

    for name in sorted(names):
        if not name.startswith('__'):
            print(name)

if __name__ == "__main":
    main()

