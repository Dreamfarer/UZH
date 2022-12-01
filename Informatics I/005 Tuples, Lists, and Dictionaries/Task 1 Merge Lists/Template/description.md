
Write a function that expects two lists of integers, `a` and `b`, as parameters and returns a list. The function should merge the elements of both input lists by index and return them as tuples in a new list. If one list is shorter than the other, the last element of the shorter list should be repeated as often as necessary. If one or both lists are empty, the empty list should be returned.

Please consider the following examples:

    merge([0, 1, 2], [5, 6, 7]) # should return [(0, 5), (1, 6), (2, 7)]
    merge([2, 1, 0], [5, 6])    # should return [(2, 5), (1, 6), (0, 6)]
    merge([], [2, 3])           # should return []

You can assume that the parameters are always valid lists and you do not need to provide any kind of input validation.

**Note:** The provided script defines the signature of the function. Do not change this signature or the automated grading will fail. Do not use any global variables. Your solution should be self-contained in the solution function.


