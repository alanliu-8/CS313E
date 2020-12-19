#  File: ExpressionTree.py

#  Description: Assignment 20

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 11/13/2020

#  Date Last Modified: 11/13/2020

import sys
from typing import Optional, List


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        return len(self.stack) == 0

    def top(self):
        return self.stack[len(self.stack) - 1]


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.left_node = None  # type: Optional[Node]
        self.right_node = None  # type: Optional[Node]


class Tree(object):
    def create_tree(self, expr):
        """
        :type expr: str
        :rtype: Node
        """
        stack = Stack()
        current_node = Node()
        clean_expr = expr.split()
        for token in clean_expr:
            if token == '(':
                current_node.left_node = Node()
                stack.push(current_node)
                current_node = current_node.left_node
            elif token in ['+', '-', '*', '/', '//', '%', '**']:
                current_node.data = token
                stack.push(current_node)
                current_node.right_node = Node()
                current_node = current_node.right_node
            elif token == ')':
                if not stack.empty():
                    current_node = stack.pop()
            else:
                current_node.data = token
                current_node = stack.pop()
        return current_node

    def evaluate(self, aNode):
        """
        :type aNode: Node
        :rtype: float
        """
        token = aNode.data
        if token not in ['+', '-', '*', '/', '//', '%', '**']:
            return float(token)
        left_result = self.evaluate(aNode.left_node)
        right_result = self.evaluate(aNode.right_node)
        if token == '+':
            return left_result + right_result
        if token == '-':
            return left_result - right_result
        if token == '*':
            return left_result * right_result
        if token == '/':
            return left_result / right_result
        if token == '//':
            return left_result // right_result
        if token == '%':
            return left_result % right_result
        if token == '**':
            return left_result ** right_result

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
        tokens.extend(self.pre_order(aNode.left_node))
        tokens.extend(self.pre_order(aNode.right_node))
        return tokens

    def post_order(self, aNode):
        """
        :type aNode: Node
        :rtype: List[str]
        """
        tokens = []
        if aNode is None:
            return tokens
        tokens.extend(self.post_order(aNode.left_node))
        tokens.extend(self.post_order(aNode.right_node))
        tokens.append(aNode.data)
        return tokens


def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    # evaluate the expression and print the result
    test1 = Tree()
    current_node = test1.create_tree(expr)
    print(expr + ' = ' + str(test1.evaluate(current_node)))
    print()
    # get the prefix version of the expression and print
    print("Prefix Expression: " + " ".join(test1.pre_order(current_node)))
    print()
    # get the postfix version of the expression and print
    print("Postfix Expression: " + " ".join(test1.post_order(current_node)))


if __name__ == "__main__":
    main()
