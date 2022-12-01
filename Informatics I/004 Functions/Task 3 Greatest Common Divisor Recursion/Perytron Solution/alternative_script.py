#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def absolute_value(a):
    # ... okay then
    return abs(a)

def gcd(a, b):
    # --> The gcd(a,b) function should be able to handle mistakenly entered negative
    # numbers by converting them to positives
    # To achieve this, the gcd(a,b) should leverage the absolute_value(a) function
    a = absolute_value(a)
    b = absolute_value(b)
    # --> If a and b is zero, None should be returned
    if a == 0 and b == 0:
        return None
    # --> If either a or b is zero, but not both, the absolute value of the parameter
    # which is not zero should be returned
    elif a == 0:
        return b
    elif b == 0:
        return a
    # --> gcd(a,b) should work in both cases a < b and a > b
    # b must be <= a for this to work
    if a < b:
        swap_tuple = (b, a)
        # array destructuring
        a, b = swap_tuple
    # once we reached the greatest common divisor,
    # a % b will return zero.
    # base case
    if a % b == 0:
        return b
    # --> The gcd(a,b) function should call itself recursively
    return gcd(b, a % b)

a = 128
b = 256
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")
