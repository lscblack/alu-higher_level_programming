#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            # If the character is lowercase, convert it to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print(uppercase_char, end='')
        else:
            # If the character is not lowercase, print it as is
            print(char, end='')
