#!/usr/bin/python3
"""Defines a function that appends a string at the end of a UTF8
text file and returns the number of characters added."""


def append_write(filename="", text=""):
    """
    appends a string at the end of the file
    Param Args1: filename(str) - file to write in
    Arg2: text(str) - characters to write
    Returns: number of chars added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
