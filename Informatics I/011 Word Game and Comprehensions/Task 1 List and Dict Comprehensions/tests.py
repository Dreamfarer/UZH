#!/usr/bin/env python3
from unittest import TestCase
import script as script

class PublicTestSuite(TestCase):

    def test_example(self):
        self.assertTrue(len(script.words_with_length(12)) == 208)

    def test_words_containing_string_patertuck(self):
        actual = script.words_containing_string("anno")
        expected = ['cannon', 'shannon', 'announce', 'annoying', 'annotated', 'announced', 'announces', 'annotation',
                    'announcement', 'announcements']
        self.assertTrue((actual == expected))

    def test_words_starting_with_character_patertuck(self):
        actual = script.words_starting_with_character("y")
        expected = ['yale', 'yang', 'yard', 'yarn', 'yeah', 'year', 'yoga', 'york', 'your', 'yacht', 'yahoo', 'yards',
                    'years', 'yeast', 'yemen', 'yield', 'young', 'yours', 'youth', 'yukon', 'yamaha', 'yearly',
                    'yellow', 'yields', 'younger', 'yourself', 'yesterday', 'yorkshire', 'yugoslavia']

    def test_alphabet_patertuck(self):
        actual = script.alphabet()
        expected = "abcdefghijklmnopqrstuvwxyz"
        self.assertTrue(actual == expected)

    def test_dictionary_patertuck(self):
        actual = script.dictionary()["z"]
        expected = ['zero', 'zinc', 'zone', 'zoom', 'zope', 'zdnet', 'zones', 'zambia', 'zoloft', 'zoning',
                    'zshops', 'zealand', 'zimbabwe', 'zoophilia']
        self.assertTrue(actual == expected)

    def test_censor_patertuck(self):
        actual = script.censored_words("ac")[:10]
        expected = ['able', 'xxxx', 'xxxx', 'xxxx', 'xxxx', 'xxxx', 'adam', 'adds', 'adsl', 'aged']
        self.assertTrue(actual == expected)

