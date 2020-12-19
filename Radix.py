#  File: Radix.py

#  Description: Assignment 17

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 10/30/2020

#  Date Last Modified: 11/2/2020

import sys


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue if empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort(a):
    queues = {}
    ordered = []
    lastq = Queue()
    for string in a:
        lastq.enqueue(string)
    passes = len(max(a, key=len))
    for idx in range(passes):
        while not lastq.is_empty():
            string = lastq.dequeue()
            padder = passes - idx - 1
            if padder >= len(string):
                asci = 0
            else:
                cell = string[padder]
                asci = ord(cell)
            if asci not in queues:
                queues[asci] = Queue()
            queues[asci].enqueue(string)
        for key in sorted(queues.keys()):
            while not queues[key].is_empty():
                current = queues[key].dequeue()
                lastq.enqueue(current)
    while not lastq.is_empty():
        ordered.append(lastq.dequeue())
    return ordered


def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int(line)

    # create a word list
    word_list = []
    for i in range(num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append(word)

    '''
    # print word_list
    print (word_list)
    '''

    # use radix sort to sort the word_list
    sorted_list = radix_sort(word_list)

    # print the sorted_list
    print(sorted_list)


if __name__ == "__main__":
    main()
