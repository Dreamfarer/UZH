#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def fac(n):
    # implement this function
    res = 1
    if fac == 1:
        return 0
    while n > 0:
        res = res * n
        n = n - 1
    return res


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print("fac({}) = {}".format(4, fac(4)))

