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

    index = 0
    roman_length = len(roman)
    numbers = {"total": 0, "current": 0, "last": 60000000}

    # Raise an error if the string contains invalid characters
    for characters in roman:
        if not characters in roman_single_digits: 
            raise Warning("Invalid Input")

    # Loop through the string containing the numerals
    while index < roman_length:

        # Catch numerals which appear in "normal notation" (up to three equals in sequence)
        # Loop over the remaining string to check if the same numeral appears up to three times
        triple_index = 0
        while index + triple_index + 1 < roman_length:

            # Break if the numeral of the next iteration is not the same as the first one anymore
            if roman[index + triple_index + 1] == roman[index]: 

                # Throw error if there is more than one equal numeral following each other
                if roman[index] in ["V", "L", "D"]: raise Warning("Invalid Input")

                # Throw error if there are more than three equal numerals
                if triple_index >= 2 and not roman[index] == "M": raise Warning("Invalid Input")

            else: break

            triple_index += 1 # Increment parsing index

        # If the same numeral has appeared multiple times, multiply the base numerals
        numbers["current"] = (triple_index + 1) * roman_single_digits[roman[index]]

        # Catch numerals in "subtractive notation"
        if not index + 1 >= roman_length:
            if roman[index] + roman[index + 1] in roman_double_digits:
                numbers["current"] = roman_double_digits[roman[index] + roman[index + 1]]
                index += 1

        # Throw error if smaller-valued letters appear before larger-valued ones
        if numbers["last"] <= numbers["current"] and not numbers["last"] == 0:
            raise Warning("Invalid Input")

        # Throw error if the current or the last was in subtractive notation but in the same range
        # Example: V-IV and VI-IV are not allowed but V-III is allowed
        if (numbers["last"] in roman_double_digits.values() or numbers["current"] in roman_double_digits.values()):
            
            # Calculate range of number one
            base_one = str(numbers["last"] // 10)
            if base_one == "0": base_one = ""
            base_one = pow(10, int(len(base_one)))

            # Calculate range of number two
            base_two = str(numbers["current"] // 10)
            if base_two == "0": base_two = ""
            base_two = pow(10, int(len(base_two)))

            # If they match, it is invalid
            if base_one == base_two: raise Warning("Invalid Input")
        
        numbers["total"] += numbers["current"] # Add the current number to the total
        numbers["last"] = numbers["current"] # Make the current number to the last one (used to compare in the next iteration)
        index += triple_index # Skip the amount of appeared same numerals 
        index += 1 # Prevent infinite loop by incrementing the index in each pass

    return numbers["total"]


# The following lines calls the function and prints the return
# value to the Console.
i = convert_roman_to_int("XVI")
print(i)