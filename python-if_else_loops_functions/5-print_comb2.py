#!/usr/bin/python3
for num in range(0, 99 + 1):
    if num == 99:
        print("{:02}".format(num), end=" ", flush=True)
    else:
        print("{:02}".format(num), end=", ", flush=True)
