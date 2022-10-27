#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def invert(d):
    inverted_dictionary = {}

    # gets the original/old keys and values
    for old_key, old_val in d.items():

        # adds the old value to an already existing new key in the Dictionary and sorts it
        if old_val in inverted_dictionary:
            inverted_dictionary[old_val].append(old_key)
            inverted_dictionary[old_val] = sorted(inverted_dictionary[old_val])

        # inserts a new key in the dictionary if there isn't one yet with the old value
        else:
            inverted_dictionary[old_val] = [old_key]

    return inverted_dictionary


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(invert({"d": 1, "b": 1, "c": 3, "c": 1}))
