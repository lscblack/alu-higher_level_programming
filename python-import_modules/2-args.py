#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
args = argv[1:]

print("Number of argument{}: {}{}".format("s" if argc != 1 else "", argc, "." if argc == 0 else ":"))

if argc > 0:
    for i, arg in enumerate(args, 1):
        print("{}: {}".format(i, arg))
