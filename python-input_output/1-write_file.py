#!/usr/bin/python3
"""Defines a function that writes a string to a UTF text file
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """ writes a string to a UTF text file
    Param Arg!: filename(str) - file to write in
    Arg2: text(str) - text to write
    Returns: the number of chars written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
