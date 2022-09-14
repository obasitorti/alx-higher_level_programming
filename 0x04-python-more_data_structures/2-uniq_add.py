#!/usr/bin/bash
def uniq_add(my_list=[]):
    a = set(my_list)
    b = 0
    for i in a:
        b += i
    return b
