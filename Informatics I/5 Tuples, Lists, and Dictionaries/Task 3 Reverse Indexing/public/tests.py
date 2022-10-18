from unittest import TestCase
from public import script

class PrivateTestSuite(TestCase):

    # If this test passes, that does not mean that you will get any points.
    # The grading system uses different, more exhaustive tests.

    # Feel free to extend the class with your own test cases,
    # which will then also be executed in every "Test & Run".

    # Check if the return type is dict
    def test_return_type_reverse_index(self):
        dataset = [
            "Hello world",
            "This is the WORLD",
            "hello again"
        ]           
        actual = script.reverse_index(dataset)
        message = "@@Expected return type is dict but {} is returned !@@".format(type(actual).__name__)
        self.assertIsInstance(actual,dict,message)

