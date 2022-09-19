#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = x+1
    try:
        print(my_list[:c])
    except ValueError:
        print("enter correct number")
