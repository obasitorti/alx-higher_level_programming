#!/usr/bin/python3
"""module initialization"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """instantiation ofattributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """new method with conditional return statements"""
        if attrs is None:
            return self.__dict__

        else:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__.keys():
                    new_dict[i] = self.__dict__[i]

        return new_dict

    def reload_from_json(self, json):
        """sets attributes of every instance"""
        for (key, value) in json.items():
            setattr(self, key, value)
