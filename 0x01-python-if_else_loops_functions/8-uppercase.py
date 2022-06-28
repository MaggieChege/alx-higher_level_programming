#!/usr/bin/python3
def uppercase(str):
    """Write a function that
    prints a string in uppercase
    followed by a new line."""
    strtmp = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            strtmp += chr(ord(c) - 32)
        else:
            strtmp += c
    print("{}".format(strtmp))
