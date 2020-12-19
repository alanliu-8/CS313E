#  File: Triangle.py

#  Description: Assignment 15

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 10/24/2020

#  Date Last Modified: 10/24/2020

import sys

from timeit import timeit


# returns the greatest path sum using exhaustive search
def brute_force(grid):
    num_paths = 2 ** (len(grid) - 1)
    max_sum = forcibly(grid, len(grid) - 1, 0, 0)
    index = 1
    # generate the sum of every path, compare to the current maximum
    while index < num_paths:
        current_sum = forcibly(grid, 0, index, 0)
        if current_sum > max_sum:
            max_sum = current_sum
        index += 1
    return max_sum


def forcibly(grid, depth, index, col):
    if depth == len(grid) - 1:
        return grid[depth][col]
    move = index / (1 << (len(grid) - 2 - depth))
    index = index % (1 << (len(grid) - 2 - depth))
    if move >= 1:
        return grid[depth][col] + forcibly(grid, depth + 1, index, col + 1)
    return grid[depth][col] + forcibly(grid, depth + 1, index, col)

# returns the greatest path sum using greedy approach
def greedy(grid):
    row = col = path_sum = 0
    while row != len(grid) - 1:
        path_sum += grid[row][col]
        if grid[row + 1][col + 1] > grid[row + 1][col]:
            col += 1
        row += 1
    path_sum += grid[row][col]
    return path_sum


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    return conquer_helper(0, 0, grid)


def conquer_helper(row, col, grid):
    if row == len(grid) - 1:
        return grid[row][col]
    return grid[row][col] + max(conquer_helper(row + 1, col, grid), conquer_helper(row + 1, col + 1, grid))


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    sum_grid = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    large_num_sum(0, 0, 0, sum_grid, grid)
    return max(sum_grid[len(grid) - 1][:len(grid)])


def large_num_sum(row, col, running_sum, sum_grid, grid):
    running_sum += grid[row][col]
    if running_sum < sum_grid[row][col]:
        return
    sum_grid[row][col] = running_sum
    if row == len(grid) - 1:
        return
    down_value = grid[row + 1][col]
    right_value = grid[row + 1][col + 1]
    if down_value >= right_value:
        large_num_sum(row + 1, col, running_sum, sum_grid, grid)
        large_num_sum(row + 1, col + 1, running_sum, sum_grid, grid)
    else:
        large_num_sum(row + 1, col + 1, running_sum, sum_grid, grid)
        large_num_sum(row + 1, col, running_sum, sum_grid, grid)


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    '''
    # check that the grid was read in properly
    print(grid)
    '''

    # output greatest path from exhaustive search
    times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
    times = times / 10
    # print time taken using exhaustive search
    print('The greatest path sum through exhaustive search is \n%s' % brute_force(grid))
    print('The time taken for exhaustive search in seconds is\n%s' % times)
    print()
    # output greatest path from greedy approach
    times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
    times = times / 10
    # print time taken using greedy approach
    print('The greatest path sum through greedy search is \n%s' % greedy(grid))
    print('The time taken for greedy approach in seconds is\n%s' % times)
    print()
    # output greatest path from divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
    times = times / 10
    # print time taken using divide-and-conquer approach
    print('The greatest path sum through recursive search is \n%s' % divide_conquer(grid))
    print('The time taken for recursive search in seconds is \n%s' % times)
    print()
    # output greatest path from dynamic programming
    times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    # print time taken using dynamic programming
    print('The greatest path sum through dynamic programming is \n%s' % dynamic_prog(grid))
    print('The time taken for dynamic programming in seconds is\n%s' % times)


if __name__ == "__main__":
    main()
