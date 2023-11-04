#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for x in num:
            print(x,end=' ')
        print(end='\n')

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()