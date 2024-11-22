#!/usr/bin/python3
"""
Rotate A 2D Matrix in a CLockwise manner
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.
    """
    # Reverse row order
    matrix.reverse()
    # for loop swaps the elemnts in the diagonal one time``
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
