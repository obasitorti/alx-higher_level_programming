#!/usr/bin/python3
"""module initialization"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """instantiation ofattributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary description"""
        return (self.__dict__)
