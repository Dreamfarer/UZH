#!/usr/bin/env python3

from unittest import TestCase
from public.script import GameRunner


class PublicTestSuite(TestCase):

    def test_example(self):
        g = GameRunner()
        res = g.generate_hex_codes()
        self.assertEqual(len(res), g.rows * g.columns)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.

