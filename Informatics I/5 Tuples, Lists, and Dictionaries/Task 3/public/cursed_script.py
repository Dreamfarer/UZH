dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
]


###################################################################
# I don't dare submit this. No guarantee if it scores all points.
###################################################################
def reverse_index(dataset):
    return dict(zip(list(dict.fromkeys(
        [*(" ".join([string.lower() for string in dataset])).split()])), [[i for i, x in enumerate(
            dataset) if word in x.lower().split()] for word in list(dict.fromkeys(
                [*(" ".join([string.lower() for string in dataset])).split()]))]))


#
# Order of operations
"""
[string.lower() for string in dataset] -> "step1"
"""
# 1. iterate over each element (string) in the dataset,and turn it to lowercase.
#    store the results in a list.
"""
" ".join([step1]) -> "step2"
"""
# 2. Join the elements in the list into one string, with the delimiter before the
#    dot. In this case, it's space.
"""
[*(step2).split()] -> "step3"
"""
# 3. split the string up at a certain character. If left empty, it defaults to space.
#    we spread its values (*) across the inside of a list.
#    EXAMPLE:
#         tuple = (1,2,3)
#         list = [*tuple]
#         >> list = [1,2,3]
"""
dict.fromkeys(step3) -> "step4"
"""
# 4. We create a dictionary based on list step3. We get rid of duplicates this way.
#    the dictionary values default to "None".
"""
list(step4) -> "step5"
"""
# 5. We turn the dictionary into a list. All keys will be inserted into the list.
"""
zip(step5, ???)

???: 
[[i for i, x in enumerate(
            dataset) if word in x.lower().split()] for word in list(dict.fromkeys(
                [*(" ".join([string.lower() for string in dataset])).split()]))])

-> [[i for i, x in enumerate(
            dataset) if word in x.lower().split()] for word in step5]
"""
# We have completed argument 1 of the "zip" function. More on that later.
# You probably recognize step5 again.
"""
[i for i, x in enumerate(dataset) if ...] -> "step6"
"""
# 6. This might look complicated, but it is actually pretty simple.
#    Remember the ternary operator?
"""
value if condition else value_if_false
"""
# We do the same here. We loop over the dataset, extract the index and value "x".
# if the condition to the right of step6 is fulfilled, we return i. There is no else statement
# in this case.
"""
x.lower().split() -> "step7"
"""
# 7. first turn the string to lowercase, then split the string (remember, defaults to space)
#    which creates a list.
"""
[i for step6 if word in step7] word???
"""
# 8. we have to go outside first to see what word even means in this context.
"""
[[... word ...] for word in step5]
"""
# We repeat this step for every word in step5. Step5 is the list of unique lowercase words
# we have.
# Now, let's look again at what we do.
"""
[i for step6 if word in step7] -> "step8"
"""
# We return the index of step6 only if the current word is equal to one of its elements.
"""
[[step8] for word in step5] -> "step9"
"""
# 9. We end up with a two-dimensional list. The outer list is one element per unique word,
#    the inner list is all indexes where the word occurred in the dataset.
"""
zip(step5, step9) -> "step10"
"""
# 10. zip() takes two lists as parameters. It creates a list of tuples. The first element of each tuple
#     is the nth place of the first list, while the second element is the nth element of the second list.
#     think of it as a way to create enumerate() from two seperate lists.
"""
return dict(step10)
"""
# 11. dict() creates a dictionary if given a two-dimensional list. Since we used zip, we now have key-value pairs
#     which create a functioning dictionary. We return it.

# Holy crap this was difficult to explain


# You can see the output of your function here
print(reverse_index(dataset))
