#!/usr/bin/python3.7
import io
import marshal

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as f:
        compiled_code = f.read()

    code = marshal.loads(io.BytesIO(compiled_code[12:]))
    names = code.co_names
    names.append("__main__")

    for name in sorted(names):
        if not name.startswith('__'):
            print(name)
