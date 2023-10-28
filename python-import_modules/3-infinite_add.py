#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]
    result = sum(int(arg) for arg in args)
    print(result)
