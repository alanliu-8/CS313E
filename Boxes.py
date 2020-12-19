#  File: Boxes.py

#  Description: Assignment 12

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 10/15/2020

#  Date Last Modified: 10/15/2020

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes(box_list, sub_set, idx, all_box_subsets):
    current_box = box_list[idx]
    sub_set.append(current_box)
    for other_box_idx in range(idx + 1, len(box_list)):
        other_box = box_list[other_box_idx]
        if does_fit(current_box, other_box):
            sub_sets_boxes(box_list, sub_set.copy(), other_box_idx, all_box_subsets)
    if sub_set not in all_box_subsets:
        all_box_subsets.append(sub_set)
    if idx < len(box_list) - 1:
        sub_sets_boxes(box_list, [], idx + 1, all_box_subsets)


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets(all_box_subsets, largest_size, all_nesting_boxes):
    for subset in all_box_subsets:
        if len(subset) > largest_size:
            largest_size = len(subset)
    for subset in all_box_subsets:
        if len(subset) == largest_size:
            all_nesting_boxes.append(subset)
    return largest_size


# returns True if box1 fits inside box2
def does_fit(box1, box2):
    return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]


def main():
    # read the number of boxes
    in_file = open('boxes.in', 'r')
    line = in_file.readline()
    line = line.strip()
    num_boxes = int(line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range(num_boxes):
        line = in_file.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)

    # close the file
    in_file.close()

    '''
    # print to make sure that the input was read in correctly
    print(box_list)
    print()
    '''

    # sort the box list
    box_list.sort()

    '''
    # print the box_list to see if it has been sorted.
    print(box_list)
    print()
    '''

    # create an empty list to hold all subset of boxes
    all_box_subsets = []

    # create a list to hold a single subset of boxes
    sub_set = []

    # generate all subsets of boxes and store them in all_box_subsets
    sub_sets_boxes(box_list, sub_set, 0, all_box_subsets)

    # initialize the size of the largest sub-set of nesting boxes
    largest_size = 0

    # create a list to hold the largest subsets of nesting boxes
    all_nesting_boxes = []

    # go through all the subset of boxes and only store the
    # largest subsets that nest in all_nesting_boxes
    largest_size = largest_nesting_subsets(all_box_subsets, largest_size, all_nesting_boxes)

    # print the largest number of boxes that fit
    print(largest_size)
    # print the number of sets of such boxes
    print(len(all_nesting_boxes))


if __name__ == "__main__":
    main()
