#!/usr/bin/python3
"""module that defines empty class"""


class BaseGeometry:
    """defines two public attributes """

    def area(self):
        """defines area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """defines integer_validator"""
        self.value = value
        self.name = name
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
        defines a class rectangle inherited from BaseGeometry
    """

    def __init__(self, width, height):
        """initialization of subclass"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
