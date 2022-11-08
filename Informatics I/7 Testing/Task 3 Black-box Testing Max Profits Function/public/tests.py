###############################################################################
# TESTING IN VS CODE
#   First off, you need to navigate your terminal to the current task's folder.
# Copy the following command into the terminal below:
# cd "Informatics I/7 Testing/Task 3 Black-box Testing Max Profits Function/"
#   To run the unit tests, copy the following line into the terminal below:
# python -m unittest public/tests.py
###############################################################################
from unittest import TestCase
from public.script import max_profit

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class MaxProfitTest(TestCase):

    # Check for non-list type inputs
    def test_input_not_list(self):
        self.assertEqual("Invalid Input Type", max_profit(-1))
    
    # Check for empty price list
    def test_input_empty_list(self):
        self.assertEqual("Empty Price List", max_profit([]))
    
    # Check for invalid data type within list
    def test_input_invalid_data_type_within_list(self):
        self.assertEqual("Invalid Data Type within List", max_profit(["uzh"]))
    
    # Check for invalid prices within list
    def test_input_invalid_prices_within_list(self):
        self.assertEqual("Invalid Prices", max_profit([-1, 2]))

    # Check if list only contains one valid number
    def test_input_single_number(self):
        self.assertEqual(0, max_profit([1]))

    # Check if cannot find a pair of prices where the first price is lower than the second price
    def test_input_cannot_find_lower_price_first(self):
        self.assertEqual(0, max_profit([3,2,1]))

    # Check if the calculations of max_profit function are correct
    def test_validate_output(self):
        self.assertEqual(4, max_profit([1, 2, 3, 4, 5]))
