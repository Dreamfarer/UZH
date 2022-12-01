#!/usr/bin/env python3

from unittest import TestCase
from public.script import Restaurant
from public.item import Item


class PublicTestSuite(TestCase):
    def test_get_revenue(self):
        # Create Item Objects with Name and Price
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)
        # Create menu list
        menu_list = [steak, salad, fish]
        # Create order list
        order_list = [steak, steak, salad, pizza]
        # Create restaurant object with name and menu list
        restaurant = Restaurant("Zurich_1", menu_list)
        # Create an order with the order list
        restaurant.set_order(order_list)
        # Get the revenue of the restaurant object
        actual = restaurant.get_revenue()
        # Expected return
        expected = 60
        # Assertion
        self.assertEqual(actual, expected)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
