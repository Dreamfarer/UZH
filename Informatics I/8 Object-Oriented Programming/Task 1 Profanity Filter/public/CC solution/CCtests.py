#!/usr/bin/env python3

from unittest import TestCase
from public.script import ProfanityFilter

class PublicTestSuite(TestCase):

    def test_filter1(self):
        pf = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        result = pf.filter("abc defghi mastard jklmno")
        self.assertEqual("abc defghi ?#$?#$? jklmno", result)

    def test_filter2(self):
        pf = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        result = pf.filter("abc Defghi Mastard jklmno")
        self.assertEqual("abc Defghi ?#$?#$? jklmno", result)
    
