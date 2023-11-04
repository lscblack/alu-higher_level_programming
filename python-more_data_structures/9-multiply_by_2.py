#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    double_ditc = dict(a_dictionary)
    for K, V in double_ditc.items():
        double_ditc[K] = V * 2
    return double_ditc
