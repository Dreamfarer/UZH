#!/usr/bin/env python3

from curses.ascii import isdigit

pwd = "abc"

def is_valid():
    # You need to change the following part of the function
    # to determine if it is a valid password.

    validity = False

    # Check whether the provided password has the correct length
    if len(pwd) >= 8 and len(pwd) <= 16:

        # Contains the counters for 2 lower case and 2 upper case characters, 2 digits, and 2 special chars
        appeareance_counter = [0, 0, 0, 0]

        # Loop over every character in the password
        for character in pwd:
            
            # Lower case
            if character.islower():
                appeareance_counter[0] += 1

            # Upper case
            elif character.isupper():
                appeareance_counter[1] += 1

            # Digits
            elif character.isdigit():
                appeareance_counter[2] += 1

            # Special characters
            elif character in ["+", "-", "*", "/"]:
                appeareance_counter[3] += 1

            # Not valid password if character is nothing from above
            else:
                return False

            # Check whether it only contains the characters a-z, A-Z, digits, or the special chars "+", "-", "*", "/".
            #if not (character in ["+", "-", "*", "/"] or character.islower() or character.isupper() or character.isdigit()):
            #    return False

        # Check that there are at least 2 lower case and 2 upper case characters, 2 digits, and 2 special chars
        for number in appeareance_counter:
            if number < 2:
                return False
        
        validity = True

    # You don't need to change the following line.
    return validity

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid())

