#  File: Chess.py

#  Description: Assignment 14

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 10/22/2020

#  Date Last Modified: 10/23/2020

import sys

DIRECTIONS = {
    'North': (-1, 0),
    'Northeast': (-1, +1),
    'East': (0, +1),
    'Southeast': (+1, +1),
    'South': (+1, 0),
    'Southwest': (+1, -1),
    'West': (0, -1),
    'Northwest': (-1, -1)
}


class Queens(object):
    def __init__(self, n=8):
        self.board = []
        self.n = n
        self.solutions = 0
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()
        print()

    # check if a position on the board is valid
    def is_valid(self, row: int, col: int) -> bool:
        for direction_name, direction_tuple in DIRECTIONS.items():
            x1 = row
            y1 = col
            while True:
                x1 += direction_tuple[0]
                y1 += direction_tuple[1]
                if x1 >= self.n or y1 >= self.n:
                    break
                if x1 < 0 or y1 < 0:
                    break
                if self.board[x1][y1] == 'Q':
                    return False
        return True

    # do the recursive backtracking
    def recursive_solve(self, col: int) -> bool:
        if col == self.n:
            return True
        for i in range(self.n):
            if self.is_valid(i, col):
                self.board[i][col] = 'Q'
                if self.recursive_solve(col + 1):
                    self.solutions += 1
                self.board[i][col] = '*'
        return False

    # if the problem has a solution print the board
    def solve(self):
        self.recursive_solve(0)


def main():
    # read the size of the board
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create a chess board
    game = Queens(n)

    # place the queens on the board and count the solutions
    game.solve()

    # print the number of solutions
    print(game.solutions)


if __name__ == "__main__":
    main()
