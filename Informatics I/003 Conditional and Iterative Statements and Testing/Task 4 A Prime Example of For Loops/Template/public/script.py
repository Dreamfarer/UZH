#!/usr/bin/env python3

# As mentioned in the hints, you might want to use the math package
import math

# You can change this value to your liking. Depending on your implementation larger values of n might take quite some time.
n = 1000


# perform the Sieve of Eratosthenes algorithm and return all primes <= n
def sieve_of_eratosthenes():
    # You need to change the functionality of this function to
    # create a (sorted) list of all primes <= n which will then be returned.
    # Use the Sieve of Eratosthenes algorithm from the description.
    # You may change the following initialization of the list to be returned.
    primes_up_to_n = []

    # You don't need to change the following line.
    # It simply returns the list created above.
    return primes_up_to_n


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(sieve_of_eratosthenes())