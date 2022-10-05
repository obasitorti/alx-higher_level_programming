#!/usr/bin/python3
"""module initialisation"""


def pascal_triangle(n):
    """pasca's triangle"""
    n_list = []
    for i in range(n):
        temp_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(n_list[i-1][j-1] + n_list[i-1][j])
        n_list.append(temp_list)
    return n_list
