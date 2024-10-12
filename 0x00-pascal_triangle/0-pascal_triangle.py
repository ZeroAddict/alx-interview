#!/usr/bin/python3
"""
0-pascal_triangle
This module contains a function that returns a list of lists
of integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    k reps PascalTriangleList
    inner for loop specifies a j index for number of elem
    to be inserted at 1th  index of current row
    adds the previous rows's jth and j+1th

    Args:
        n (int): number of rows
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, len(k[i - 1])):
            row.append(k[i - 1][j - 1] + k[i - 1][j])
        row.append(1)
        k.append(row)
    return k
