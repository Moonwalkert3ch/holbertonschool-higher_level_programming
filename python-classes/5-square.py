#!/usr/bin/python3

""" python3 -c 'print(__import__("3-Square.py").__doc__)' """
"""python3 -c 'print(__import__("4-Square.py").MyClass.my_function.__doc__)'"""


class Square:
    """ Class that defines a square """

    def __init__(self, size=0):
        """
        initialized Square class
        param arg: size - defines size of square
        """

        self.__size = size

    @property
    def size(self):
        """
        retrieves the size of square
        """

        return self. __size

    @size.setter
    def size(self, value):
        """
        sets value of size
        raises exceptions:
        TypeError if not an integer
        ValueError if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """"
        calculates area of square
        returns the current square area
        """

        return (self. __size ** 2)

    def my_print(self):
        """
        prints the square with the character #
        """

        for i in range(self.__size):
            print("#" * self.__size)

        if self.__size == 0:
            print()
