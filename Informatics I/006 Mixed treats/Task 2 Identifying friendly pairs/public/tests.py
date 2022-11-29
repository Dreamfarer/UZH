from unittest import TestCase

from public import script

# This test suite only tests whether the given two numbers are
# friendly pair or not. It uses the numbers 6 and 28, 
# which are given as examples in the description of the task.
# If this test passes, that does not mean that you will get any points.
# The grading system uses different, more exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".

class PublicTestSuite(TestCase):

    def test_checkFriendly(self):
        script.num1 = 6
        script.num2 = 28
        actual = script.isFriendlyPair()
        message = "@@{} and {} wrongly detected as not friendly pair even though they are.@@".format(script.num1, script.num2)
        self.assertTrue(actual, message)  
