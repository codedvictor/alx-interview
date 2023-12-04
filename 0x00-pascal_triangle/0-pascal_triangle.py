#!/usr/bin/python3
"""
a function that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    a list of lists of integers representing
    the Pascal’s triangle of n
    """

    ptri = []

    if n <= 0:
        return ptri
    for x in range(n):
        xrow = []
        for y in range(x + 1):
            if (y == 0 or y == x):
                xrow.append(1)
            else:
                xrow.append(ptri[x - 1][y - 1] + ptri[x - 1][y])
        ptri.append(xrow)
    return ptri
