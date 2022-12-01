#!/usr/bin/env python3

from unittest import TestCase
from public.knight import Knight
from public.rogue import Rogue

class TestBattle(TestCase):

    def test_basic_attack(self):
        sut = Knight("Arthur", 3)
        actual = sut.get_health()
        expected = (150, 150)
        self.assertEqual(expected, actual)

    def test_knight_attack(self):
        k = Knight("Arthur", 3)
        r = Rogue("Shades", 3)
        k.attack(r)
        actual = r.get_health()[0]
        expected = 150 - round(0.8*(3*10+0))
        self.assertEqual(expected, actual)

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
