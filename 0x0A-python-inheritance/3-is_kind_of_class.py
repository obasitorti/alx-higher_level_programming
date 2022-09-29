#!/usr/bin/python3
"""module defines a function"""


def is_kind_of_class(obj, a_class):
    """checks if obj is a istance of a_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
