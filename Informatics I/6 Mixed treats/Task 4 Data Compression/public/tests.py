#!/usr/bin/env python3

from unittest import TestCase
from public.script import compress

# This test suite does not exhaustively test the implementation,
# a passing "test & run" does not mean that all possible cases
# have been considered. For the grading, an extended tests suite
# will be executed that will cover many more cases.

# Feel free to add additional test cases here. All test cases
# will be executed as part of the "Test & Run".

class PublicTestSuite(TestCase):

    def test_1(self):
        actual = compress([
            {"a": 1, "b": 2, "c": 3},
            {"a": 9, "c": 7, "b": 8}
        ])
        expected = (
            ("a", "b", "c"),
            [
                (1, 2, 3),
                (9, 8, 7)
            ]
        )
        self.assertEqual(expected, actual)
