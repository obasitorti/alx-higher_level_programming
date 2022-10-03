#!/usr/bin/python3
"""module initialisation"""

import json


def load_from_json_file(filename):
    """module defines creates object from json file"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        return json.load(a_file)
