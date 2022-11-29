#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):

    output_dictionary = {} # Will hold the output dictionary
    
    # Loop over every string in the post
    for line in posts:

        # Count the '#' present in the current line
        occurances = line.count("#")

        # Only carry on if there are any '#' present in the current line
        if occurances > 0:

            # Loop over every occurance
            for index in range(occurances):

                # Cut away everything until and including the first '#'
                line = line[line.find("#")+1:]

                # Check that line contains any characters
                if len(line) == 0: continue

                # If the first character of the hastag is a number it is not a valid hastag
                if ord(line[0]) >= 48 and ord(line[0]) <= 57: continue

                captured_hastag = "" # Will hold the extracted hashtag

                # Loop over every character to check if there are any unwanted characters present
                for character in line:

                    # Break if the current character is not a-z, A-Z or 0-9 (with means hashtag has ended)
                    if not ((ord(character) >= 48 and ord(character) <= 57) or (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122)): break
                    captured_hastag += character

                # Check that the hashtag is not empty
                if len(captured_hastag) == 0: continue
                
                # Create a new key or count up if it already exists
                if captured_hastag in output_dictionary: output_dictionary[captured_hastag] += 1
                else: output_dictionary[captured_hastag] = 1
    
    return output_dictionary

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3"]
print(analyze(posts))
