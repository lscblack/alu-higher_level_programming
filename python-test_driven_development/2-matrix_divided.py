#!/usr/bin/python3
"""
This is a Matrix Divided function
"""


def matrix_divided(matrix, div):
    """Divides all elements in a matrix"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix of integers/floats")
    size = None
    for yy in matrix:
        if type(yy) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(yy)
        elif size != len(yy):
            raise TypeError("Each row of the matrix must have the same size")
        for i in yy:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in yy] for yy in matrix]
