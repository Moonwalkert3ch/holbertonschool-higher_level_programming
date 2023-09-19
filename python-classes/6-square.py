#!/usr/bin/python3

""" python3 -c 'print(__import__("5-Square.py").__doc__)' """
"""python3 -c 'print(__import__("6-Square.py").MyClass.my_function.__doc__)'"""


class Square:
    """ Class that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """
        initialized Square class
        param arg1: size - defines size of square
        arg2: position - position of square
        """

        self.__size = size
        self.__position = position


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

    @property
    def position(self):
        """
        retrieves position of square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        param arg: value - must be a tuple of 2 pos integers
        raises exceptions
        TypeError if not 2 pos ints or a tuple
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

        [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print("", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()

        if self.__size == 0:
            print()
