#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 5

# build a string 
def build_string_pyramid():

    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    s = ""

    # Create a tuple holding the numbers 1 to 'h'
    # I prefer this way over an index based approach because it starts at 1 instead of the common 0
    heights = range(h+1)[1:]

    # Loop over 1, 2, 3, ..., n height steps 
    for step in heights:

        # Loop over all sub-steps leading up to the current step
        steps = range(step+1)[1:]
        for sub_step in steps:

            if sub_step == 1: s += str(sub_step)
            else: s += "*" + str(sub_step)
        
        # End line
        s += "\n"

    # Loop over n-1, n-2, ..., 2, 1 height steps (reverse). Pay attention to start of 'n-1', because we've already printed 'n' before
    for step in reversed(heights[:len(heights)-1]):

        # Loop over all sub-steps leading up to the current step
        steps = range(step+1)[1:]
        for sub_step in steps:

            if sub_step == 1: s += str(sub_step)
            else: s += "*" + str(sub_step)
        
        # End line
        s += "\n"

    # Return the string but cut away the last '\n'
    return s[:len(s)-1]
    
# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())