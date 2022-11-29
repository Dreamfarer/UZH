
In this task you are going to practice *black-box testing*, thereby testing the program's ability to comply with its specification, in terms of expected output to specific inputs, with no knowledge about its implementation.

## Function Specification

The function you will be testing, called `max_profit` calculates the best day to purchase a share and sell it given a range of prices.
The function takes 1 parameters: `prices` which is a list of prices for a share over a period of time.
The maximum profit is calculated by subtracting the lowest price from the highest price in the list provided that the lowest price comes before the highest price.

A correct implementation of `max_profit` must comply with the following requirements:

* For the prices parameter it expects a list of non-negative int numbers
* The function returns the string `Invalid Input Type` if it receives a non-list input.
* The function returns the string `Empty Price List` if it receives an empty list.
* The function returns the string `Invalid Data Type within List` if it receives a list with non-int elements.
* The function returns the string `Invalid Prices` if it receives a list with negative int elements.
* The function returns `0` if the list contains only one element or if the function cannot find a pair of prices where the first price is lower than the second price.
* If the parameters are valid, the function returns the maximum profit that can be made from buying and selling the share.

For example, if the list of prices is `[1, 2, 3, 4, 5]`, the function should return `4` because the maximum profit is made by buying the share at price `1` and selling it at price `5`.

```Python
max_profit([1, 2, 3, 4, 5])
# returns 4
```

## Task details

Your task is to provide a good test suite in `public/tests.py` that can decide whether a given `max_profit` implementation follows the specification given above.
Your test suite will be run with a variety of correct and incorrect implementations.
The resulting grade depends on its ability to detect faulty implementations of `max_profit`.
More specifically, the test suite should pass for a correct implementation and fail for an incorrect one.

Your task is to make sure that any implementation of `max_profit` does indeed always comply with *all* of specified requirements.
For this purpose, you need to test the function with multiple test cases that you will write.

**Note:** You do not need to implement `max_profit` in `public/script.py`. You can simply start writing your tests against unknown implementations. However, for yourself it might be useful to write a correct implementation of the function so you can make sure your test cases work as expected. However, your implementation of the function is irrelevant for the grading.

**Note:** You do not need to come up with good error messages, it is enough to fail a test if a problem can be detected (e.g., `self.assertEquals(expected, actual)`).

**Note:** Define your test suite as a subclass of `TestCase`.
Do not use utility functions for the assertions, instead, include calls like `self.assertEqual` directly in the body of the test functions or the automated grading will mark the solution as incorrect.

**Note:** The provided files define the signatures of various classes and functions.
Do not change these signatures or the automated grading will fail.
