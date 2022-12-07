#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def invert(d):
    '''
    Takes a dictionary as the parameter, inverts it and returns a list
    '''

    new_dictionary = {} # Create new dictionary

    # Loop over the keys of the dictionary 'd'
    for key in d.keys():

        # Check if new dictionary already has the specifc key
        if d[key] in new_dictionary: 
            new_dictionary[d[key]].append(key) # If it exists, add key (value of old dict.) to the value list (keys of old dict.)
        else:
            new_dictionary[d[key]] = [key] # Add key (value of old dict.) and add a list as a value (key of old dict.)

    # Sort the values of the new dict.
    for value_lists in new_dictionary.values():
        value_lists.sort()

    return new_dictionary

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(invert({"a":1, "b":1, "c":3}))
