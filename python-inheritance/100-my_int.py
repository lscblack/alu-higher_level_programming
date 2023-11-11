#!/usr/bin/python3
"""Rebel int"""


class MyInt(int):
    """Rebel int class"""

    def __eq__(self, other):
        """not equal when =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """equal when !="""
        return super().__eq__(other)
