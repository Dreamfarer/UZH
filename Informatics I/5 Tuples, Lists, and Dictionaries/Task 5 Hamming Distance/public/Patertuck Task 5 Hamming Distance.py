#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

# calculates the hamming distance of 2 Lists of same length
def hamming_dist_calc_list(list1, list2):
    hamming = 0

    for (x, y) in zip(list1, list2):
        if x != y:
            hamming += 1
    return hamming


def hamming_dist(signal_1, signal_2):
    return_list = []

    # checks if the dictionary is in the first or second input so the code works for both
    if type(signal_2) == dict:
        signal_1, signal_2 = signal_2, signal_1

    # Catches case where the two dataset aren't the same lengths or any of the two are empty lists
    if "data" not in signal_1 or len(signal_1["data"]) != len(signal_2) or (len(signal_1["data"]) or len(signal_2)) == 0:
        return "Empty signal on at least one of the sensors"

    # Takes the different lists out of the datasets and puts them into val1 and val2
    for index, val2 in enumerate(signal_2):
        val1 = signal_1["data"][index]

        # Catches case where the strings are of different length
        if len(val1) != len(val2):
            return "Sensor defect detected"

        # adds the triplets to the to be returned list if hamming length > 0
        hamming = hamming_dist_calc_list(val1, val2)
        if hamming > 0:
            return_list.append((val1, val2, hamming))

    return return_list


# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_2 = {"times": [0, 1, 2, 3, 4, 5],
                   "test": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_1 = ("10101110", "11001001", "11110011", "01111011", "11001101", "00011011")

print(hamming_dist(signal_sensor_1, signal_sensor_2))

# [('00101110', '10101110', 1), ('11001011', '11001001', 1), ('11110000', '11110011', 2), ('01000011', '01111011', 3)]
