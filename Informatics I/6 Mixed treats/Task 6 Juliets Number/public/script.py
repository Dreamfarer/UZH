#!/usr/bin/env python3

# These numbers that are registered with Whatsapp
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):
    # This function accepts a string n for juliets number where one digit is missing.
    # and should return a list of all whatsapp numbers that might belong to juliet 
    possible_nrs_for_juliet = []

    # Loop over each position in the number where additional digits can be inserted ('07' is given so it starts at index = 2)
    for position_in_number in range(2, 10):

        # Loop over the digits 0 to 9 (to insert them into the position)
        for digit in range(10):

            # Insert the current digit at the current position in the number
            generated_number = n[:position_in_number] + str(digit) + n[position_in_number:]

            # If the generated number is present in the list of registered Whatsapp numbers, add it to the list of possible numbers
            if generated_number in wa_nrs: possible_nrs_for_juliet.append(generated_number)

    # Remove duplicates and return the list containing possible numbers (https://www.w3schools.com/python/python_howto_remove_duplicates.asp)
    return list(dict.fromkeys(possible_nrs_for_juliet))

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))