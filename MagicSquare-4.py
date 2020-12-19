#  File: MagicSquare.py

#  Description: Assignment 13

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 10/16/2020

#  Date Last Modified: 10/16/2020

from itertools import permutations
import math

square_size = 0
magic_num = 0


# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic(a):
    diag1 = 0
    diag2 = 0
    global square_size
    global magic_num
    for idx in range(square_size):
        col_sum = 0
        row_sum = 0
        idx_jumper = idx
        for cell in range(square_size):
            col_sum += a[idx_jumper]
            idx_jumper += square_size
        if col_sum != magic_num:
            return False
        for cell in range(square_size):
            row_sum += a[idx * square_size + cell]
        if row_sum != magic_num:
            return False
    for idx in range(0, len(a), square_size + 1):
        diag1 += a[idx]
    if diag1 != magic_num:
        return False
    for idx in range(square_size - 1, len(a) - 1, square_size - 1):
        diag2 += a[idx]
    if diag2 != magic_num:
        return False
    return True


# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# it stores all 1-D lists that are magic in the list all_magic
def permute(a, idx, all_magic):
    global square_size, magic_num
    square_size = int(math.sqrt(len(a)))
    magic_num = round(square_size * (square_size ** 2 + 1) / 2)
    for perm in permutations(a):
        if is_magic(perm):
            all_magic.append(list(perm))
    return


def main():
    # read the dimension of the magic square
    in_file = open('magic.in', 'r')
    line = in_file.readline()
    line = line.strip()
    n = int(line)
    in_file.close()

    # check if you read the input correctly
    print(n)

    # create an empty list for all magic squares
    all_magic = []

    # create the 1-D list that has the numbers 1 through n^2
    start_list = list(range(1, n ** 2 + 1))
    # generate all magic squares using permutation
    permute(start_list, 0, all_magic)
    # print all magic squares
    for perm in all_magic:
        print(perm)


if __name__ == "__main__":
    main()
