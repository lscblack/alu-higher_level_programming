#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    prevent the user from instantiating new lockedClass attributes
    for anything but attributes called 'first_namer'.
    """

    __slots__ = ["first_name"]
