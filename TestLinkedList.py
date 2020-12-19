#  File: TestLinkedList.py

#  Description: Assignment 18

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 11/5/2020

#  Date Last Modified: 11/5/2020


class Link(object):
    def __init__(self, data):
        self.data = data
        self.pointer = None


class LinkedList(object):
    # create a linked list
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        link_counter = 0
        x = self.first
        while x is not None:
            link_counter += 1
            x = x.pointer
        return link_counter

    # add an item at the beginning of the list
    def insert_first(self, data):
        x = Link(data)
        x.pointer = self.first
        self.first = x

    # add an item at the end of a list
    def insert_last(self, data):
        x = self.first
        if self.first is None:
            return self.insert_first(data)
        while x.pointer is not None:
            x = x.pointer
        x.pointer = Link(data)

    # add an item in an ordered list in ascending order
    def insert_in_order(self, data):
        x = self.first
        previous = None
        if self.first is None:
            return self.insert_first(data)
        while x.data < data:
            if x.pointer is None:
                x.pointer = Link(data)
                return
            previous = x
            x = x.pointer
        if previous is None:
            return self.insert_first(data)
        previous.pointer = Link(data)
        previous.pointer.pointer = x

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        x = self.first
        while x is not None:
            if x.data == data:
                return x.data
            x = x.pointer
        return None

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        x = self.first
        while x is not None:
            if x.data == data:
                return x.data
            if x.data < data:
                break
            x = x.pointer
        return None

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        x = self.first
        previous = None
        while x is not None:
            if x.data == data:
                skip = x.pointer
                if previous is None:
                    self.first = skip
                else:
                    previous.pointer = skip
                return x
            previous = x
            x = x.pointer
        return None

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        x = self.first
        string = ''
        tracker = 0
        if x is None:
            return string
        while x.pointer is not None:
            string = string + str(x.data) + '  '
            x = x.pointer
            tracker += 1
            if tracker == 10:
                string = string + '\n'
                tracker = 0
        return string + str(x.data)

    # Copy the contents of a list and return new list
    def copy_list(self):
        x = self.first
        new_list = LinkedList()
        while x is not None:
            new_list.insert_last(x.data)
            x = x.pointer
        return new_list

    # Reverse the contents of a list and return new list
    def reverse_list(self):
        x = self.first
        reversal = LinkedList()
        while x is not None:
            reversal.insert_first(x.data)
            x = x.pointer
        return reversal

    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        x = self.first
        sorted_list = LinkedList()
        while x is not None:
            sorted_list.insert_in_order(x.data)
            x = x.pointer
        return sorted_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        x = self.first
        while x is not None:
            if x.pointer is None:
                return True
            if x.data <= x.pointer.data:
                x = x.pointer
            else:
                break
        return False

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        return self.first is None

    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        merged_list = self.copy_list()
        other_copy = other.copy_list()
        while not other_copy.is_empty():
            merged_list.insert_in_order(other_copy.first.data)
            other_copy.delete_link(other_copy.first.data)
        return merged_list

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        """
        :type other: LinkedList
        """
        x = self.first
        y = other.first
        biggest_list = max(self.get_num_links(), other.get_num_links())
        for idx in range(biggest_list):
            if x is None or y is None:
                return False
            if x.data == y.data:
                x = x.pointer
                y = y.pointer
            else:
                return False
        return True

    # Return a new list, keeping only the first occurrence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        x = self.first
        cut_list = LinkedList()
        while x is not None:
            if not cut_list.find_unordered(x.data):
                cut_list.insert_last(x.data)
            x = x.pointer
        return cut_list


def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    test1 = LinkedList()
    test5 = LinkedList()
    for x in range(20):
        test1.insert_first(x)
    print(test1)
    print(test5)
    # Test method insert_last()
    test2 = LinkedList()
    for x in range(20):
        test2.insert_last(x)
    print(test2)
    # Test method insert_in_order()
    test3 = LinkedList()
    test3.insert_last(12)
    test3.insert_last(99)
    test3.insert_last(37)
    test3.insert_in_order(12)
    print(test3)
    # Test method get_num_links()
    test4 = LinkedList()
    print(test3.get_num_links())
    print(test4.get_num_links())
    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    test6 = LinkedList()
    test6.insert_last(12)
    test6.insert_last(99)
    test6.insert_last(37)
    print(test6.find_unordered(12))
    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    test7 = LinkedList()
    test7.insert_last(12)
    test7.insert_last(37)
    test7.insert_last(99)
    print(test7.find_ordered(99))
    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    test8 = LinkedList()
    test8.insert_last(12)
    test8.insert_last(37)
    test8.insert_last(99)
    test8.delete_link(37)
    print(test8)
    # Test method copy_list()
    test9 = LinkedList()
    test9.insert_last(23)
    test9.insert_last(52)
    test9.insert_last(101)
    print(test9.copy_list())
    # Test method reverse_list()
    test10 = LinkedList()
    test10.insert_last(23)
    test10.insert_last(52)
    test10.insert_last(101)
    print(test10.reverse_list())
    # Test method sort_list()
    test11 = LinkedList()
    for x in [2592, 5, 13, 89, 72, 23, 5, 1]:
        test11.insert_last(x)
    print(test11.sort_list())
    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    test12 = LinkedList()
    for x in [1, 1, 4, 9, 15, 15, 2097, 2098]:
        test12.insert_last(x)
    print(test12.is_sorted())
    # Test method is_empty()
    test13 = LinkedList()
    test13.insert_last(1)
    print(test13.is_empty())
    # Test method merge_list()
    test14 = LinkedList()
    for x in [1, 3, 5, 7, 9]:
        test14.insert_last(x)
    test14_1 = LinkedList()
    for x in [2, 4, 6, 8, 10]:
        test14_1.insert_last(x)
    print(test14.merge_list(test14_1))
    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    test15 = LinkedList()
    test15_1 = LinkedList()
    for x in [1, 3, 5, 7, 9]:
        test15.insert_last(x)
    for x in [1, 3, 5, 7, 9]:
        test15_1.insert_last(x)
    print(test15.is_equal(test15_1))
    # Test remove_duplicates()
    test16 = LinkedList()
    for x in [1, 1, 5, 8, 10, 9, 7, 7, 7, 3, 5, 7, 9]:
        test16.insert_last(x)
    print(test16.remove_duplicates())


if __name__ == "__main__":
    main()
