#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
    '''
    Takes two lists as parameters, merge them and return a list
    '''
    mergelist = []

    # If one or both lists are empty, the empty list should be returned.
    if len(a) == 0 or len(b) == 0:
        return []

    # Make sure a is always larger than b
    flipped = False # remember if we flipped a and b (important for later)
    if len(b) > len(a):
        a, b = b, a
        flipped = True

    # Loop over the longer list (in our case always a)
    for index in range(len(a)):
        
        # Assign the first number
        first = a[index] 

        # Assign the second number
        if index > len(b) - 1: second = b[len(b) - 1]
        else: second = b[index]

        # Flip them around if you have flipped a and b before
        if flipped == True: first, second = second, first

        # Put the variables into a new list
        mergelist.append((first, second))

    return mergelist

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0, 1, 2], [5, 6]))
