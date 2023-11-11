#!/usr/bin/python3
"""How far with comments """


def add_attribute(obj, name, value):
    """are you documented"""
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
