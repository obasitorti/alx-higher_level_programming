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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation of the dict"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the python object into a json file"""
        obj_dict = []
        if list_objs is not None:
            for obj in list_objs:
                obj_dict.append(cls.to_dictionary(obj))
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(obj_dict))
