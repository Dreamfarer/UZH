#!/usr/bin/env python3

from unittest import TestCase
from public.script import MagicDrawingBoard


class PublicTestSuite(TestCase):

    def test_example(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        db.rect((2, 2), (5, 4))
        actual = db.img()
        expected = "\n".join(["000000",
                              "010000",
                              "001110",
                              "001110"])
        self.assertEqual(expected, actual)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
