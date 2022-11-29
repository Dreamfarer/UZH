#!/usr/bin/env python3

# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def convert_roman_to_int(roman):
    roman_single_digits = {
        # simple cases
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_double_digits = {
        # compound cases
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    lst = sorted(list(roman_single_digits.values()) + list(roman_double_digits.values()))
    skip = False
    result = 0
    found_num = 1

    # If Input is empty
    if roman == "":
        return 0

    # loop through all letters with index
    for index, letter in enumerate(roman):
        # checks if all letters are a valid roman letter
        for i in roman:
            if i not in roman_single_digits:
                raise Warning("Invalid Input")

        # skip implementation for loop if found number is double-digit (dodges picking the next letter a second time)
        if skip:
            skip = False

            # if the current roman isn't the last one and the next letter is bigger than the just added double-digit
            # raises warning
            if index + 1 != len(roman) and roman_single_digits[roman[index + 1]] > number:
                raise Warning("Invalid Input")
            continue

        # assigns single digit number to roman letter
        number = roman_single_digits[letter]

        # if the number isn't the last number and the next number isn't bigger
        # so only goes to the double-digit segment if the next number is bigger
        if index + 1 != len(roman) and number < roman_single_digits[roman[index + 1]]:

            # raises a Warning if the two put together letters aren't a real combination
            if letter + roman[index + 1] not in roman_double_digits:
                raise Warning("Invalid Input")

            # puts the correct double-digit number to add it to the result and adds the before mentioned skip
            number = roman_double_digits[letter + roman[index + 1]]
            skip = True

            # raises Warning if the current double-digit is smaller than the next double-digit
            # the first if line is to check if the next double-digit exists, so the current double-diggit
            # needs to be at index -4 and - 3 to be valid. Else gives Error
            if len(roman) > 3 and not index + 3 > len(roman) and roman[index + 2] + roman[index + 3] in roman_double_digits:
                next_double_digit = roman_double_digits[roman[index + 2] + roman[index + 3]]
                if next_double_digit > number:
                    raise Warning("Invalid Input")

        # Raises a warning if the input has I, X or C 4 times in a row because it should then be a IV, XL or CD
        if not index + 4 > len(roman) and (letter == "I" == roman[index + 1] == roman[index + 2] == roman[index + 3] or
                                           letter == "X" == roman[index + 1] == roman[index + 2] == roman[index + 3] or
                                           letter == "C" == roman[index + 1] == roman[index + 2] == roman[index + 3]):
            raise Warning("Invalid Input")

        # checks that letter V L and D are not back to back because then X, C and M should be used
        if index + 1 != len(roman) and ((letter == "V" and roman[index + 1] == "V") or
                                        (letter == "L" and roman[index + 1] == "L") or
                                        (letter == "D" and roman[index + 1] == "D")):
            raise Warning("Invalid Input")

        # saves the just added number to found_num if it's bigger than the last found number
        # This is to ensure that found_num is always the biggest, so far added number
        # This is important for the last catching to raise a Warning
        if number > found_num:
            found_num = number

        # adds the number to the result
        result += number

        # if the current number isn't the last one and of either of lst nor the input
        # and the result is bigger than the next biggest number in lst, it raises a warning.
        # Used to get cases like "IVIV" where there is a better/correct way to express this number
        if index != len(roman) and found_num != 1000 and result >= lst[lst.index(found_num) + 1]:
            raise Warning("Invalid Input")

    return result


# The following lines calls the function and prints the return
# value to the Console.
i = convert_roman_to_int("XIII")
print(i)
