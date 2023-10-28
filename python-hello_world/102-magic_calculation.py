#!/usr/bin/python3
def magic_calculation(a, b):
    result = 98  # LOAD_CONST 1 (98)
    result = result + a  # LOAD_FAST 0 (a) and BINARY_ADD
    result = result + b  # LOAD_FAST 1 (b) and BINARY_ADD
    return result
