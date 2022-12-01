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

    def test_example_1_perytron(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)
    
    def test_example_2_perytron(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi Mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)
    
    def test_example_3_perytron(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi 3lMastardIUS jklmno"
        actual = f.filter(msg)
        expected = "abc defghi 3l?#$?#$?IUS jklmno"
        self.assertEqual(expected, actual)
    
    def test_example_4_perytron(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard", "mastard2"], "?#$")
        msg = "abc defghi mastard2 jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$?# jklmno"
        self.assertEqual(expected, actual)


    def test_example_paul(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)

    def test_1_paul(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard shot"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? ?#$?"
        self.assertEqual(expected, actual)

    def test_2_paul(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc ducki MastArd jklmno"
        actual = f.filter(msg)
        expected = "abc ?#$?i ?#$?#$? jklmno"
        self.assertEqual(expected, actual)

    def test_3_paul(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "fafa defghi mastard shotibatchmmastaRdk lmno"
        actual = f.filter(msg)
        expected = "fafa defghi ?#$?#$? ?#$?i?#$?#m?#$?#$?k lmno"
        self.assertEqual(expected, actual)

    def test_4_paul(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "FaI heiHkaoe"
        actual = f.filter(msg)
        expected = "FaI heiHkaoe"
        self.assertEqual(expected, actual)

