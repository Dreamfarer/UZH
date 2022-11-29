#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 7


# build a string
def build_string_pyramid():
    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    s = ""
    line_numb = ""

    # Enter your code here
    # use nested loops and the range() function

    # produces the first half of the pyramid until the top by quick saving the individual line through evr iteration and
    # then adding the next number
    for number in range(1, h + 1):
        s += line_numb + str(number) + "\n"
        line_numb += str(number) + "*"

    # creates a list of the individual lines of the first half of the pyramid
    half_pyramid = s.split("\n")
    line_index = h - 2

    # by indexing the first half of the pyramid in descending order the other half of the pyramid gets "copied"
    for _ in range(h - 1):
        s += str(half_pyramid[line_index]) + "\n"
        line_index += -1

    # the string gets stripped at the end to remove the last newline / "\n"
    s = s.strip()

    # You don't need to change the following line.
    # It simply returns the string created above.
    return s


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())
