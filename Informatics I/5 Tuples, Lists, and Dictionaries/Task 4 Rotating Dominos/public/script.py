#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):

    # Return -1 if they don't have the same length
    if not len(top) == len(bottom): return -1

    # Temporery extend the list, 'cause we need to find the number which appears the most
    temporary_list = top + bottom

    # Find the element that occurs the most
    most_occurances = max(set(temporary_list), key = temporary_list.count) # Don't ask me: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/

    # Find out if we should rotate top or bottom
    if top.count(most_occurances) <= bottom.count(most_occurances): turns = top.count(most_occurances)
    else: turns = bottom.count(most_occurances)

    # Compensate for dominos that have the same number on both sides
    index = 0
    while index < len(top):
        if top[index] == bottom[index] and top[index] == most_occurances: 
            turns -= 1
        index += 1

    # Check that one row, either the top or the bottom, has the same numbers
    if max(top.count(most_occurances), bottom.count(most_occurances)) + turns < len(top):
        return -1

    return turns

# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))