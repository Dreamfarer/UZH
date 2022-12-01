from unittest import TestCase

from public import script

class PublicTestSuite(TestCase):

    def test_basic(self):
        actual = script.transform_string()

        m = "The transform_string function should return a string!"
        self.assertTrue(isinstance(actual, str), m)

