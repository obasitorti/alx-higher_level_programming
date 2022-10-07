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
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """assigns attributes to arguments"""
        attributes = ["id", "size", "x", "y"]
        for arg in range(len(args)):
            for attr in range(len(attributes)):
                if attr == arg:
                    setattr(self, attributes[attr], args[arg])
                    break

        if not args or len(args) == 0:
            for key, value in kwargs.items():
                for attr in range(len(attributes)):
                    if key == attributes[attr]:
                        setattr(self, attributes[attr], value)
                        break

    def to_dictionary(self):
        """returns dictionary representation of object"""
        obj_dict = {"id": self.id, "size": self.width,
                    "x": self.x, "y": self.y}

        return obj_dict
