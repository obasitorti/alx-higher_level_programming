#!/usr/bin/python3
"""module initialization"""

# from rectangle import Rectangle
from models.rectangle import Rectangle


class Square(Rectangle):
    """class inherited fr0m class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialisation of attributes"""
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overrides string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.__height

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")

        self.__width = value
        self.__height = value
