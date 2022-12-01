# This enables us to write test cases.
# Imports will be discussed later in the lecture.
from unittest import TestCase

# For now, only the following import matters. It
# makes things from public/script.py available here.

# Chose depending on your folder structure
#from public import script (used on 'Access')
import script

# Don't worry about this line, for now it just
# marks the beginning of your Test Suite
class PublicTestSuite(TestCase):

    # These functions are the individual tests. You
    # can name them (almost) any way you like. In this
    # case, we decided to call this test "test_one".
    def test_one(self):
        # First, we set n in the script to 1
        script.n = 1
        # Then we call the fizz_buzz function
        # and assign the return value to "res"
        res = script.fizz_buzz()
        # Now we assert that res equals 1
        # If this were untrue, the assertion, and with
        # it the test, would fail.
        self.assertEqual(res, 1)

    # Another test to check if calling fizz_buzz()
    # with n = 3 will return "Fizz".
    def test_three(self):
        script.n = 3
        res = script.fizz_buzz()
        self.assertEqual(res, "Fizz")

    # Now, implement a third test case that checks if
    # given n = 5, the function correctly returns
    # "Buzz". The test is very similar to the second
    # test case and it should pass if you hit
    # "Test & Run". Do not rename this test!

    def test_five(self):
        script.n = 5
        res = script.fizz_buzz()
        self.assertEqual(res, "Buzz")

    # Finally, implement a fourth test case that
    # checks if given n = 15, the function correctly
    # returns "FizzBuzz". Again, the test is very
    # similar to the others. You will notice that the
    # test will fail because of the existing bug in
    # fizz_buzz()! Do not rename this test.

    def test_fifteen(self):
        script.n = 15
        res = script.fizz_buzz()
        self.assertEqual(res, "FizzBuzz")

