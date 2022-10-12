#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def absolute_value(a):
    
    # If the number is minus, multiply it with -1 for it to be positve
    if a < 0: return a * -1
    return a

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gcd(a, b):
    
    # We will use the 'Euclidean algorithm' to achieve our goal!
    # You can also find the gcd through 'Integer factorization' 
    # or you could list all possible divisors which yield rest 0
    # Read more on https://www.mathebibel.de/groesster-gemeinsamer-teiler

    # However, only the 'Euclidean algorithm' fits here because
    # we are not allowed to change the function signature or
    # introduce more variables.

    # We need to make every number positive
    a = absolute_value(a)
    b = absolute_value(b)

    # According to the description, we should return 'None' if a and b is 0
    if a == 0 and b == 0: return None

    # If either a or b is 0, return the abs. value of the non-zero number
    if a == 0: return b
    if b == 0: return a

    # Devide the bigger number by the smaller number
    # and get the remainder
    remainder  = max(a, b) % min(a, b)

    # Base case: The gcd has been found if division yields remainder 0
    if remainder == 0: return min(a, b)

    # Replace the bigger number with the remainder and call the function again
    return gcd (remainder, min(a, b))


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = 33
b = 17
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")