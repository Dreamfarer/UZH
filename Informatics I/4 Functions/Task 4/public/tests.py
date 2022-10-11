#!/usr/bin/env python3
from unittest import TestCase

from public import script

# This test suite only tests whether the value returned by
# the solution function has the correct type. If this test
# passes, that does not mean that you will get any points.
# The grading system uses different, more exhaustive tests.

# Feel free to extend the class with your own test cases,
# which will then also be executed in every "Test & Run".

IP_STRING = "127.0.0.1"

class PublicTestSuite(TestCase):
    def test_return_type(self):
        self.assertTrue(script.is_valid_IP(IP_STRING))
