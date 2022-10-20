from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):
    
    index_dictionary = {} # Create new dictionary holding the the words as keys and indexes as values

    # Loop over the dataset entries. Enumerate assigns every value an index which can be used in the loop
    for index, dataset_entries in enumerate(dataset):
        
        # Each dataset might have multiple 'values', loop over all of them.
        for str in dataset_entries.split():

            str = str.lower() # Convert to lowercase

            # Check if new dictionary already has the specifc key
            if str in index_dictionary: 
                index_dictionary[str].append(index)
            else:
                index_dictionary[str] = [index]

    return index_dictionary

# You can see the output of your function here
print(reverse_index(dataset))
