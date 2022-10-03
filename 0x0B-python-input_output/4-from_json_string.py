#!/usr/bin/python3
"""module defines returning json string to python obj """

import json


def from_json_string(my_str):
    """my_str json string"""
    return json.loads(my_str)
