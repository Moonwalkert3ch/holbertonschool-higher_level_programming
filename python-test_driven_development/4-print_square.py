#!/usr/bin/python3
"""python3 -c 'print(__import__("4-print_square.py").__doc__)"""


def print_square(size):
    """Returns: prints a square with the character #
    Param Arg: size(int) - the size length of the square
    Raise Exceptions:
    TypeError if is not an a integer
    ValueError if is lt 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        [print("#", end="") for col in range(size)]
        print("")
