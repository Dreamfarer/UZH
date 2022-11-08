#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 100

# build a string 
def build_string_pyramid():

    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    s = ""
    line_counter = 0
    
    if h==0:
        return s
    
    for i in range(1,h+1): #every line
        for j in range(i):
            if j == 0:
                s += "{}".format(j+1)
            else:
                s += "*{}".format(j+1)
        s += "\n"#add enter to end of every line
        line_counter += 1
    for i in range (h-1,0,-1):
        for j in range(i):
            if j == 0:
                s += "{}".format(j+1)
            else:
                s += "*{}".format(j+1)
        s += "\n"#add enter to end of every line
        line_counter += 1
        
    print(line_counter)
    # Enter your code here
    # use nested loops and the range() function

    # You don't need to change the following line.
    # It simply returns the string created above.
    return s

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())



