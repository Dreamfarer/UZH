#!/usr/bin/env python3

from unittest import TestCase
from public.word_logic import WordLogic


class PublicTestSuite(TestCase):

    def test_example(self):
        w = WordLogic(10, 7, 5)
        self.assertEqual(10, w.num_words)
        self.assertEqual(7, w.len_words)
        self.assertEqual(5, w.num_attempts)
        self.assertEqual(len(w.words), w.num_words)
        self.assertEqual(w.password in w.words, True)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.

