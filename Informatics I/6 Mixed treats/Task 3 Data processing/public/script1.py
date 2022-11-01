#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        # what to do if the input file does not exist?
        print("False")
        return False
    # the rest of your implementation

    file_read = open(path_reading, 'r')
    all_lines = file_read.readlines()
    file_write = open(path_writing, 'w')
    
    #if the file is empty, write an empty file
    if not os.path.getsize(path_reading)>0:
        file_read.close()
        file_write.close()
        print ("path 1 is taken")
        return
    
    #if file only contains "Name", return file with "firstname, lastname"
    if file_read.read() == "Name":
        file_write.write("Firstname,Lastname")
        file_read.close()
        file_write.close()
        print("path 2 is taken")
        return
    
    

    for line in all_lines:
        #remove trailing next line char
        line = line.strip()
        
        #take care of the Name line
        if line == "Name":
            file_write.write("Firstname,Lastname")
            continue #this line only has Name, hence done
            
        
        
        column = line.find(";")
        #if column is found, write firstname and lastname
        if column != -1:
            lastname = line[0:column]
            firstname = line[column+2:]
            file_write.write("\n"+firstname + "," + lastname)
            continue #this line is done
        
        #if no column found, use space to seperate first and last name
        space = line.find(" ")
        if space == -1:
            file_write.write("\n,")
            continue #no space and no comma, so no name, this line is done
        else:
            firstname = line[0:space]
            lastname = line[space+1:]
            file_write.write("\n"+firstname + "," + lastname)
        
        
    
    
    file_read.close()
    file_write.close()
    return
    


# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "my_data.txt"
OUTPUT_PATH = "my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")

