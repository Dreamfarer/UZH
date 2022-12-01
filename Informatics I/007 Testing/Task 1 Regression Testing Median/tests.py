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

    def test_median_works_for_single_elements_perytron(self):
        self.assertEqual(13, median([13]))
    
    # Additional test case for floating point numbers
    def test_median_works_for_single_float_perytron(self):
        self.assertAlmostEqual(5.90, median([5.90]))

    def test_median_works_for_sorted_numbers_perytron(self):
        self.assertEqual(2, median([1, 2, 6]))

    def test_median_works_for_unsorted_numbers_perytron(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_odd_lists_perytron(self):
        self.assertEqual(2, median([6, 1, 2]))

    # Test case changed to incorporate average requirement
    def test_median_works_for_even_lists_perytron(self):
        self.assertAlmostEqual(4.5, median([4, 5]))
    
    # Additional test case if an empty list ist provided
    def test_median_works_for_empty_list_perytron(self):
        self.assertEqual(None, median([]))


    def test_median_works_for_single_elements_paul(self):
        self.assertEqual(13, median([13]))

    def test_median_works_for_sorted_numbers_paul(self):
        self.assertEqual(2, median([1, 2, 6]))

    def test_median_works_for_unsorted_numbers_paul(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_odd_lists_paul(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_even_lists_paul(self):
        self.assertEqual(3, median([5, 1]))

    # My implementation
    def test_median_works_for_firstuser_paul(self):
        self.assertAlmostEqual(6, median([5.9, 6.1]))

    def test_median_works_for_float_paul(self):
        self.assertAlmostEqual(6.1, median([5.9, 6.1, 7.2]))

    def test_median_works_for_float2_paul(self):
        self.assertAlmostEqual(6.2, median([5.9, 6.1, 6.3, 7.2]))

    def test_median_works_for_fourthuser_paul(self):
        self.assertEqual(None, median([]))


    def test_median_works_for_empty_list_patertuck(self):
        self.assertEqual(None, median([]))

    def test_median_works_for_single_elements_patertuck(self):
        self.assertEqual(13, median([13]))

    def test_median_works_for_sorted_numbers_patertuck(self):
        self.assertEqual(2, median([1, 2, 6]))

    def test_median_works_for_unsorted_numbers_patertuck(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_odd_lists_patertuck(self):
        self.assertEqual(2, median([6, 1, 2]))

    def test_median_works_for_even_lists_patertuck(self):
        self.assertEqual(3, median([5, 1]))

    def test_median_works_for_single_float_patertuck(self):
        self.assertEqual(3.3, median([3.3]))

    def test_median_works_for_multiple_floats_patertuck(self):
        self.assertEqual(4.4, median([4.5, 4.3, 3.3, 6.6]))

