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

    @property
    def size(self):
        """
            returns size of square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
            sets the size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
            this method returns the area of a square
        """
        return self.__size ** 2
