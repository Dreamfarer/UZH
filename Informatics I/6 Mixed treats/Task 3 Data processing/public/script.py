#!/usr/bin/env python3

import os

#################################################################################
# Watch out at the bottom; you have to differentiate between Access and your IDE.
#################################################################################

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):

    # Check if 'my_data.txt' exists
    if not os.path.exists(path_reading): return False

    # Open the input file
    with open(path_reading) as input_file:

        input_file_lines = input_file.readlines() # Store every line from the input file
        output_file_content = "" # Will hold the string for the output file

        # Read each line of the input file seperately
        for index, line in enumerate(input_file_lines):

            # Cut away unnessecary characters
            line = line.replace("\t", "") # Remove all tabs from the string
            line = line.replace("\n", "") # Remove the line break from the string
                
            # Continue with next iteration if the line only contains 'name'
            if line == "Name" and index == 0:
                
                # Break if the file only contains 'name'
                if len(input_file_lines) == 1: 
                    output_file_content = "Firstname,Lastname"
                    break
                
                # Top row of output file
                output_file_content = "Firstname,Lastname\n"
                continue

            # Write a ',' to the output string in case the line is empty
            if len(line) == 0:
                output_file_content += ",\n"
                continue

            # Check what format the line has
            if not line.find(";") == -1:

                # Remove ';' from the string
                line = line.replace(";", "") 

                # Read firstname and lastname
                lastname, firstname = line.split()

            else:
                # Read firstname and lastname
                firstname, lastname = line.split()

            # Append the firstname and the lastname to the output string
            output_file_content += firstname + "," + lastname + "\n"

        # Remove last '\n' (if there is something to check)
        if len(output_file_content) > 0: 
            if output_file_content[-1] == "\n": output_file_content = output_file_content[:-1]

        # Write to output file
        with open(path_writing, "w") as output_file:
            output_file.write(output_file_content)

# Use this in your local IDE (Python somehow does not know the concept of relative paths)
#INPUT_PATH = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "my_data.txt")
#OUTPUT_PATH = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "my_data_processed.txt")

# Provide this to ACCESS
INPUT_PATH = "public/my_data.txt"
OUTPUT_PATH = "public/my_data_processed.txt"

# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        pass
        print(resultfile.read())
else:
    print("No output file exists")

