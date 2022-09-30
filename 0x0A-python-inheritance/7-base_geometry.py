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
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
