#!/usr/bin/env python3

from unittest import TestCase
from script import ProfanityFilter


class PublicTestSuite(TestCase):

    def test_example(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)
        
    def test_1(self):    
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard shot"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? ?#$?"
        self.assertEqual(expected, actual)
        
    def test_2(self):    
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc ducki MastArd jklmno"
        actual = f.filter(msg)
        expected = "abc ?#$?i ?#$?#$? jklmno"
        self.assertEqual(expected, actual)
        
    def test_3(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "fafa defghi mastard shotibatchmmastaRdk lmno"
        actual = f.filter(msg)
        expected = "fafa defghi ?#$?#$? ?#$?i?#$?#m?#$?#$?k lmno"
        self.assertEqual(expected, actual)
        
        
    def test_4(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "FaI heiHkaoe"
        actual = f.filter(msg)
        expected = "FaI heiHkaoe"
        self.assertEqual(expected, actual)
        
        

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
