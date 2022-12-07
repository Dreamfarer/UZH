#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

#########################################################################
# File doesn't work for you?
# This task requires the relative path to your file. However, depending on your
# IDE, that path may differ. It's not (always) relative to the python file, but instead
# to the top directory of your project.
#
# Don't know where to find that?
# execute the command
#   print(os.getcwd())
# cwd stands for "current working directory", and it will display from where
# you execute python files. Your relative file must point from there.
# this example assumes you have "UZH" as the highest folder. So we must
# work our way down the folders to reach the txt file.
#########################################################################


#############
# Points: 3/3
#############
# DO NOT COPY THE LAST LINE INTO ACCESS. IT MAY CAUSE FAILURE.
def get_average_grade(path):
    if not os.path.exists(path):
        return None

    # while not necessary in this example, always list what your encoding
    # is. You are probably familiar with ASCII encoding, but utf-8
    # is the more widespread one on the internet. If you don't specify,
    # future projects may fail due to "é" being turned into unreadable
    # characters.
    with open(path, "r", encoding="utf-8") as f:
        grades_sum = 0
        grades_count = 0
        for line in f.readlines():
            # the strip method strips whitespace characters and spaces from the
            # beginning and end of a string. Example: "   test case  \n" -> "test case"
            line = line.strip()
            # IMPORTANT: line[0] throws an error if the line has no length.
            # test for line length FIRST.
            if len(line) == 0 or line[0] == "#":
                continue

            colon_index = line.index(":")
            grade = float(line[colon_index + 1:].strip())
            grades_sum += grade
            grades_count += 1
        # we cannot divide by zero. Default to 0.0 if it happens
        average_grade = 0.0 if grades_count == 0 else grades_sum / grades_count

    return average_grade


print(get_average_grade(
    "Informatics I/5 Tuples, Lists, and Dictionaries/Task 6/public/my_grades.txt"))
