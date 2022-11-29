# Consol 
#output Firstname,Lastname
#
#Beat,Beat ,
#
#Barbara,Barbara Roland,Berger

# Submission hint: Conversion was not correct for file: Name\nQuirinus Quirrell

#!/usr/bin/env python3

import os

#######################################################################################################
# DO NOT SUBMIT TO ACCESS! CURRENTLY YIELDS 2/3 POINTS
#######################################################################################################

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        # what to do if the input file does not exist?
        return False
    # the rest of your implementation
    
    #open() takes a filename and a mode as its arguments. r opens the file in read only mode. To write data to a file, pass in w as an argument instead
    with open(path_reading, "r") as f:
        with open(path_writing, "w") as f2:
            header = f.readline()
            
            #when the file is empty
            if header == "":
                return None
            
            
            if header.find("\n") != -1:
                f2.write("Firstname,Lastname\n")
            
            else:
                f2.write("Firstname,Lastname")
            
            for line in f.readlines():
                index_semicolon = line.find(";")

                if index_semicolon != -1:
                    if line.find("\n") != -1:
                        firstname = line[index_semicolon + 2:-1]
                        lastname = line[:index_semicolon] +"\n"
                    
                    else:
                        firstname = line[index_semicolon +2:]
                        lastname = line[:index_semicolon]
                    
                    f2.write("{},{}".format(firstname, lastname))
                
                elif line == "\n":
                    f2.write(",\n")
            
                else:
                    index_space = line.find (" ")
                    firstname = line[:index_space]
                    lastname =line[:index_space +1:]
                    f2.write("{},{}".format(firstname, lastname))


# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "public/my_data.txt"
OUTPUT_PATH = "public/my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")
