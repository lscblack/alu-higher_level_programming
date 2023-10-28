#!/usr/bin/python3

output = ""
for num in range(100):
    if num == 99:
        output += f"{num:02} "
    else:
        output += f"{num:02}, "

print(output, end="", flush=True)
