#!/usr/bin/python3
def uppercase(input_str):
    output_str = ""
    for char in input_str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        output_str += "{}".format(uppercase_char)
    print(output_str)
