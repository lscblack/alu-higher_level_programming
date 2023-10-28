#!/usr/bin/python3
def magic_calculation(a, b):
    result = 98  # LOAD_CONST 1 (98)
    result += a  # LOAD_FAST 0 (a)
    result += b  # LOAD_FAST 1 (b)
    result **= 2  # BINARY_POWER
    return result  # RETURN_VALUE
