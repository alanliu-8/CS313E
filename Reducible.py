#  File: Reducible.py

#  Description: Assignment 16

#  Student Name: Alan Liu

#  Student UT EID: ael2695

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 10/28/2020

#  Date Last Modified: 10/30/2020


# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime(n):
    if n == 1:
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True


# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


def memoize(f):
    memo = {}

    def helper(x, num):
        if x not in memo:
            memo[x] = f(x, num)
        return memo[x]

    return helper


# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
@memoize
def step_size(s, const):
    return const - (hash_word(s, const) % const)


# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word(s, hash_table):
    index = hash_word(s, len(hash_table))
    while hash_table[index] != '':
        index += step_size(s, 13)
        if index >= len(hash_table):
            index -= len(hash_table)
    hash_table[index] = s


# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word(s, hash_table):
    idx = hash_word(s, len(hash_table))
    while hash_table[idx] != '':
        if hash_table[idx] == s:
            return True
        idx += step_size(s, 13)
        if idx >= len(hash_table):
            idx -= len(hash_table)
    return False


# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
def is_reducible(s, hash_table, hash_memo):
    if find_word(s, hash_memo):
        return True
    if not ('a' in s or 'i' in s or 'o' in s):
        return False
    for idx in range(len(s)):
        concat_word = s[0:idx] + s[idx + 1:]
        if len(concat_word) == 1:
            if concat_word in ('a', 'i', 'o'):
                return True
        if find_word(concat_word, hash_table):
            if is_reducible(concat_word, hash_table, hash_memo):
                insert_word(concat_word, hash_memo)
                return True
    return False


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words(string_list):
    pass


def main():
    # create an empty word_list
    # read words from words.txt and append to word_list
    word_list = [line.rstrip() for line in open("words.txt")]
    # find length of word_list
    total_words = len(word_list)
    # determine prime number N that is greater than twice
    # the length of the word_list
    prime_num_start = 2 * total_words
    while not is_prime(prime_num_start):
        prime_num_start += 1
    # create an empty hash_list
    # populate the hash_list with N blank strings
    hash_list = [''] * prime_num_start
    # hash each word in word_list into hash_list
    for word in word_list:
        insert_word(word, hash_list)
    # for collisions use double hashing

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than
    # 0.2 * size of word_list
    second_prime = int(0.2 * total_words)
    while not is_prime(second_prime):
        second_prime += 1
    # populate the hash_memo with M blank strings
    hash_memo = [''] * second_prime
    # create an empty list reducible_words
    reducible_words = []
    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)
    # find words of length 10 in reducible_words
    ordered_list = []
    for word in reducible_words:
        if len(word) == 10:
            ordered_list.append(word)
    # print the words of length 10 in alphabetical order
    # one word per line
    ordered_list.sort()
    for idx in ordered_list:
        print(idx)


if __name__ == "__main__":
    main()
