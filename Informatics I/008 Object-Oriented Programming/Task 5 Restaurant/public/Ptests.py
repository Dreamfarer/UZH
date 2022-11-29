#!/usr/bin/env python3

from unittest import TestCase
from script import Restaurant
from item import Item


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
        
        
    def test_get_revenue_empty_orderlist(self):
        # Create Item Objects with Name and Price
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)
        # Create menu list
        menu_list = [steak, salad, fish]
        # Create order list
        order_list = []
        # Create restaurant object with name and menu list
        restaurant = Restaurant("Zurich_1", menu_list)
        # Create an order with the order list
        restaurant.set_order(order_list)
        # Get the revenue of the restaurant object
        actual = restaurant.get_revenue()
        # Expected return
        expected = 0
        # Assertion
        self.assertEqual(restaurant.get_order_list(),"No order yet")
        self.assertEqual(actual, expected)
        
    def test_get_revenue_empty_orderlist2(self):
        # Create Item Objects with Name and Price
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)
        # Create menu list
        menu_list = [steak, salad, fish]
        # Create order list
        order_list = [pizza]
        # Create restaurant object with name and menu list
        restaurant = Restaurant("Zurich_1", menu_list)
        # Create an order with the order list
        restaurant.set_order(order_list)
        # Get the revenue of the restaurant object
        actual = restaurant.get_revenue()
        # Expected return
        expected = 0
        # Assertion
        self.assertEqual(restaurant.get_order_list(),"No order yet")
        self.assertEqual(actual, expected)
        
    def test_get_revenue2(self):
        # Create Item Objects with Name and Price
        steak = Item("Steak", 20)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)
        # Create menu list
        menu_list = [steak, salad, fish, pizza]
        # Create order list
        order_list = [steak, steak, salad, pizza, salad, steak, fish]
        # Create restaurant object with name and menu list
        restaurant = Restaurant("Zurich_1", menu_list)
        # Create an order with the order list
        restaurant.set_order(order_list)
        # Get the revenue of the restaurant object
        actual = restaurant.get_revenue()
        # Expected return
        expected = 150
        # Assertion
        self.assertEqual(actual, expected)
        
    def test_get_revenue3(self):
        # Create Item Objects with Name and Price
        steak = Item("Steak", 10)
        salad = Item("Salad", 10)
        fish = Item("Fish", 10.5)
        pizza = Item("Pizza", 10)
        # Create menu list
        menu_list = [steak,fish]
        # Create order list
        order_list = [steak, steak, salad, pizza,fish]
        # Create restaurant object with name and menu list
        restaurant = Restaurant("Zurich_1", menu_list)
        # Create an order with the order list
        restaurant.set_order(order_list)
        # Get the revenue of the restaurant object
        actual = restaurant.get_revenue()
        # Expected return
        expected = 30.5
        # Assertion
        self.assertEqual(actual, expected)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
