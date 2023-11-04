#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return ""
    else:
        for num in my_list[::-1]:
            print("{:d}".format(num))
