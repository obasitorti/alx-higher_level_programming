#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        i = number % (-10)
    elif number >= 0:
        i = number % 10
    return (i)
