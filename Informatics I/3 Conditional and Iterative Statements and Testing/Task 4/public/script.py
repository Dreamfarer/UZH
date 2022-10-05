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
    
    primes_up_to_n = [] # This variable will hold every number from 1 to n (Be aware that the index mateches the value, E.g. primes_up_to_n[10] contains the value 10)

    # Return ["empty"] if n is smaller or equal to 1 (nasty little rule)
    if n in range(0,2):
        return ["empty"]

    # Populate list with the numbers from 0 to n
    for iteration in range(0, n + 1):
        primes_up_to_n.append(iteration)
    
    # Scratch the 0 and the 1, these aren't prime numbers for sure
    primes_up_to_n[0] = None
    primes_up_to_n[1] = None

    # Iterate over the whole list containing the numbers 1 to n. 
    # The algorithm will set every non-prime-number to 'None'. So in the end, only the prime numbers remain in the list.
    for iteration in primes_up_to_n:

        # If the value in primes_up_to_n at this index (from above we know index = value) has already been set to 'None', you don't have to calculate all the multiples again, because we already know it's not a prime number.
        if iteration != None:

            # Calculate all multiples of the value in primes_up_to_n at this index and scratch them
            for multiplier in range(2, n + 1):

                index = iteration * multiplier # Calculate the number which needs to be scratched from the list

                # Break free if index is out of bounds or 'None'
                if index > n or index == None:
                    break

                primes_up_to_n[index] = None # Set current index to 'None' -> We have found another not-prime-number

    # Remove all Nones from the list so only the prime numbers remain
    primes_up_to_n = list(filter(None, primes_up_to_n))

    # You don't need to change the following line.
    # It simply returns the list created above.
    return primes_up_to_n 

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(sieve_of_eratosthenes())