#!/usr/bin/python3
for num in range(0, 99 + 1):
    if num == 99:
        print("{}".format(num,'02'),end="")
    else:
        print("{}".format(num,'02')+", ",end="")
