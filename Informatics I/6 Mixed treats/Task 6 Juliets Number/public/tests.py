#!/usr/bin/env python3

from unittest import TestCase
from public import script

# This test suite does not exhaustively test the implementation,
# a passing "test & run" does not mean that all possible cases
# have been considered. For the grading, an extended tests suite
# will be executed that will cover many more cases.

# Feel free to add additional test cases here. All test cases
# will be executed as part of the "Test & Run".

class PublicTestSuite(TestCase):

    def test_1(self):
        script.wa_nrs = []
        
        actual = script.get_possible_nrs("077342119")
        self.assertEqual([], actual, "script should not find any number on an empty wa_nrs list")
