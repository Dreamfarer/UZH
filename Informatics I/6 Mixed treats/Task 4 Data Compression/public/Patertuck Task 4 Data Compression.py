#!/usr/bin/env python3

#def tuple_builder(list):

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.
def compress(data):

    if not data:
        return (), []
    if data == [{}]:
        return (), [()]

    keys = sorted(data[0].keys())
    return_list_of_tuples = []
    end_return_tuple = ()



    for dict in data:
        tuples_of_list = []
        for key in keys:
            tuples_of_list.append(dict[key])
        tuples_of_list = tuple(tuples_of_list)
        return_list_of_tuples.append(tuples_of_list)
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