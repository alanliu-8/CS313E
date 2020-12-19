# File: Fibonacci.py

# Description: Assignment 10

# Student's Name: Alan Liu

# Student's UT EID: ael2695

# Partner's Name: n/a

# Partner's UT EID: n/a

# Course Name: CS 313E

# Unique Number: 50850

# Date Created: 10/8/2020

# Date Last Modified: 10/8/2020

import sys
import time


def decoration(func):
    memory = {}

    def cached_f(n):
        if n not in memory:
            memory[n] = func(n)
        return memory[n]

    return cached_f


# Input: n a positive integer
# Output: a bit string
@decoration
def f(n: int) -> str:
    if n == 0:
        return str(n)
    if n == 1:
        return str(n)
    if n > 1:
        return f(n - 1) + f(n - 2)


# Input: s and p are bit strings
# Output: an integer that is the number of times p occurs in s
def count_overlap(s, p):
    counter = 0
    if len(s) == 0:
        return 0
    for index in range(len(s) - len(p)):
        if s[index:index + len(p)] == p:
            counter += 1
    return counter


def main():
    n = int(sys.stdin.readline())
    p = sys.stdin.readline().strip()

    # start = time.time()
    bit_string = f(n)
    # end = time.time()
    occurrences = count_overlap(bit_string, p)
    print(occurrences)
    # print("Took %s seconds" % (end - start))


if __name__ == "__main__":
    main()
