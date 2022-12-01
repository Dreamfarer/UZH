#!/usr/bin/env python3

s = "aB:cD"

# perform the transformation
def transform_string():
    # Insert your code here.
    # You may want to use several variables to
    # store temporary values (such as the index of
    # the colon or the two strings before and after
    # it). Then, you can construct the final result
    # from your temporary variables.

    # 1 Extract everything until ":" and convert it to lower case letters
    # 2 Extract everything after ":" and convert it to upper case letters
    # 3 Combine the two expressions and add them together
    res = s[:s.find(":")].lower() + s[s.find(":"):].upper()

    # You don't need to change the following line.
    # It simply returns the string created above.
    return res