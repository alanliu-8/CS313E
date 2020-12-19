#  File: Josephus.py

#  Description: Assignment 19

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 11/9/2020

#  Date Last Modified: 11/10/2020

import sys


class Link(object):
    def __init__(self, data):
        self.data = data
        self.pointer = None

    def __str__(self):
        output = str(self.data)
        if self.pointer is not None:
            output += " => " + str(self.pointer.data)
        return output


class CircularList(object):
    # Constructor
    def __init__(self):
        self.last_pointer = None

    # Insert an element (value) in the list
    def insert(self, data):
        x = Link(data)
        if self.last_pointer is None:
            self.last_pointer = x
            self.last_pointer.pointer = x
            return
        previous = self.last_pointer.pointer
        self.last_pointer.pointer = x
        x.pointer = previous
        self.last_pointer = x

    # Find the link with the given data (value)
    def find(self, data):
        x = self.last_pointer
        while x.data is not data:
            if x.pointer is self.last_pointer:
                return None
            x = x.pointer
        return x

    # Delete a link with a given data (value)
    def delete(self, data):
        x = self.last_pointer
        previous = None
        while x.data is not data:
            if x.pointer is self.last_pointer:
                return None
            previous = x
            x = x.pointer
        skip = self.last_pointer.pointer
        previous.pointer = skip

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
    def delete_after(self, start, n):
        """
        :type start: Link
        :type n: int
        """
        x = start
        previous = None
        for _ in range(n - 1):
            previous = x
            x = x.pointer
        skip = x.pointer
        previous.pointer = skip
        print(x.data)
        return skip

    # Return a string representation of a Circular List
    def __str__(self):
        x = self.last_pointer
        string = ''
        if x is None:
            return string
        while x.pointer is not self.last_pointer:
            string = string + str(x.data) + ' '
            x = x.pointer
        return string + str(x.data)


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # your code
    test = CircularList()
    for soldier in range(1, num_soldiers + 1):
        test.insert(soldier)
    start_link = test.find(start_count)
    for _ in range(num_soldiers):
        start_link = test.delete_after(start_link, elim_num)


if __name__ == "__main__":
    main()
