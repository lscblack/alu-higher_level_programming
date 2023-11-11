#!/usr/bin/python3
"""Are you docuemnted ?"""


def append_write(filename="", text=""):
    """How far now"""
    with open(filename, 'a+') as f:
        return f.write(text)
