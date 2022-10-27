#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def absolute_value(a):
    # implement this function
    if a < 0:
        return a * -1
    return a

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gcd(a, b):
    a = absolute_value(a)
    b = absolute_value(b)
    # implement this function
    if a == 0 == b:
        return None
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a % b)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = 33
b = 17
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")

