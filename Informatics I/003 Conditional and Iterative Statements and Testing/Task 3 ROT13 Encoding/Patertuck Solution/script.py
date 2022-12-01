#!/usr/bin/env python3

# You can freely adopt these values to try your solution
# with different values.
plain_text = "abzAZ!"
shift_by = 1


# perform a ROTn encoding
def rot_n():
    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    encoded = ""

    #loop over plain_text
    for character in plain_text:

        #checks if character is a letter
        if not character.isalpha():
            encoded += character
            continue

        shifter = shift_by

        #shifts the letter by one every loop until shifter is 0
        while shifter != 0:

            #for positive shifting of the letter
            if shifter > 0:
                character = chr(ord(character) + 1)
                shifter -= 1

                #If the letter exceeds "z" or "Z" it loops around to "a" or "A" specifically
                if ord(character) == 123:
                    character = "a"

                elif ord(character) == 91:
                    character = "A"

            #for negative shifting of the letter
            elif shifter < 0:
                character = chr(ord(character) - 1)
                shifter += 1

                # If the letter falls bellow "a" or "A" it loops around to "z" or "Z" specifically
                if ord(character) == 96:
                    character = "z"

                elif ord(character) == 64:
                    character = "Z"

        # Adds character to output string
        encoded += character

    # You don't need to change the following line.
    # It simply returns the string created above.
    return encoded


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(rot_n())
