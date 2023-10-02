#!/usr/bin/python3
"""Defines a class Rectangle that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the rectangle
        Param Arg1: width(int) - width of rectangle
        Arg2: height(int) - height of rectangle
        Arg3:(int) x - points to itself
        Arg4:(int) y - points to itself
        Arg5: id(int) - identity of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """Set height
        Param Arg: value - value to be determined
        raise exceptions:
        TypeError if not an integer
        ValueError if lt 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height
        Param Arg: value - value to be determined
        Raise Exceptions:
        TypeError - if not an int
        ValueError -  if lt 0
        """
        if type(value) != int:
            raise TypeError("height must be a in integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ set y
        Param arg: value - value to be determined
        Raise Exceptions:
        TpeError - must be an int
        ValueError - if lt 0
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves y """
        return self.__y

    @x.setter
    def y(self, value):
        """set y
        Param Arg: value - value to be determined
        Raise Exceptions:
        TypeError - must be an int
        ValueError - if lt 0
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area measurement"""
        return (self.width * self.height)

    def display(self):
        """Returns rectangle in # symbol character """
        rectangle = ""
        symbol = "#"

        for row in range(self.__height - 1):
            rectangle += symbol * self.__width

        print("{}".format(rectangle))

    def __str__(self):
        """Return the print() and str() representation"""
        return
