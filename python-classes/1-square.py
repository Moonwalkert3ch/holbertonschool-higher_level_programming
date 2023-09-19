#!/usr/bin/python3

""" python3 -c 'print(__import__("0-Square.py").__doc__)' """
"""python3 -c 'print(__import__("1-Square.py").MyClass.my_function.__doc__)'"""


class Square:
    """ Class that defines a square """

    def __init__(self, size):
        """ initializing class """
        """ param arg: size - will be area computation """

        self.__size = size
