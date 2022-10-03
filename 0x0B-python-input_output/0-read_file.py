#!/usr/bin/python3
"""
    this module defines a fucntion 
    which opens and prints a file to 
    standard output
"""


def read_file(filename=""):
    """function definition"""
    with open(filename, encoding='utf-8') as a_file
        print(a_file.read(), end="")
