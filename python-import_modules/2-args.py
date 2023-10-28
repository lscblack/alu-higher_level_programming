#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
args = argv[1:]

if argc == 0:
    print("0 arguments.")
elif argc == 1:
    print("1 argument:")
    print("1: {}".format(args[0]))
else:
    print("{} arguments:".format(argc))
    for i in range(argc):
        print("{}: {}".format(i + 1, args[i]))
