#!/usr/bin/python3
"""module defines a subclass rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        defines a class rectangle inherited from BaseGeometry
    """

    def __init__(self, width, height):
        """initialization of subclass"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """returns the rectangle"""
        get = (self.__class__.__name__)
        return ("[{}] {}/{}".format(get, self.__width, self.__height))
