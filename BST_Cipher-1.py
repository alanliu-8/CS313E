#  File: BST_Cipher.py

#  Description: Assignment 21

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 11/15/2020

#  Date Last Modified: 11/15/2020

import sys
from typing import Optional


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.left_node = None  # type: Optional[Node]
        self.right_node = None  # type: Optional[Node]


class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = None
        encrypt_str = encrypt_str.lower()
        for letter in encrypt_str:
            if 97 <= ord(letter) <= 122 or letter == ' ':
                self.insert(letter)

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert(self, ch):
        current_node = self.root
        previous = current_node
        if current_node is None:
            self.root = Node(ch)
        else:
            found = False
            while current_node is not None and not found:
                previous = current_node
                if current_node.data == ch:
                    found = True
                elif current_node.data > ch or ch == ' ':
                    current_node = current_node.left_node
                elif current_node.data < ch:
                    current_node = current_node.right_node
            if not found:
                if previous.data > ch or ch == ' ':
                    previous.left_node = Node(ch)
                else:
                    previous.right_node = Node(ch)

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):
        current_node = self.root
        pathway = ''
        if current_node.data == ch:
            return '*'
        found = False
        while current_node is not None and not found:
            if current_node.data == ch:
                found = True
            elif current_node.data > ch:
                pathway = pathway + '<'
                current_node = current_node.left_node
            elif current_node.data < ch:
                pathway = pathway + '>'
                current_node = current_node.right_node
        if not found:
            return ''
        else:
            return pathway

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        current_node = self.root
        if st == '*':
            return self.root.data
        for iterator in st:
            if current_node is None:
                return ''
            if iterator == '<':
                current_node = current_node.left_node
            if iterator == '>':
                current_node = current_node.right_node
        return current_node.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):
        cleaned_string = st.lower()
        encrypted_letters = []
        for letter in cleaned_string:
            encrypted_letters.append(self.search(letter))
        return '!'.join(encrypted_letters)

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):
        decrypted_string = ''
        clean_str = st.split('!')
        for chain in clean_str:
            decrypted_string += self.traverse(chain)
        return decrypted_string


def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print(the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print(the_tree.decrypt(str_to_decode))


if __name__ == "__main__":
    main()
