#!/usr/bin/python3
"""Define text-identation function Below."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    yy = 0
    while yy < len(text) and text[yy] == ' ':
        yy += 1

    while yy < len(text):
        print(text[yy], end="")
        if text[yy] == "\n" or text[yy] in ".?:":
            if text[yy] in ".?:":
                print("\n")
            yy += 1
            while yy < len(text) and text[yy] == ' ':
                yy += 1
            continue
        yy += 1
