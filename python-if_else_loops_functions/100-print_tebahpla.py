#!/usr/bin/python3
for char in range(ord('z'), ord('Z') - 1, -1):
    if (ord('a') <= char <= ord('z')) or (ord('A') <= char < ord('Z')):
        if char % 2 != 0:
            print("{}".format(chr(char).upper()), end='')
        else:
            print("{}".format(chr(char).lower()), end='')
