#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters.
def analyze(posts):
    return_dict = {}

    # cycles through all the different posts
    for element in posts:

        # loops through the same cycle as long asthere is a "#" in there
        while "#" in element:
            # takes the element after the # until the end
            element = element[element.find("#") + 1:]
            already_added = False

            # ends the current iteration if the start of hashtag isn't a letter or empty
            if element == "" or not element[0].isalpha():
                continue

            # iterates through the different symbols in the element until there is a symbol that is not a letter or
            # not a number the # or the hashtag is the whole element
            for index, symbol in enumerate(element):

                if not symbol.isalnum():

                    # adds the element to the dictonary until the hashtag-ending symbol and counts it plus 1
                    element_add = element[:element.find(symbol)]

                    if element_add in return_dict:

                        return_dict[element_add] = return_dict[element_add] + 1
                        already_added = True

                    else:
                        return_dict[element_add] = 1
                        already_added = True

                    break

            # ends the current iteration if the element has already been added to avoid if the last symbol of the
            # element is not alpha or num for the next line to wrongfully add it
            if already_added:
                continue

            # adds the element to the dictionary if the whole element is a valid hashtag
            if len(element) == index + 1:

                if element in return_dict:
                    return_dict[element] += 1
                else:
                    return_dict[element] = 1

    # returns the dictionary
    return return_dict


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #§c.########3#ss#####",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3"]
print(analyze(posts))
