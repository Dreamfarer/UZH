
Write a function `invert` that expects a dictionary `d`. The function should return a dictionary where keys-value pairs in `d` have been inverted, meaning that the original values become keys and the original keys become values.

Given that in the original `d`, the same value might be referred to by multiple keys, and given that keys in dictionaries must be unique, the inverted
dictionary must have lists as values, in which all original keys are collected *and sorted*.

Please consider the following example.

    invert({"a": 1, "b": 1, "c": 3}) # should return {1: ["a", "b"], 3: ["c"]}

You can assume that the parameter is always a dictionary and you do not need to provide any kind of input validation.
The implementation should not change the provided dictionary and create a new one instead.

**Note:** The provided script defines the signature of the function. Do not change this signature or the automated grading will fail. Do not use any global variables. Your solution should be self-contained in the solution function.

**Note:** You are allowed to use the built-in function [`sorted`][sorted] to sort the list of resulting values. Depending on your implementation, you might find Python dictionary functions `.items()`, `.keys()` or `.values()` useful.

[sorted]: https://docs.python.org/3/library/functions.html#sorted

