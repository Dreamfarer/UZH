###############################################################################
# TESTING IN VS CODE
#   First off, you need to navigate your terminal to the current task's folder.
# Copy the following command into the terminal below:
# cd "Informatics I/7 Testing/Task 1 Regression Testing Median/"
#   To run the unit tests, copy the following line into the terminal below:
# python -m unittest public/tests.py
###############################################################################
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
    
    # Additional test case for floating point numbers
    def test_median_works_for_single_float(self):
        self.assertAlmostEqual(5.90, median([5.90]))

    def test_median_works_for_sorted_numbers(self):
        self.assertEqual(2, median([1, 2, 6]))

    def test_median_works_for_unsorted_numbers(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_odd_lists(self):
        self.assertEqual(2, median([6, 1, 2]))

    # Test case changed to incorporate average requirement
    def test_median_works_for_even_lists(self):
        self.assertAlmostEqual(4.5, median([4, 5]))
    
    # Additional test case if an empty list ist provided
    def test_median_works_for_empty_list(self):
        self.assertEqual(None, median([]))

