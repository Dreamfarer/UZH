#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def req_steps(num_disks):
    # Wikipedia: 
    # With 3 disks, the puzzle can be solved in 7 moves. 
    # The minimal number of moves required to solve a Tower of Hanoi puzzle is 2^n − 1, where n is the number of disks.
    # We do not actually need to implement the puzzle, we only need to calculate 2^n - 1 without Math.pow()
    
    # Hint: 2^n - 1 can be written as: 1 + 2 * (1 + 2 * (1 + 2 * (...))). Instead of subtracting at the end, we add 1 to every multiplication by 2.
    # Example:
    # 2^4 - 1 = 2 * 2 * 2 * 2 - 1
    # 2^4 - 1 = 1 + 2 * (1 + 2 * (1 + 2 * (1)))
    
    if num_disks == 1: return 1 # Stop calling the function recursively if the base case has been reached. In this case, stop before the last multiplication by 2.
    return 1 + 2 * req_steps(num_disks-1) # Implement the above-mentioned algorithm

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print("For moving {} disks, {} steps are required.".format(3, req_steps(3)))

