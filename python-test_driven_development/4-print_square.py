#!/usr/bin/python3
"""print square function"""


def print_square(size):
    """prints a square with "#" size."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
