#!/usr/bin/python3
"""Defines a rectangle class """


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes rectangle class
        Param Arg1: width(int) - width of rectangle
        Arg2: height(int) - height of rectangle
        Raises exceptions:
        TypeError: if not an integer
        ValueError: if is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
