#!/usr/bin/python3
"""module initialisation"""


def add_attribute(obj, att, value):
    """adds a new attribute to an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
