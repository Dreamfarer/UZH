#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def fac(n):
    res = 1
    # Keep in mind, the stop parameter for range is NOT
    # included in the loop. This range only returns up to and
    # including 1.
    for i in range(n, 0, -1):
        print(i)
        res *= i
    # implement this function
    return res


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print("fac({}) = {}".format(8, fac(8)))
