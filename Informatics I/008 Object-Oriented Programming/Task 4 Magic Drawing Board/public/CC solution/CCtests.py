#!/usr/bin/env python3

from unittest import TestCase
from public.script import MagicDrawingBoard

class PublicTestSuite(TestCase):

    def test_pixel(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        self.assertEqual(db.img(), "\n".join(["000000",
                                              "010000",
                                              "000000",
                                              "000000"]))

    def test_rect(self):
        db = MagicDrawingBoard(6, 4)
        db.rect((2, 2), (5, 4))
        self.assertEqual(db.img(), "\n".join(["000000",
                                              "000000",
                                              "001110",
                                              "001110"]))

    def test_reset(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        db.reset()
        db.rect((2, 2), (5, 4))
        self.assertEqual(db.img(), "\n".join(["000000",
                                              "000000",
                                              "001110",
                                              "001110"]))

