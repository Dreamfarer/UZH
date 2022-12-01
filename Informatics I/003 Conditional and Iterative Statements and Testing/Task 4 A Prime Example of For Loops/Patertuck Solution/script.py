#!/usr/bin/env python3

# As mentioned in the hints, you might want to use the math package
import math

# You can change this value to your liking. Depending on your implementation larger values of n might take quite some
# time.
n = 1000


# perform the Sieve of Eratosthenes algorithm and return all primes <= n
def sieve_of_eratosthenes():
    # You need to change the functionality of this function to
    # create a (sorted) list of all primes <= n which will then be returned.
    # Use the Sieve of Eratosthenes algorithm from the description.
    # You may change the following initialization of the list to be returned.

    current_number = 2
    multiplier = 2
    primes_up_to_n = []
    counter = 1

    # Return ["empty"] if n is 0 or 1 (Rule!)
    if n in range(0, 2):
        primes_up_to_n.append("empty")

    else:

        # Create a list of all prime numbers
        for number in range(2, n + 1):
            primes_up_to_n.append(number)

        # Loops until a prime number is found that is smaller than the square root of n (largest number)
        while current_number < math.sqrt(n):

            # Goes through every multiple of current_number that are smaller than n
            while current_number * multiplier <= n:

                # Removes the multiple if it is still inside the list primes_up_to_n
                if current_number * multiplier in primes_up_to_n:
                    primes_up_to_n.remove(current_number * multiplier)

                multiplier += 1

            # The multiplier gets reset for the next loop and the next prime number in the list gets taken
            multiplier = 2
            current_number = primes_up_to_n[counter]
            counter += 1

    # You don't need to change the following line.
    # It simply returns the list created above.
    return primes_up_to_n


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(sieve_of_eratosthenes())
