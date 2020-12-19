#  File: TestBinaryTree.py

#  Description: Assignment 22

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/na

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 11/20/2020

#  Date Last Modified: 11/20/2020

import sys
from typing import Optional


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None  # type: Optional[Node]
        self.right_child = None  # type: Optional[Node]
        # self.parent = None
        # self.visited = False


class Tree(object):
    def __init__(self):
        self.root = None

    # insert data into the tree
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while current is not None:
                parent = current
                if data < current.data:
                    current = current.left_child
                else:
                    current = current.right_child

            # found location now insert node
            if data < parent.data:
                parent.left_child = new_node
            else:
                parent.right_child = new_node

    # search for a node with given data
    def find(self, data):
        current = self.root
        while (current is not None) and (current.data != data):
            if data < current.data:
                current = current.left_child
            else:
                current = current.right_child
        return current

    # find the node with the minimum key
    def find_min(self):
        current = self.root
        parent = self.root
        while current is not None:
            parent = current
            current = current.left_child
        return parent

    # find the node with the maximum key
    def find_max(self):
        current = self.root
        parent = self.root
        while current is not None:
            parent = current
            current = current.right_child
        return parent

    # in order traversal - left, center, right
    def in_order(self, aNode):
        if aNode is not None:
            self.in_order(aNode.left_child)
            print(aNode.data)
            self.in_order(aNode.right_child)

    # pre order traversal - center, left, right
    def pre_order(self, aNode):
        """
        :type aNode: Node
        :rtype: List[str]
        """
        tokens = []
        if aNode is None:
            return tokens
        token = aNode.data
        tokens.append(token)
        tokens.extend(self.pre_order(aNode.left_child))
        tokens.extend(self.pre_order(aNode.right_child))
        return tokens

    # post order traversal - left, right, center
    def post_order(self, aNode):
        """
        :type aNode: Node
        :rtype: List[str]
        """
        tokens = []
        if aNode is None:
            return tokens
        tokens.extend(self.post_order(aNode.left_child))
        tokens.extend(self.post_order(aNode.right_child))
        tokens.append(aNode.data)
        return tokens

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        return self.pre_order(self.root) == self.pre_order(pNode)

    # Prints out all nodes at the given level
    def print_level(self, level):
        print(self.cursive_get_level(level, self.root, 0))

    def cursive_get_level(self, level, node, current_level):
        """
        :type current_level: int
        :type node: Node
        :type level: int
        """
        level_collect = []
        if node is None:
            return []
        if current_level != level:
            level_collect.extend(self.cursive_get_level(level, node.left_child, current_level + 1))
            level_collect.extend(self.cursive_get_level(level, node.right_child, current_level + 1))
        if current_level == level:
            if node.data is not None:
                level_collect.append(node.data)
        return level_collect

    # Returns the height of the tree
    def get_height(self):
        return self.recursive_get_height(self.root, 0)

    def recursive_get_height(self, current_node, current_height):
        left_max = right_max = 0
        if current_node.left_child is None and current_node.right_child is None:
            return current_height
        if current_node.left_child is not None:
            left_max = self.recursive_get_height(current_node.left_child, current_height + 1)
        if current_node.right_child is not None:
            right_max = self.recursive_get_height(current_node.right_child, current_height + 1)
        return max(left_max, right_max)

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        left_nodes = right_nodes = 0
        if self.root.left_child is not None:
            left_nodes = self.recursive_num_nodes(self.root.left_child)
        if self.root.right_child is not None:
            right_nodes = self.recursive_num_nodes(self.root.right_child)
            right_nodes += 1
        return left_nodes, right_nodes

    def recursive_num_nodes(self, current_node):
        left_sum = right_sum = 0
        if current_node.left_child is not None:
            left_sum = self.recursive_num_nodes(current_node.left_child)
        if current_node.right_child is not None:
            right_sum = self.recursive_num_nodes(current_node.right_child)
        return left_sum + right_sum + 1


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints

    # Creation of trees
    tree1 = Tree()
    for num in tree1_input:
        tree1.insert(num)
    tree2 = Tree()
    for num in tree2_input:
        tree2.insert(num)
    tree3 = Tree()
    for num in tree3_input:
        tree3.insert(num)

    # The input of the samples cases and answers provided are:
    # tree1: 50 30 70 10 40 60 80 7 25 38 47 58 65 77 96
    # tree2: 50 30 70 10 40 60 80 7 25 38 47 58 65 77 96
    # tree3: 58 77 65 30 38 50 7 25 47 96 80 10 60 70 40

    # Test your method is_similar()
    # Test is_similar for every combination of trees
    print('Test 1: is_similar')
    print(tree1.is_similar(tree2.root))
    print(tree1.is_similar(tree3.root))

    print(tree2.is_similar(tree1.root))
    print(tree2.is_similar(tree3.root))

    print(tree3.is_similar(tree1.root))
    print(tree3.is_similar(tree2.root))
    print()  # if you need it to ensure the print_levels are on two different lines

    # Results should be
    # True
    # False
    # True
    # False
    # False
    # False

    # Print the various levels of two of the trees that are different
    print('Test 2: print_level')
    tree1.print_level(2)  # assumed to print out on one line
    tree2.print_level(2)  # assumed to print out on one line

    # Answer to printing level two for both tree1 and tree2 should be [10, 40, 60, 80]

    tree1.print_level(5)  # assumed to print out on one line
    tree3.print_level(0)  # assumed to print out on one line
    tree3.print_level(3)  # assumed to print out on one line
    print()  # if you need it to ensure the print_levels are on two different lines

    # Answer to the printing levels should be a blank list [] for printing level 5 of tree1
    # Answer to printing level 0 of tree3 should be [58]
    # Answer to printing level 3 of tree3 should be [25, 50, 60, 70, 80]

    # Get the height of the two trees that are different
    print('Test 3: get_height')
    print(tree1.get_height())
    print(tree2.get_height())
    print(tree3.get_height())
    print()  # if you need it to ensure the print_levels are on two different lines

    # Answer to the heights of the trees should be 3, 3, 5

    # Get the total number of nodes a binary search tree
    print('Test 4: num_nodes')
    print(tree1.num_nodes())
    print(tree2.num_nodes())
    print(tree3.num_nodes())

    # Answer to the number of left/right nodes in a tuple format should be (7,8), (7,8), (8,7). The left side of the
    # tuple indicates the number of left side nodes and the right side of the tuple indicates the number of
    # right side nodes with the inclusion of the root node


if __name__ == "__main__":
    main()
