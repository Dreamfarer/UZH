#!/usr/bin/env python3

from unittest import TestCase
from public.script import gcd


class PublicTestSuite(TestCase):

    def test1(self):
        a, b, expected = 33, 17, 1
        actual = gcd(a, b)
        m = f"gcd for {a} and {b} is {expected} and not {actual}"
        self.assertEqual(expected, actual, m)

    def test2(self):
        a, b, expected = 30, 12, 6
        actual = gcd(a, b)
        m = f"gcd for {a} and {b} is {expected} and not {actual}"
        self.assertEqual(expected, actual, m)
