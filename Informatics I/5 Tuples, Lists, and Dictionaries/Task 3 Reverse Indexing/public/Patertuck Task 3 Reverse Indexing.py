# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
]


def reverse_index():
    index_dictionary = {}

    # turns every word lower and iterates through every word individually
    for index, string in enumerate(dataset):
        string = string.lower()
        string = string.split()
        for word in string:

            # if the word already in the dictionary, it adds the number of the row (index) its in to the correct entry
            # else it adds a new entry in the dictionary with that word and the row (index)
            if word in index_dictionary:
                index_dictionary[word].append(index)

            else:
                index_dictionary[word] = [index]

    # don't forget to return your resulting dictionary
    return index_dictionary


# You can see the output of your function here
print(reverse_index())
