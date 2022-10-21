#!/usr/bin/env python3

import os

#################################################################################
# Watch out at the bottom; you have to differentiate between Access and your IDE.
#################################################################################

def get_average_grade(path):

    # What can be expect from the file?
    # * One line per course
    # * The first string on each line is the course name
    # * The grade (float) follows after a colon (':')

    # What error handling do we need to consider
    # * Tabs and spaces before/after course name and before/after grade should be erased
    # * Empty lines
    # * Lines starting with '#' should be considered a comment
    # * Return 'None' if the file does not exists
    # * Return 0.0 if file does not contain any grades

    # In the real world we would need to check multiple other cases

    # Define variables
    grades = []

    # Return 'None' if file does not exist
    if not os.path.exists(path):
        return None
    
    # Open the file (so it closes it automatically afterwards)
    with open(path) as my_file:

        # Loop over each line seperately
        for line in my_file.readlines():

            line = line.replace("\t", "") # Remove all tabs from the string
            line = line.replace("\n", "") # Remove the line break from the string

            # Continue if whole line is empty
            if len(line) == 0: continue

            # Continue if line is a comment (first index of line, not counting whitespaces, has to be a '#')
            if "".join(line.split())[0] == "#": continue

            # Continue if the line has stuff in it but does not contain grades
            if line.find(":") == -1: continue

            # Cut line into two parts, the first containing the course name, the second containing the grade
            grade = line.split(":")[1]

            # Cut away leading and trailing whitespaces
            grade =  grade.strip()

            # Append the float of the parsed grade to the list
            grades.append(float(grade))
    
    # If there were no grades found, return 0.0
    if len(grades) == 0: return 0.0

    # Calulcate average and return it
    return sum(grades) / len(grades)

# Provide this to Access
print(get_average_grade("public/my_grades.txt"))

# Use this locally (Python somehow does not know the concept of relative paths)
# 'my_grades.txt' must be placed in the same folder as this script is run from
# print(get_average_grade(os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "my_grades.txt")))

