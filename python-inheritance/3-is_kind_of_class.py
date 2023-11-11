#!/usr/bin/python3
"""Checks object class"""


def is_kind_of_class(obj, a_class):
    """Checks object class
    Args:
        - obj: object to class
        - a_class: class to check
    """
    return isinstance(obj, a_class)
