#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list_ in matrix:
        if not list_:
            print()
        for item in list_:
            if item == list_[-1]:
                print('{:d}'.format(item))
            else:
                print('{:d}'.format(item), end=" ")
