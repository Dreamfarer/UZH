#!/usr/bin/env python3

from unittest import TestCase
from public.script import MagicDrawingBoard


class PublicTestSuite(TestCase):

    def test_example_perytron(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        db.rect((2, 2), (5, 4))
        actual = db.img()
        expected = "\n".join(["000000",
                              "010000",
                              "001110",
                              "001110"])
        self.assertEqual(expected, actual)


    def test_example_paul(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        db.rect((2, 2), (5, 4))
        actual = db.img()
        expected = "\n".join(["000000",
                              "010000",
                              "001110",
                              "001110"])
        self.assertEqual(expected, actual)

    def test_warning_datatype1_paul(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(-1, 4)

    def test_warning_datatype2_paul(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(1, "e")

    def test_warning_datatype3_paul(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(2.3, 4)

    def test_warning_pixel1_paul(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6, 4)
            db.pixel((-1, 1))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])

    def test_warning_pixel2_paul(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6, 4)
            db.pixel((2, "eai"))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])

    def test_warning_pixel3_paul(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6, 4)
            db.pixel((2, 4))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])

    def test_warning_rect1_paul(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6, 4)
            db.rect((-1, 1), (4, 1))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])

    def test_warning_rect2_paul(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6, 4)
            db.rect(("ea", 1), (4, 1))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])

    def test_warning_rect3_paul(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6, 4)
            db.rect((-1, 1), (4, 3.1))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])

    def test_warning_rect4_paul(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6, 4)
            db.rect((2, 3), (1, 1))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])

    def test_example1_paul(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((5, 3))
        db.rect((0, 0), (2, 2))
        actual = db.img()
        expected = "\n".join(["110000",
                              "110000",
                              "000000",
                              "000001"])
        self.assertEqual(expected, actual)

    def test_example2_paul(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        db.pixel((2, 2))
        db.pixel((5, 3))
        db.rect((0, 0), (6, 1))
        db.rect((2, 2), (5, 4))
        actual = db.img()
        expected = "\n".join(["111111",
                              "010000",
                              "001110",
                              "001111"])
        self.assertEqual(expected, actual)

    def test_example3_paul(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        db.rect((0, 0), (2, 4))
        db.rect((0, 3), (6, 4))
        actual = db.img()
        expected = "\n".join(["110000",
                              "110000",
                              "110000",
                              "111111"])
        self.assertEqual(expected, actual)

    def test_example4_paul(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        db.rect((2, 2), (5, 4))
        db.reset()
        actual = db.img()
        expected = "\n".join(["000000",
                              "000000",
                              "000000",
                              "000000"])
        self.assertEqual(expected, actual)

    # def test_example_paul(self):
    #     db = MagicDrawingBoard(6, 4)
    #     db.pixel((1, 1))
    #     db.rect((2, 2), (5, 4))
    #     actual = db.img()
    #     expected = "\n".join(["000000",
    #                           "010000",
    #                           "001110",
    #                           "001110"])
    #     self.assertEqual(expected, actual)

    def test_pixe_codecylce(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        self.assertEqual(db.img(), "\n".join(["000000",
                                              "010000",
                                              "000000",
                                              "000000"]))

    def test_rect_codecylce(self):
        db = MagicDrawingBoard(6, 4)
        db.rect((2, 2), (5, 4))
        self.assertEqual(db.img(), "\n".join(["000000",
                                              "000000",
                                              "001110",
                                              "001110"]))

    def test_reset_codecylce(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        db.reset()
        db.rect((2, 2), (5, 4))
        self.assertEqual(db.img(), "\n".join(["000000",
                                              "000000",
                                              "001110",
                                              "001110"]))

