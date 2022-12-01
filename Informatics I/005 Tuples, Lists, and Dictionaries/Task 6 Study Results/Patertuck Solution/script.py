#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):

    # Returns None if the file doesn't exists
    if not os.path.exists(path):
        return None

    grade = 0.0
    grades_count = 0

    # opens the file from the given path and copies it into content
    file = open(path, 'r')
    content = file.read()

    # iterates through the different lines in the file
    for line in content.split("\n"):

        # ignores comments in the file
        if "#" in line or len(line) == 0:
            continue

        # removes the spaces and tabs from the string after te ":" and adds the number to grade
        # adds +1 to grades_count to calculate the average grade later
        grade += float(line[line.index(":") + 1:].strip())
        grades_count += 1

    # calculates and returns the average
    if grades_count == 0:
        return 0.0
    return grade/grades_count




# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("C:/Users/patri/Desktop/Programmieren/Programme/Informatik 1/Exercise 5/my_grade.txt"))
