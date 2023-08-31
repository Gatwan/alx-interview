#!/usr/bin/python3
""" Returns island perimeter """


def island_perimeter(grid):
    """ Checks perimeter """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += front_per(grid, i, j)
                perimeter += back_per(grid, i, j)
                perimeter += right_per(grid, i, j)
                perimeter += left_per(grid, i, j)

    return perimeter


def front_per(grid, i, j):
    """ Checks front perimeter """
    if i == 0:
        return 0

    if grid[i - 1][j] == 0:
        return 1

    return 0


def right_per(grid, i, j):
    """ Checks right perimeter """
    if j == len(grid[i]) - 1:
        return 0

    if grid[i][j + 1] == 0:
        return 1

    return 0


def back_per(grid, i, j):
    """ Checks back perimeter """
    if i == len(grid) - 1:
        return 0

    if grid[i + 1][j] == 0:
        return 1

    return 0


def left_per(grid, i, j):
    """ Checks left perimeter """
    if j == 0:
        return 0

    if grid[i][j - 1] == 0:
        return 1

    return 0
