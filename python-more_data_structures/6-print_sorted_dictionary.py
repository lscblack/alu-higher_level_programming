#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for K, V in sorted(a_dictionary.items()):
        print("{}: {}".format(K, V))
