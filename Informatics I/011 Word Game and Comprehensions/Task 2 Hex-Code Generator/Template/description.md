In this exercise, you will extend the functionality of the 'Hacker Game' code you saw in the last lecture. You solve the tasks online as usual to obtain points. But, if you like, you can optionally download the lecture implementation of the game [here](https://lms.uzh.ch/url/RepositoryEntry/16814277160/CourseNode/90126956590914/path%3D~~Week12~~game%2Ezip/0) and integrate your solutions into the program. You can then run and play the completed version yourself, locally on your machine.

In this first task, you implement a more sophisticated version of the `generate_hex_codes` function.
First have a look at the current implementation:

    def generate_hex_codes(self):
        return ["0x0000"] * (self.columns * self.rows)

Calling this function returns a list, in which each element is the same string `"0x0000"`.

To make the game look more realistic, modify the function `generate_hex_codes` (which belongs to the class `GameRunner`) and make it return random 4-digit hex codes. The hex codes must still be prefixed with `0x` , but the 4 remaining characters must be randomly chosen alphanumeric characters (e.g., `0x7A36`). To achieve this, import the [choice](https://docs.python.org/3/library/random.html#random.choice) function and use it four times to pick random characters from the string `"0123456789ABCDEF"` to generate the individual hex codes. You need to specify exactly this string, choose hex code digits individually, and must not set any seed or otherwise the automated tests for this exercise may fail.

Like the current implementation, your function needs to return `rows * columns` hex codes. Make sure that every list element is generated individually to reduce the probability of including the same hex-code multiple times.

**Note:** All state must be contained within the function. Do not store information in global variables or in class variables.

**Note:** Do not change provided function signatures and do not set a seed for the random function or the automated grading will fail.

**Note:** We strongly encourage you to add more tests to the public test suite.

