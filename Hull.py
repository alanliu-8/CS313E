#  File: Hull.py

#  Description: Assignment 6

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 9/22/2020

#  Date Last Modified: 10/23/2020

import math
import sys

from typing import List


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y < other.y)
        return (self.x < other.x)

    def __le__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)


# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det(p, q, r):
    return ((q.x * r.y) - (q.y * r.x)) - (p.x * ((1 * r.y) - (q.y * 1))) + (p.y * ((1 * r.x) - (q.x * 1)))


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull(sorted_points: List[Point]):
    upper_hull = [sorted_points[0], sorted_points[1]]
    for point in sorted_points[2:]:
        upper_hull.append(point)
        while len(upper_hull) >= 3 and not is_turning_right(upper_hull[-3:]):
            upper_hull.pop(-2)

    lower_hull = [sorted_points[-1], sorted_points[-2]]
    for point in reversed(sorted_points[:-2]):
        lower_hull.append(point)
        while len(lower_hull) >= 3 and not is_turning_right(lower_hull[-3:]):
            lower_hull.pop(-2)
    lower_hull.pop(0)
    lower_hull.pop()
    upper_hull.extend(lower_hull)
    return upper_hull


def is_turning_right(provided_hull: List[Point]):
    return det(*provided_hull[0:3]) < 0


# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly(convex_poly: List[Point]):
    convex_poly_len = len(convex_poly)
    if convex_poly_len >= 3:
        poly_det = 0
        i = j = 0
        while i < convex_poly_len - 1:
            poly_det += (convex_poly[i].x * convex_poly[i + 1].y)
            i += 1
        # Wraps matrix calculation back to the beginning
        poly_det += (convex_poly[-1].x * convex_poly[0].y)
        while j < convex_poly_len - 1:
            poly_det -= (convex_poly[j].y * convex_poly[j + 1].x)
            j += 1
        # Wraps matrix calculation back to the beginning
        poly_det -= (convex_poly[-1].y * convex_poly[0].x)
        poly_area = (1 / 2) * math.fabs(poly_det)
        return poly_area
    return 0


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases

    return "all test cases passed"


def main(coords):
    my_points = []
    for x, y in coords:
        my_points.append(Point(x, y))
    return my_main(my_points)


def my_main(my_points):
    # # create an empty list of Point objects
    # my_points = []
    # # read data from standard input
    # total_coords = int(sys.stdin.readline())
    # # read line by line, create Point objects and store in a list
    # for points in range(total_coords + 1):
    #     x_y_iter = map(lambda x: int(x), sys.stdin.readline().split())
    #     my_points.append(Point(*x_y_iter))

    # sort the list according to x-coordinates
    my_points.sort(key=lambda point: (point.x, point.y))
    # get the convex hull
    convex_points = convex_hull(my_points)
    # run your test cases
    test_cases()
    # print your results to standard output
    # print the convex hull
    print('Convex Hull')
    for point in convex_points:
        print(point)
    # get the area of the convex hull
    convex_area = area_poly(convex_points)
    # print the area of the convex hull
    print()
    print('Area of Convex Hull =', convex_area)

    return convex_points


if __name__ == "__main__":
    # create an empty list of Point objects
    my_points = []
    # read data from standard input
    total_coords = int(sys.stdin.readline())
    # read line by line, create Point objects and store in a list
    for points in range(total_coords + 1):
        x_y_iter = map(lambda x: int(x), sys.stdin.readline().split())
        my_points.append(Point(*x_y_iter))
    my_main(my_points)
