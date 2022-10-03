#!/usr/bin/python3
"""
    this module defines a fucntion 
    which opens and prints a file to 
    standard output
"""


def read_file(filename=""):
    """function definition"""
    a_file = open(filename, encoding='utf-8')
    a_file.read()
