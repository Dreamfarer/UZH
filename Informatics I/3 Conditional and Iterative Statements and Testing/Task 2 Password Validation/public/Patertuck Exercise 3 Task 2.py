# Exercise 3 Task 2

# !/usr/bin/env python3

pwd = "abcdefg323"


def is_valid():
    # You need to change the following part of the function
    # to determine if it is a valid password.
    lowercount = 0
    uppercount = 0
    numbercount = 0
    specialcount = 0
    error = True

    # counts every type of character in the input string
    for character in pwd:
        if character in "abcdefghijklmnopqrstuvwxyz":
            lowercount += 1
        elif character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercount += 1
        elif character in "0123456789":
            numbercount += 1
        elif character in "+-*/":
            specialcount += 1

            # special case if the character is not a letter, numer, +, -, or /
        else:
            error = False
            break

    # returns True if the pwd matches the given conditions
    return 7 < len(pwd) < 17 and error and lowercount > 1 and uppercount > 1 and numbercount > 1 and specialcount > 1


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid())
