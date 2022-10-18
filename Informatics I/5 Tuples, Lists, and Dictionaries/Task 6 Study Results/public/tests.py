#!/usr/bin/env python3

from unittest import TestCase
from public.script import get_average_grade


class PublicTestSuite(TestCase):

    def test_example_file(self):
        actual = get_average_grade("public/my_grades.txt")
        expected = 3.5
        self.assertEqual(expected, actual)

    def test_non_existing_file(self):
        actual = get_average_grade("non_existing_file.txt")
        expected = None
        self.assertEqual(expected, actual)

