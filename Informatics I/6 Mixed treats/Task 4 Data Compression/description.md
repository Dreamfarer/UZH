
Assume you have a list of dictionaries that all have the same keys. For example:

    [
        {"a": 1, "b": 2, "c": 3},
        {"a": 9, "c": 7, "b": 8}, # dictionary keys don't have any order
        ...
    ]

Write a function `compress` that takes such a list of dictionaries as a parameter `data`.
The function should perform two tasks, best illustrated by the result below.
First, it should extract all keys, sort them alphabetically (as the Python `sorted` function does it), and store them in a tuple.
Second, it should create a tuple for each dictionary, where the values of the dictionary are stored in the correct order.

Finally, the function should return a tuple that itself contains the keys as a tuple and a list containing the value tuples.

When called on the previous example, your function should return the following data:

    (
        ("a", "b", "c"),   # keys in a tuple
        [
            (1, 2, 3),     # values of each dictionary
            (9, 8, 7)      # values in correct order corresponding to the keys!
        ]
    )

You can assume that the provided parameter is always a valid list of dictionaries and that
all these dictionaries in the list share the same keys. However, the order of the keys might
be different among the dictionaries.

Make sure that your solution also works for empty lists or for empty dictionaries.
The return value should *always* be a tuple with two values. If `data` is an entirely empty list,
the result tuple should contain an empty tuple and an empty list. If `data` is a list containing an empty
dictionary, then the result tuple should contain an empty tuple as the first value and a list containing an empty tuple as the second value.

**Note:** The provided script defines the signature of the function. Do not change this signature or the automated grading will fail. Do not use any global variables. Your solution should be self-contained in the solution function.

**Note:** Tuples are immutable, so you cannot append values. However, you can
use a `list` and `append` each record. The final result can then be converted to a
tuple. For example, `tuple([1, 2, 3])` evaluates to `(1, 2, 3)`.

**Note:** You are allowed to use the built-in function [`sorted`][sorted] to sort the list of keys.

[sorted]: https://docs.python.org/3/library/functions.html#sorted
