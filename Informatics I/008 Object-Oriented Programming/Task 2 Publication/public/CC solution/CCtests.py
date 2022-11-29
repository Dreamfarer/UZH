#!/usr/bin/env python3

from unittest import TestCase
from public.script import Publication

class PublicTestSuite(TestCase):

    def test_to_string(self):
        pub = Publication(["Duvall", "Matyas"], "Continuous Integration", 2007)
        self.assertEqual(str(pub), "Publication([\"Duvall\", \"Matyas\"], \"Continuous Integration\", 2007)")

    def test_equal(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["A"], "B", 1234)
        self.assertEqual(a, b)

    def test_not_equal(self):
        a = Publication(["A"], "B", 1234)
        b = Publication(["B"], "C", 2345)
        self.assertNotEqual(a, b)
    
