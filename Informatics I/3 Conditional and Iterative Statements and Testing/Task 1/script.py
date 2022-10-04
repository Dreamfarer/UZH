#!/usr/bin/env python3

n = 0

# This implementation contains a bug! First, go
# to public/tests.py and implement two more tests.
# Finally, come back here and correct the code
def fizz_buzz():
    if n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    elif n % 5 == 0 and n % 3 != 0:
        return "Buzz"
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    else:
        return n