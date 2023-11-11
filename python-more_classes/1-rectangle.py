#!/usr/bin/python3
"""Define Rectangle class"""


class Rectangle:
    """Define a Rectangle class"""
    def __init__(self, width=0, height=0):
        """Args:
            Width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the length"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
