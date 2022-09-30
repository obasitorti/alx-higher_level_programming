#!/usr/bin/python3
"""module that defines empty class"""


class BaseGeometry:
    """defines a public attribute 'area' """

    def area(self):
        raise Exception("area() is not implemented")
