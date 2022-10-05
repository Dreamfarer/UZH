from unittest import TestCase

from public import script

class PublicTestSuite(TestCase):

    def test_basic(self):
        actual = script.generate_greeting()

        m = "The generate_greeting function should return a string!"
        self.assertTrue(isinstance(actual, str), m)

