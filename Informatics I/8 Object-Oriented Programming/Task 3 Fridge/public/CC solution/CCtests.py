#!/usr/bin/env python3
from unittest import TestCase
from public.script import Fridge

class PublicTestSuite(TestCase):

    def test_store_take(self):
        f = Fridge()
        f.store((191112, "Butter"))
        self.assertEqual(1, len(f))
        item = f.take((191112, "Butter"))
        self.assertEqual(0, len(f))
        self.assertEqual((191112, "Butter"), item)

    def test_find(self):
        f = Fridge()
        f.store((191113, "Butter"))
        f.store((191112, "Butter"))
        self.assertEqual((191112, "Butter"), f.find("Butter"))

    def test_take_before(self):
        f = Fridge()
        f.store((191127, "Butter"))
        f.store((191117, "Milk"))
        self.assertEqual([(191117, "Milk")], f.take_before(191120))
        self.assertEqual(1, len(f))

