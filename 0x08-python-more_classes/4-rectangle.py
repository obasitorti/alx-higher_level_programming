#!/usr/bin/python3
"""This module defines a class rectangle"""


class Rectangle:
    """This class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Inittialisation of class rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the condtions for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the conditions for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((2*self.__height) + (2*self.__width))

    def __str__(self):
        """Prints the rectangle with #s"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["#"*self.__width for rows in range(self.__height)]))

    def __repr__(self):
        """String representation"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
