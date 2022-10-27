#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):
    most_number = 0
    rotations = 0

    # calculates the most common number
    for number in range(1, 7):
        if top.count(number) > most_number or bottom.count(number) > most_number:
            most_number = number

    # checks if the most common number is available on every domino, returns -1 if there is not
    for (top_number, bottom_number) in zip(top, bottom):
        if top_number != most_number and bottom_number != most_number:
            return -1

    # calculates the amount of rotations needed
    if top.count(most_number) >= bottom.count(most_number):
        return len(top) - top.count(most_number)
    return len(bottom) - bottom.count(most_number)


# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
