#!/usr/bin/python3
"""this module defines a function ref=garding json"""

import json


def save_to_json_file(my_obj, filename):
    """defines adding object to textfile"""
    with open(filename, 'w', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
