#!/usr/bin/python3
"""module defines a function for writing to file"""


def write_file(filename="", text=""):
    """this function explains writing text to file"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        return a_file.write(text)
