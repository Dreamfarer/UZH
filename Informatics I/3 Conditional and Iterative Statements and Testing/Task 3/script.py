#!/usr/bin/env python3

# You can freely adopt these values to try your solution
# with different values.
from curses.ascii import isalpha, islower, isupper

plain_text = "abc"
shift_by = 1

# perform a ROTn encoding
def rot_n():
    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.

    global shift_by # Explicitly make the scope global, somehow it did not work otherwise

    encoded = "" # String holding the encoded characters

    # Loop over plain text
    for character in plain_text:

        # Only rotate A-Z and a-z
        if character.isalpha():
            
            # Get Ascii code of character
            ascii_index = ord(character) 

            # Prodedure for lower-case letters
            if character.islower():

                # Make sure index stays in between a to z: 97 to 122
                while not ascii_index + shift_by in range(97, 123):

                    if shift_by <= 0:
                        shift_by += len(range(97, 123))
                    else:
                        shift_by -= len(range(97, 123))

            # Prodedure for upper-case letters
            else:

                # Make sure index stays in between A to Z: 65 to 90
                while not ascii_index + shift_by in range(65, 91):

                    if shift_by <= 0:
                        shift_by += len(range(65, 91))
                    else:
                        shift_by -= len(range(65, 91))

            # Add character to output string
            encoded += chr(ascii_index + shift_by)   

        else:
            encoded += character

    # You don't need to change the following line.
    # It simply returns the string created above.
    return encoded

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(rot_n())