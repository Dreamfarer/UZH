#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def compress(data):

    # Return an empty tuple and an empty list in the output tuple
    if len(data) == 0: return ((),[])

    # Return a tuple containing an empty tuple as the first value and a list containing an empty tuple as the second value
    if len(data[0]) == 0: return ((),[()])

    # Define output tuple consisting of the sorted keys of the dictionary
    output_keys_touple = tuple(sorted(data[0].keys()))

    output_list = [] # Will hold all the output tuples

    # Loop over every dictionary in the input list
    for dictionary in data:

        output_dictionary_tuple = [] # Currently a list to be able to modify it

        # Loop over every key (they guaranteed us that they keys are the same in every dictionary)
        for key in output_keys_touple:
            
            # Scan the current dictionary, retrieve the value of the current key and write it into the tuple (currently a list)
            output_dictionary_tuple.append(dictionary[key])

        # Convert list to tuple and add it to the output list
        output_list.append(tuple(output_dictionary_tuple))

    return (output_keys_touple, output_list)

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "c": 6, "b": 5}
]
print(compress(data))