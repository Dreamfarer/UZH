# find difference between two strings

# sensor 1 stores data as {
# "times": [*int],
# "data": [*str]
# }

# sensor 2 stores data as (*str)

# func hamming_dist
# compare a["data"][i] to b[i]
# if they DON'T match
# return: (
#   string a[i],
#   string b[i],
#   d int
# )

# if ONE OF THE strings differ, return "Sensor defect detected"
# if both datasets are empty or have different lengths,
# return "Empty signal on at least one of the sensors"

# Example a:  {"times": [0, 2, 5], "data": ["0010", "1101", "1100"]}
# Example b:  ("0010", "1111", "0000")
# Result:     [("1101", "1111", 1), ("1100", "0000", 2)]


#!/usr/bin/env python3

########################################################
# TASK IS EXPERIENCING ModuleNotFound ERRORS.
# THIS FILE IS UNTESTED AND NOT GUARANTEED TO GRANT
# FULL POINTS.
#######################################################

# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def calc_difference(str_1, str_2):
    difference = 0
    for idx, char in enumerate(str_1):
        if char != str_2[idx]:
            difference += 1
    return difference


def is_same_length(iter_1, iter_2):
    return len(iter_1) == len(iter_2)


def hamming_dist(signal_1, signal_2):
    hamming_distances = []
    data_1 = signal_1["data"][:]
    data_2 = signal_2[:]

    # data_1 / _2 are lists
    if not is_same_length(data_1, data_2):
        return "Empty signal on at least one of the sensors"

    for idx, string in enumerate(data_1):
        # compare string length
        if not is_same_length(string, data_2[idx]):
            return "Sensor defect detected"

        difference = calc_difference(string, data_2[idx])
        if difference == 0:
            continue

        hamming_distances.append((string, data_2[idx], difference))

    return hamming_distances


# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011",
                   "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))
