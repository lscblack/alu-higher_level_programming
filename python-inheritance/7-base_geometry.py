#!/usr/bin/python3
"""Empty BaseGeometry class"""


class BaseGeometry:
    """Class Geometry"""

    def area(self):
        """Raises Exception only"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Integer validator if less than 0 or not int"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
