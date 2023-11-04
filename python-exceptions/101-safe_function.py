#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
    except Exception as err:
        result = None
        stderr.write("Exception: {}\n".format(err))
    return result
