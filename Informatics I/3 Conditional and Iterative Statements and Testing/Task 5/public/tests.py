#!/usr/bin/env python3
from unittest import TestCase

from public import script

# This test suite only tests whether the value returned by
# the solution function has the correct type. If this test
# passes, that does not mean that you will get any points.
# The grading system uses different, more exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".


class PublicTestSuite(TestCase):
    def test_return_type(self):
        actual = script.get_bmi_category()
        m = "The get_size function should return a string!"
        self.assertTrue(isinstance(actual, str), m)
