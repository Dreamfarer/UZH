#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def fac(n):

    # implement this function
    if n == 0: return 1 # Stop calling the function recursively if the base case has been reached
    return n * fac(n-1) # Multiply the current 'n' with the, from the function call, returned factorial of 'n-1'

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print("fac({}) = {}".format(8, fac(8)))