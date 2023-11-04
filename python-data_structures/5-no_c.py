#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return ""
    else:
        my_string = my_string.translate({ord("c"): None})
        my_string = my_string.translate({ord("C"): None})
        return my_string
