#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def hamming_dist(signal_1, signal_2):

    hamming_distance_output_list = []

    # Make sure parameters match our expections (Signal 1: dictionary, Signal 2: tuple)
    if type(signal_1) == dict and type(signal_2) == tuple: dic, tup = signal_1, signal_2
    else: dic, tup = signal_2, signal_1

    # If the length of the dictionary and the tuple do not match, return specified strings
    if (not len(dic["times"]) == len(dic["data"]) == len(tup)) or len(dic["times"]) == 0 or len(dic["data"]) == 0 or len(tup) == 0:
        return "Empty signal on at least one of the sensors"
    
    # Check that each string of the dictionary and the tuple have the same length (we could integrate this into the function below)
    # I'll leave this here for the sake of readability
    for index in range(len(tup)):
        if not len(dic["data"][index]) == len(tup[index]):
            return "Sensor defect detected"
    
    # Loop over every data entry
    for entry_index in range(len(tup)):

        hamming_distance_counter = 0 # Will hold the number of changes required

        # Loop over every string in a data entry
        for string_index in range(len(tup[entry_index])):

            # Check if both characters (i n dictionary and tuple) match
            if not tup[entry_index][string_index] == dic["data"][entry_index][string_index]:
                hamming_distance_counter += 1
        
        # Append tuple to output list if there was an discrepancy
        if hamming_distance_counter > 0:
            hamming_distance_output_list.append((dic["data"][entry_index], tup[entry_index], hamming_distance_counter))

    return hamming_distance_output_list
        

# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))
