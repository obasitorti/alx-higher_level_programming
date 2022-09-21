#!/usr/bin/python3
"""
    docstring for program
"""


class Square:
    """
        this class defines a square
    """

    def __init__(self, size=0):
        """
            arguments: self and size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            this method returns the area of a square
        """
        return self.__size ** 2
