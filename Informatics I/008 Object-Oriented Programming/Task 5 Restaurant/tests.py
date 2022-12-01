#!/usr/bin/env python3

from unittest import TestCase
from public.script import Restaurant
from public.item import Item


class PublicTestSuite(TestCase):

    def test_get_revenue_perytron(self):
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


    def test_get_revenue_paul(self):
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

    def test_get_revenue_empty_orderlist_paul(self):
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
        self.assertEqual(restaurant.get_order_list(), "No order yet")
        self.assertEqual(actual, expected)

    def test_get_revenue_empty_orderlist2_paul(self):
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
        self.assertEqual(restaurant.get_order_list(), "No order yet")
        self.assertEqual(actual, expected)

    def test_get_revenue2_paul(self):
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

    def test_get_revenue3_paul(self):
        # Create Item Objects with Name and Price
        steak = Item("Steak", 10)
        salad = Item("Salad", 10)
        fish = Item("Fish", 10.5)
        pizza = Item("Pizza", 10)
        # Create menu list
        menu_list = [steak, fish]
        # Create order list
        order_list = [steak, steak, salad, pizza, fish]
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

    def test_get_revenue1_codecycle(self):
        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)

        restaurant = Restaurant("Zurich_1", [steak, salad, fish])
        restaurant.set_order([steak, steak, salad, pizza])
        self.assertEqual(60, restaurant.get_revenue())

    def test_get_revenue2_codecycle(self):
        hamburger = Item("Hamburger", 20)
        pizza = Item("Pizza", 35)
        steak = Item("Steak", 50)

        restaurant = Restaurant("Zurich_1", [hamburger, pizza])
        restaurant.set_order([pizza, pizza, hamburger, steak])
        self.assertEqual(90, restaurant.get_revenue())
