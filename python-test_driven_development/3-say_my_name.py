#!/usr/bin/python3
"""python3 -c 'print(__import__("3-say_my_name.py").__doc__)"""


def say_my_name(first_name, last_name=""):
    """Returns: prints a name
    Param Arg1: first_name(str) - first name to print
    Arg2: last_name(str) - last name to print
    Raise Exceptions:
    TypeError if is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
