#!/usr/bin/python3
for d in range(10):
    for a in range(d + 1, 10):
        print("{:d}{:d}".format(d, a), end=", " if d < 8 else "\n")
