#!/usr/bin/env python3

from unittest import TestCase
from public.script import invert


# This test suite does not exhaustively test the
# implementation, a passing "test & run" does not mean that all
# possible cases have been considered. For the grading, an
# extended tests suite will be executed that will cover many
# more cases.

# Feel free to add additional test cases here. All test cases
# will be executed as part of the "Test & Run".

class PublicTestSuite(TestCase):

    def test_1(self):
        actual = invert({"a": 1, "b": 1, "c": 3})
        expected = {1: ["a", "b"], 3: ["c"]}
        self.assertEqual(expected, actual)
