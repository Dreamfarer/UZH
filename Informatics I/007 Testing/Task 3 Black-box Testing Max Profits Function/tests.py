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
    def test_input_not_list_perytron(self):
        self.assertEqual("Invalid Input Type", max_profit(-1))
    
    # Check for empty price list
    def test_input_empty_list_perytron(self):
        self.assertEqual("Empty Price List", max_profit([]))
    
    # Check for invalid data type within list
    def test_input_invalid_data_type_within_list_perytron(self):
        self.assertEqual("Invalid Data Type within List", max_profit(["uzh"]))
    
    # Check for invalid prices within list
    def test_input_invalid_prices_within_list_perytron(self):
        self.assertEqual("Invalid Prices", max_profit([-1, 2]))

    # Check if list only contains one valid number
    def test_input_single_number_perytron(self):
        self.assertEqual(0, max_profit([1]))

    # Check if cannot find a pair of prices where the first price is lower than the second price
    def test_input_cannot_find_lower_price_first_perytron(self):
        self.assertEqual(0, max_profit([3,2,1]))

    # Check if the calculations of max_profit function are correct
    def test_validate_output_perytron(self):
        self.assertEqual(4, max_profit([1, 2, 3, 4, 5]))

    def test_nonlistinput_paul(self):
        self.assertEquals(max_profit("abc"), "Invalid Input Type")

    def test_nonlistinput2_paul(self):
        self.assertEquals(max_profit({'a': 2}), "Invalid Input Type")

    def test_emptylistinput_paul(self):
        self.assertEquals(max_profit([]), "Empty Price List")

    def test_invalid_elem_in_list1_paul(self):
        self.assertEquals(max_profit(['a']), "Invalid Data Type within List")

    def test_invalid_elem_in_list2_paul(self):
        self.assertEquals(max_profit([4.3, 4.1]), "Invalid Data Type within List")

    def test_invalid_elem_in_list3_paul(self):
        self.assertEquals(max_profit([[2]]), "Invalid Data Type within List")

    def test_negative_ints1_paul(self):
        self.assertEquals(max_profit([-1, 2, 3]), "Invalid Prices")

    def test_negative_ints2_paul(self):
        self.assertEquals(max_profit([0, 2, -3]), "Invalid Prices")

    def test_returns0_1_paul(self):
        self.assertEquals(max_profit([3]), 0)

    def test_returns0_2_paul(self):
        self.assertEquals(max_profit([5, 3, 1]), 0)

    def test_returns0_3_paul(self):
        self.assertEquals(max_profit([10, 5, 2, 0]), 0)

    # test for correct output when input is valid
    def test_correct_output1_paul(self):
        self.assertEquals(max_profit([1, 2, 3, 4, 5]), 4)

    def test_correct_output2_paul(self):
        self.assertEquals(max_profit([1, 9, 3, 8, 4]), 8)

    def test_correct_output3_paul(self):
        self.assertEquals(max_profit([0, 5, 2, 9, 11, 2, 14, 17]), 17)

    def test_correct_output4_paul(self):
        self.assertEquals(max_profit([9, 3, 1, 21, 13, 19, 1]), 20)

    def test_correct_output5_paul(self):
        self.assertEquals(max_profit([2, 4, 61, 12, 34, 2, 1, 39]), 59)

    def test_correct_output6_paul(self):
        self.assertEquals(max_profit([11, 2, 432, 432, 35, 10000, 1]), 9998)



    def test_input_non_list1_patertuck(self):
        self.assertEqual(max_profit(-3), "Invalid Input Type")

    def test_input_non_list2_patertuck(self):
        self.assertEqual(max_profit({"Hello": 3, "HI": "Bye"}), "Invalid Input Type")

    def test_empty_list1_patertuck(self):
        self.assertEqual(max_profit([]), "Empty Price List")

    def test_list_non_int1_patertuck(self):
        self.assertEqual(max_profit(["Hello", 1, 2, 3]), "Invalid Data Type within List")

    def test_negative_prices1_patertuck(self):
        self.assertEqual(max_profit([1, 2, -3]), "Invalid Prices")

    def test_only_one_element1_patertuck(self):
        self.assertEqual(max_profit([1]), 0)

    def test_highest_price_before_lowest1_patertuck(self):
        self.assertEqual(max_profit([5, 4, 1]), 0)

    def test_highest_price_before_lowest2_patertuck(self):
        self.assertEqual(max_profit([10, 3, 1]), 0)

    def test_standard_test1_patertuck(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)
