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
        """
        return area measurement
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Returns rectangle in # symbol character
        """
        for rows in range(self.__y):
            print("")
        for rows in range(self.__height):
            for col in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        Return the print() and str() representation
        """
        return (f"[{self.__class__.__name__}] ({self.id})"
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args):
        """
         assigns an argument to each attribute
         Param Arg: *args - no kw arg
        """
        if args:
            for arg in args:
                if arg is args[0]:
                    self.id = arg
                elif arg is args[1]:
                    self.width = arg
                elif arg is args[2]:
                    self.height = arg
                elif arg is args[3]:
                    self.x = arg
                elif arg is args[4]:
                    self.y = arg

        def dictionary(self):
            """returns dictionary
            """
            return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                    'id': getattr(self. "id"), 'height':
                    getattr(self, "height"),
                    'width': getattr(self, "width")}
