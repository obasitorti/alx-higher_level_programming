#!/usr/bin/pyton3
def square_matrix_simple(matrix=[]):
    # new_matrix = {x: x**2 for x in matrix}
    # print (new_matrix)
    # new_matrix = (list(map(lambda x : x**2, row)) for row in matrix)
    # return new_matrix
    return [list(map(lambda x: x**2, row)) for row in matrix]
