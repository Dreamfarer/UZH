#!/usr/bin/env python3
from unittest import TestCase
from Patertuck_Task_3_Black_Box_Testing_Max_Profits_Function import max_profit


# from public.script import max_profit

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class MaxProfitTest(TestCase):

    def test_input_non_list1(self):
        self.assertEqual(max_profit(-3), "Invalid Input Type")

    def test_input_non_list2(self):
        self.assertEqual(max_profit({"Hello": 3, "HI": "Bye"}), "Invalid Input Type")

    def test_empty_list1(self):
        self.assertEqual(max_profit([]), "Empty Price List")

    def test_list_non_int1(self):
        self.assertEqual(max_profit(["Hello", 1, 2, 3]), "Invalid Data Type within List")

    def test_negative_prices1(self):
        self.assertEqual(max_profit([1, 2, -3]), "Invalid Prices")

    def test_only_one_element1(self):
        self.assertEqual(max_profit([1]), 0)

    def test_highest_price_before_lowest1(self):
        self.assertEqual(max_profit([5, 4, 1]), 0)

    def test_highest_price_before_lowest2(self):
        self.assertEqual(max_profit([10, 3, 1]), 0)

    def test_standard_test1(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)
