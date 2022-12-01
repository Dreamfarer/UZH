#!/usr/bin/env python3
from unittest import TestCase
from public.script import max_profit

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class MaxProfitTest(TestCase):

    def test_maxprofit_should_return_invalid_when_input_int(self):
        self.assertEqual("Invalid Input Type", max_profit(1))

    def test_maxprofit_should_return_invalid_when_input_float(self):
        self.assertEqual("Invalid Input Type", max_profit(2.54))

    def test_maxprofit_should_return_invalid_when_input_boolean(self):
        self.assertEqual("Invalid Input Type", max_profit(True))

    def test_maxprofit_should_return_invalid_when_input_string(self):
        self.assertEqual("Invalid Input Type", max_profit("hallo"))

    def test_maxprofit_should_return_invalid_when_input_dictionary(self):
        self.assertEqual("Invalid Input Type", max_profit({"a": 2,"b": 3}))

    def test_maxprofit_should_return_invalid_when_input_none(self):
        self.assertEqual("Invalid Input Type", max_profit(None))

    def test_maxprofit_should_return_empty_when_list_empty(self):
        self.assertEqual("Empty Price List", max_profit([]))

    def test_maxprofit_should_return_invalid_type_when_list_with_string(self):
        self.assertEqual("Invalid Data Type within List", max_profit(["adfs", 125]))

    def test_maxprofit_should_return_invalid_prices_when_list_with_negative_int(self):
        self.assertEqual("Invalid Prices", max_profit([-254, 125, 61]))

    def test_maxprofit_should_return_invalid_prices_when_list_with_negative_int_other(self):
        self.assertEqual("Invalid Prices", max_profit([-6]))

    def test_maxprofit_should_return_zero_when_list_with_one_item(self):
        self.assertEqual(0, max_profit([83]))

    def test_maxprofit_should_return_zero_when_list_with_no_right_pair(self):
        self.assertEqual(0, max_profit([100, 25]))

    def test_maxprofit_should_return_correct_when_valid(self):
        self.assertEqual(480, max_profit([20, 500]))

    def test_maxprofit_should_return_correct_when_valid_other(self):
        self.assertEqual(4, max_profit([1, 2, 3, 4, 5]))
