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

    # Small details in the rules which I had forgot about
    if n in range(0,2):
        return ["empty"]

    # Populate the list with the numbers from 0 to 1000
    for iteration in range(0, n + 1):
        primes_up_to_n.append(iteration)
    
    # Drop the first two
    primes_up_to_n[0] = None
    primes_up_to_n[1] = None

    # Iterate over whole list. It will set every non-prime-number to 'None'. So in the end only the prime numbers remain.
    for iteration in primes_up_to_n:

        # If index has already been set to None, you don't have to loop over this number again (efficiency)
        if iteration != None:

            # Calulcate all multiples of a number
            for multiplier in range(2, n + 1):

                index = iteration * multiplier # Calculate index

                # Break free if index is out of bounds or 'None'
                if index > n or index == None:
                    break

                primes_up_to_n[index] = None # Set current index to 'None'

    # Remove all 'None's from the list so only prime numbers remain
    primes_up_to_n = list(filter(None, primes_up_to_n))

    # You don't need to change the following line.
    # It simply returns the list created above.
    return primes_up_to_n 

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(sieve_of_eratosthenes())