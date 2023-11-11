#!/usr/bin/python3
"""Checks object class"""


def is_same_class(obj, a_class):
    """Checks object class
    Args:
        - obj: object to class
        - a_class: class to check
    """
    return type(obj) is a_class
