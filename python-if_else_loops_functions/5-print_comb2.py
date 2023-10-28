#!/usr/bin/python3

output = ""
for num in range(100):
    if num == 99:
        output += "{:02} ".format(num)
    else:
        output += "{:02}, ".format(num)

print(output, end="", flush=True)
