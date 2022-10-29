#!/usr/bin/env python3

import os


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# THOUGH IT WORKS, SOLUTION IS UGLY AND INEFFICIENT BECAUSE OF DUMB THINKING MISTAKES. NOW AM MAD AND DON'T WANT TO
# IMPROVE THE CODE. DUMB TASK!!!
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        # what to do if the input file does not exist?
        return False
    # the rest of your implementation

    # Takes the input file and saves it into a list
    input_list = []
    output_list = []
    with open(path_reading, 'r') as input_file:
        for line in input_file.readlines():
            input_list.append(line)

    # Opens the output to write into it
    with open(path_writing, 'w') as output_file:

        # If the input file is empty this returns an empty txt file
        if not input_list:
            output_file.write("")
            return

        # adds the heading to the output file + iterates through the lines of input without first line (which is "Name")
        output_list.append("Firstname,Lastname\n")
        for line in input_list[1:]:

            # for empty lines (lines with an \n only) adds a "," to output list
            if line == "\n":
                output_list.append(",\n")

            # add the line with ";"
            elif ";" in line:
                # swaps first and last line
                line = line.split("; ")
                line = line[1] + "," + line[0]

                # inefficient code to remove \n between the two lines and ads one at the end and adss to output_list
                if "\n" in line:
                    line = line.replace("\n", "")
                line += "\n"
                output_list.append(line)

            # takes lines that have " " for separation and adds it to output_list
            else:
                output_list.append(",".join(line.split(" ")))

        # removes the last \n from the output_list
        if "\n" in output_list[-1]:
            output_list[-1] = output_list[-1][:len(output_list[-1]) - 1]

        # writes the output_list into the output file
        output_file.write("".join(output_list))


# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "public/my_data.txt"
OUTPUT_PATH = "public/my_data_processed.txt"
# INPUT_PATH = "C:/Users/patri/Desktop/Programmieren/Programme/Informatik 1/Exercise 6/my_data.txt"
# OUTPUT_PATH = "C:/Users/patri/Desktop/Programmieren/Programme/Informatik 1/Exercise 6/my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")
