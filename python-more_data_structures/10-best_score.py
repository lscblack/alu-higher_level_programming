#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = list(a_dictionary.items())[0][1]
    for key, value in a_dictionary.items():
        if value > max:
            max = value
    for key, value in a_dictionary.items():
        if value == max:
            return key
