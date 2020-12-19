#  File: Grid.py

#  Description: Assignment 8

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 9/29/2020

#  Date Last Modified: 10/23/2020

import sys
import math
from decimal import Decimal


# counts all the possible paths in a grid
def count_paths(n):
    length = len(n) - 1
    return Decimal(math.factorial(length + length)) / Decimal(math.factorial(length) * math.factorial(length))


# gets the greatest sum of all the paths in the grid
def path_sum(grid, n):
    sum_grid = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    large_num_sum(0, 0, 0, sum_grid, grid)
    return sum_grid[len(grid) - 1][len(grid) - 1]


def large_num_sum(x, y, running_sum, sum_grid, grid):
    running_sum += grid[x][y]
    if running_sum < sum_grid[x][y]:
        return
    sum_grid[x][y] = running_sum
    if x == len(grid) - 1 and y == len(grid) - 1:
        return
    if x + 1 > len(grid) - 1:
        down_value = -1
    else:
        down_value = grid[x + 1][y]
    if y + 1 > len(grid) - 1:
        right_value = -1
    else:
        right_value = grid[x][y + 1]
    if down_value >= right_value:
        large_num_sum(x + 1, y, running_sum, sum_grid, grid)
        if right_value != -1:
            large_num_sum(x, y + 1, running_sum, sum_grid, grid)
    else:
        large_num_sum(x, y + 1, running_sum, sum_grid, grid)
        if down_value != -1:
            large_num_sum(x + 1, y, running_sum, sum_grid, grid)


def main():
    # read data from standard input
    dim = []
    dimensions = int(sys.stdin.readline())
    for row in range(dimensions):
        num = list(map(lambda x: int(x), sys.stdin.readline().split()))
        dim.append(num)
    # get the number of paths in the grid and print
    num_paths = count_paths(dim)
    print(num_paths)
    print()

    # get the maximum path sum and print
    max_path_sum = path_sum(dim, dim)
    print(max_path_sum)


if __name__ == "__main__":
    main()
