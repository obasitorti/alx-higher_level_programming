#!/usr/bin/python3
"""initialize module"""


import json


class Base:
    """defines a class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns json string representation of the dict"""
        if list_dictionaries is None:
            return ("[]")
        else:
            json.dumps(list_dictionaries)
