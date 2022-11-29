###############################################################################
# TESTING IN VS CODE
#   First off, you need to navigate your terminal to the current task's folder.
# Copy the following command into the terminal below:
# cd "Informatics I/8 Object-Oriented Programming\Task 1 Profanity Filter/"
#   To run the unit tests, copy the following line into the terminal below:
# python -m unittest public/tests.py
###############################################################################
from unittest import TestCase
from public.script import ProfanityFilter


class PublicTestSuite(TestCase):

    def test_example_1(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)
    
    def test_example_2(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi Mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)
    
    def test_example_3(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi 3lMastardIUS jklmno"
        actual = f.filter(msg)
        expected = "abc defghi 3l?#$?#$?IUS jklmno"
        self.assertEqual(expected, actual)
    
    def test_example_4(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard", "mastard2"], "?#$")
        msg = "abc defghi mastard2 jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$?# jklmno"
        self.assertEqual(expected, actual)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
