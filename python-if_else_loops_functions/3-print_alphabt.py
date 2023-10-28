#!/usr/bin/python3
for let in range(ord('a'), ord('z')+1):
    if chr(let) == 'e' or chr(let) == 'q':
        continue
    else:
        print("{}".format(chr(let)), end='')
