#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def req_steps(num_disks):
    # implement this function

    if num_disks == 1:
        return 1

    return 2 * req_steps(num_disks - 1) + 1


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print("For moving {} disks, {} steps are required.".format(4, req_steps(4)))

