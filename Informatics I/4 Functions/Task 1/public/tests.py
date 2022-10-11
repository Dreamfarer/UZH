#!/usr/bin/env python3

from unittest import TestCase
from public.script import fac


class PublicTestSuite(TestCase):

    def test1(self):
         self.assertEqual(120, fac(5))

