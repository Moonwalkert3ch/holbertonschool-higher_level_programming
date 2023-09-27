#!/usr/bin/python3
"""Defines a function that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """
    Prints the text of a UTF8 file in stdout
    Param Arg: filename(char) - file to be read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
