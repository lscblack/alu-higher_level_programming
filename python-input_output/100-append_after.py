#!/usr/bin/python3
"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    """append_after"""

    with open(filename, mode="r+", encoding="utf-8") as readFile:
        data = readFile.readlines()

    count = 0
    with open(filename, mode="w", encoding="utf-8") as writeFile:
        for lines in data:
            count += 1
            if search_string in lines:
                data.insert(count, new_string)
        for lines in data:
            writeFile.write(lines)
