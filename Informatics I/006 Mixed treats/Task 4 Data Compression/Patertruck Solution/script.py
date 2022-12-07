#!/usr/bin/env python3

#def tuple_builder(list):

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.
def compress(data):

    # catches cases of an empty data set or an empty dictionary and returns the right answer
    if not data:
        return (), []
    if data == [{}]:
        return (), [()]

    #  takes the sorted keys of the first entry
    keys = sorted(data[0].keys())

    return_list_of_tuples = []
    end_return_tuple = ()

    # loops through the individual dictionaries in the data set
    for dict in data:
        tuples_of_list = []

        # loops through the previously saved keys to take the connected value of each dictionary and add it to the
        # to be output tuple of lists
        for key in keys:
            tuples_of_list.append(dict[key])

        # takes the individual results of every dictionary as a tuple and adds them to the to be returned list of tuples
        tuples_of_list = tuple(tuples_of_list)
        return_list_of_tuples.append(tuples_of_list)

    # adds both the keys and list of tuples as a tuple and returns it
    end_return_tuple = (tuple(keys), return_list_of_tuples)
    return end_return_tuple





# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [
    {"a": 1, "c": 2, "b": 3},
    {"a": 4, "c": 6, "b": 5},
    {"a": 9, "c": 6, "b": 11}
]
print(compress(data))