#!/usr/bin/env python3

from unittest import TestCase
from public.script import Restaurant
from public.item import Item

class PublicTestSuite(TestCase):

    def test_get_revenue1(self):

        steak = Item("Steak", 25)
        salad = Item("Salad", 10)
        fish = Item("Fish", 30)
        pizza = Item("Pizza", 40)

        restaurant = Restaurant("Zurich_1", [steak, salad, fish])
        restaurant.set_order([steak, steak, salad, pizza])
        self.assertEqual(60, restaurant.get_revenue())

    def test_get_revenue2(self):

        hamburger = Item("Hamburger", 20)
        pizza = Item("Pizza", 35)
        steak = Item("Steak", 50)

        restaurant = Restaurant("Zurich_1", [hamburger, pizza])
        restaurant.set_order([pizza, pizza, hamburger, steak])
        self.assertEqual(90, restaurant.get_revenue())

    