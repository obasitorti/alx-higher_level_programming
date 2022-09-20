#!/usr/bin/python3
from sys import exc_info, stderr


def safe_function(fct, *args):
    try:
        r = fct(*args)
        return (r)

    except (IndexError, TypeError, ZeroDivisionError, ValueError):
        print('Exception: {}'.format(exc_info()[1]), file=stderr)
        return None
