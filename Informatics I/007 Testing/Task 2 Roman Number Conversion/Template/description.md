Often a given task may seem easy to implement at first. However,
looking at it from a testing perspective a lot of possible pitfalls may be uncovered.
An example for such a task is the conversion of roman numbers to integers.
In this exercise, you will leverage testing to create a function that achieves this conversion task
as rock-solidly as possible.

The suggested development pattern adheres to the following steps:
1. Write a very simple test.
2. Check whether it fails with the current implementation
3. If it fails, build the specifically tested functionality into the `convert_roman_to_int` function in the `public/script.py` file.
4. Re-execute the steps above with a new, slightly more elaborate test case.

The goal is to gradually improve the `convert_roman_to_int` function. 
Take the specification below as an orientation of what to use as test cases in the workflow described above.

## Specification / Orientation for test driven iterations
- The function `convert_roman_to_int` accepts a string and returns an integer value
- Given very simple string numerals like e.g. `"I"` or `"X"` it returns the correct integer value (1, or 10 respectively)
- Check that this works for all roman numerals `"I"`, `"V"`, `"X"`, `"L"`, `"C"`, "`"D"`, `"M"`
- Check that basic additive numerals return the correct results, e.g. `convert_roman_to_int("XI")` returns 11
- Check that basic subtractive notation works correctly, e.g. `"IV"` is 4, `"XL"` is 40 and `"CD"` is 400,
    `"IX"` is 9, `"XC"` is 90 and `"CM"` is 900.
- Check that longer additive numerals like `"VIII"`, `"MDC"` etc. give the correct results.
- Check that numerals that include both additive and subtractive elements work correctly, e.g. `"XIV"` is 14,
 `"XLI"` is 41 etc.
- Check that numerals that do not contain the 7 valid roman numerals (e.g. "XLS") raise a Warning by the statement
`raise Warning("Invalid Input")` (You must use this warning statement for all following invalid input cases)
- Check that numerals of an incorrect format (smaller-valued letters before larger-valued ones, like `"IIMX"`, `"IVII"` etc)
raise a Warning.
- Check that numerals of the pattern `"IVIV"`, `"IXIX"` raise a warning.
- Check that numerals not conforming to the classic roman number system (not using subtractive notation,
e.g. `"VIIII"` instead of `"IX"` ) raise a warning.
- Check that numerals that should not be repeated (e.g. `"VV"`, `"DD"`, `"LL"`) raise a warning.
- Check that any number of `"M"`s are allowed, e.g. `"MMMMMI"`.
- Check that cases `"CDXC"` and `"XLIX"` are accepted, 
- Check that cases `"VIV"` or `LLX` are rejected with a Warning.

## Important Notes
- Both `public/script.py` and `public/tests.py` will be taken into account for grading.
- The test suite is checked based on its ability to correctly identify correct and incorrect implementations
and the function itself based on its correctness.
- This means even if you are not able to build the `convert_roman_to_int` function,
you will get points for providing a complete test suite.
- It is important that the test suite only accesses the top function `convert_roman_to_int` though,
even if you decide to factor out functionality into utility functions in your own implementation.
- Make sure that your test suite checks whether a Warning is raised in the invalid input cases!
Various ways exist to do so, make yourself familiar with `self.assertRaises` to learn about the most convenient one.
- You do not need to worry about handling lowercase strings, just always use uppercase letters for the roman numbers.

## Further Hints
- Using dictionaries for storing the conversion of single roman numerals or compound numerals helps
- Parse the whole roman string in a structured fashion, inspecting one and two indices at the same time.
- Enumerating a range of test cases may help you discover patterns that you can use for your implementation
- Don't be afraid to discard some pieces of code when adding new functionality.
- The solution test suite contains about 50 tests

## Food for Thought
- Would you have been able to write this function without the tests?
- Would you have been as confident to change your code if you didn't have your whole testing suite for assurance?
- If time: implement the inverse conversion function `convert_int_to_roman(x)` as exam preparation.
