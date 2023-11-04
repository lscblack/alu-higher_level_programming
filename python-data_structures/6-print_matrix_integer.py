#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for x in num:
            print("{:d}".format(x),end=' ')
        print(end='\n')
