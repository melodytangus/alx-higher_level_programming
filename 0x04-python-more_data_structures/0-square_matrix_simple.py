#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    '''computes square values of a matrix'''
    return ([list(map(lambda x: x * x, row)) for row in matrix])
