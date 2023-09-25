#!/usr/bin/python3
"""Defines a class that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a BaseGeometery Rectangle """

    def __init__(self, width, height):
        """ initializes rectangle
        Param Arg1: width(int) - width of rectangle
        Arg2: height(int) - height of rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area """
        return self.__width * self.__height

    def __str__(self):
        """Returns the str() and print()"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
