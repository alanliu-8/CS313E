#  File: Work.py

#  Description: Assignment 7

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 9/26/2020

#  Date Last Modified: 10/23/2020

import time
import math


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series(v, k):
    p = 0
    sum = 0
    while v // k ** p != 0:
        sum += v // k ** p
        p += 1
    return sum


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search(n, k):
    v = 0
    sum = 0
    while sum < n:
        v += 1
        sum = sum_series(v, k)
    return v


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search(n, k):
    return ragnorak(0, n, n, k)


def ragnorak(lower, upper, n, k):
    v = lower + ((upper - lower) / 2)
    v_lower = math.floor(v)
    v_upper = math.ceil(v)
    if sum_series(v_lower, k) >= n > sum_series(v_lower - 1, k):
        return v_lower
    elif sum_series(v_upper, k) >= n > sum_series(v_upper - 1, k):
        return v_upper
    sum = sum_series(v_upper, k)
    if sum > n:
        return ragnorak(lower, v_upper, n, k)
    else:
        return ragnorak(v_upper, upper, n, k)


# Input: no work.in
# Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases

    return "all test cases passed"


def main():
    in_file = open("work.in", "r")
    num_cases = int((in_file.readline()).strip())

    for i in range(num_cases):
        inp = (in_file.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


if __name__ == "__main__":
    main()
