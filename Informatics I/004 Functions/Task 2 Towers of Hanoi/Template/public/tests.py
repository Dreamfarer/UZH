#!/usr/bin/env python3

from unittest import TestCase
from public.script import req_steps


class PublicTestSuite(TestCase):

    def test1(self):
        n = 3
        expected = 7
        actual = req_steps(n)
        m = "The calculation is not correct for {} disks.".format(n)
        self.assertEqual(expected, actual, m)

    def test2(self):
        n = 4
        expected = 15
        actual = req_steps(n)
        m = "The calculation is not correct for {} disks.".format(n)
        self.assertEqual(expected, actual, m)
