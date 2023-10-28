#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
args = argv[1:]

if argc == 0:
    print("0 argument{}.".format("" if argc == 1 else "s"))
else:
    print("{} argument{}:".format(argc, "" if argc == 1 else "s"))

for i in range(argc):
    print("{}: {}".format(i + 1, args[i]))