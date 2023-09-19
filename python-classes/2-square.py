#!/usr/bin/python3

""" python3 -c 'print(__import__("1-Square.py").__doc__)' """
"""python3 -c 'print(__import__("2-Square.py").MyClass.my_function.__doc__)'"""


class Square:
    """ Class that defines a square """

    def __init__(self, size=0):
        """
        initialized Square class
        param arg: size - will be area computation of square
        raises exceptions:
        for TypeError if not an integer
        and ValueError if less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
