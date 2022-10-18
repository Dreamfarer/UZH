dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
]


def reverse_index(dataset):

    index_dictionary = {}
    # We require each unique word. Luckily, index_dictionary can't have duplicates and is the perfect
    # tool to keep track of it.
    for string in dataset:
        # we make sure to turn each string into lowercase before splitting it up.
        # split() defaults to " ".
        words = string.lower().split()
        for word in words:
            if word not in index_dictionary:
                # the empty array is for easier appending in the next loop.
                index_dictionary[word] = []

    for keyword in index_dictionary:
        # search each keyword in the dataset
        for idx, string in enumerate(dataset):
            # Warning: do NOT use "if keyword in el".
            # keyword = "hello" and string = "hellohello" would result true, even though it's false.
            if keyword in string.lower().split():
                index_dictionary[keyword].append(idx)
    return index_dictionary


# You can see the output of your function here
print(reverse_index(dataset))
