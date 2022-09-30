#!/usr/bin/python3
"""module that defines a function"""


def inherits_from(obj, a_class):
    """function checks if class is inherited"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
