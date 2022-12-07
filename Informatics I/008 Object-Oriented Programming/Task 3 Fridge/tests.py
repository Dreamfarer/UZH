#!/usr/bin/env python3
from unittest import TestCase
from public.script import Fridge


class PublicTestSuite(TestCase):

    def test_example_perytron(self):
        f = Fridge()
        # put an item into the fridge
        f.store((191112, "Butter"))
        self.assertEqual(1, len(f))
        # take it out again
        item = f.take((191112, "Butter"))
        self.assertEqual(0, len(f))
        # is it the right item?
        self.assertEqual((191112, "Butter"), item)


    def test_store_take_codecylce(self):
        f = Fridge()
        f.store((191112, "Butter"))
        self.assertEqual(1, len(f))
        item = f.take((191112, "Butter"))
        self.assertEqual(0, len(f))
        self.assertEqual((191112, "Butter"), item)

    def test_find_codecylce(self):
        f = Fridge()
        f.store((191113, "Butter"))
        f.store((191112, "Butter"))
        self.assertEqual((191112, "Butter"), f.find("Butter"))

    def test_take_before_codecylce(self):
        f = Fridge()
        f.store((191127, "Butter"))
        f.store((191117, "Milk"))
        self.assertEqual([(191117, "Milk")], f.take_before(191120))
        self.assertEqual(1, len(f))
