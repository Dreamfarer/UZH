#!/usr/bin/env python3
from unittest import TestCase
from public.script import median

# Extend the test suite with regression tests that cover the
# meaningful bug reports. Make sure that you define test methods
# and that each method _directly_ includes an assertion in the
# body, or -otherwise- the grading will mark the test suite as
# invalid.
class MedianTests(TestCase):

    def test_median_works_for_single_elements(self):
        self.assertEqual(13, median([13]))

    def test_median_works_for_sorted_numbers(self):
        self.assertEqual(2, median([1, 2, 6]))

    def test_median_works_for_unsorted_numbers(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_odd_lists(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_even_lists(self):
        self.assertEqual(3, median([5, 1]))
