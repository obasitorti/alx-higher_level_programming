#!/usr/bin/python3
"""this modules defines how to append text to file"""


def append_write(filename="", text=""):
    """defines aappending text to the end of file"""
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
