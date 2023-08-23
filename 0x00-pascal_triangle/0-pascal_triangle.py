#!/usr/bin/python3
""" Pascal's triangle """


def pascal_triangle(n):
    """ returns triangle """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = []
        for j in range(i + 1):
            num = factorial(i)
            den = factorial(j) * factorial(i - j)
            row.append(num // den)

        triangle.append(row)

    return triangle


def factorial(n):
    """ factorial number"""
    if n == 0:
        return 1

    return n * factorial(n - 1)
