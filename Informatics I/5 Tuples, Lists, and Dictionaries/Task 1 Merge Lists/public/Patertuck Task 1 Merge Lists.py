#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
    mergelist = []

    # returns an empty List if minimum one of the Lists is empty
    if a == [] or b == []:
        return []

    # Expands the shorter list by the last element until they are the same length
    if len(a) > len(b):
        while len(a) > len(b):
            b.append(b[-1])

    if len(b) > len(a):
        while len(b) > len(a):
            a.append(a[-1])

    # creates tupels out of every element in the Lists
    for index, val in enumerate(a):
        mergelist.append((val, b[index]))

    return mergelist


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([1], [2]))
