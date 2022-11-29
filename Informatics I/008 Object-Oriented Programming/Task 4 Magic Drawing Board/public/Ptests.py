#!/usr/bin/env python3

from unittest import TestCase
from script import MagicDrawingBoard


class PublicTestSuite(TestCase):

    def test_example(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        db.rect((2, 2), (5, 4))
        actual = db.img()
        expected = "\n".join(["000000",
                              "010000",
                              "001110",
                              "001110"])
        self.assertEqual(expected, actual)
        
    def test_warning_datatype1(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(-1,4)
    def test_warning_datatype2(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(1,"e")
            
    def test_warning_datatype3(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(2.3,4)
            
    def test_warning_pixel1(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6,4)
            db.pixel((-1, 1))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])
    def test_warning_pixel2(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6,4)
            db.pixel((2, "eai"))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])
            
    def test_warning_pixel3(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6,4)
            db.pixel((2, 4))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])
    def test_warning_rect1(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6,4)
            db.rect((-1, 1),(4,1))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])
            
    def test_warning_rect2(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6,4)
            db.rect(("ea", 1),(4,1))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])
    def test_warning_rect3(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6,4)
            db.rect((-1, 1),(4,3.1))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])
    def test_warning_rect4(self):
        with self.assertRaises(Warning):
            db = MagicDrawingBoard(6,4)
            db.rect((2, 3),(1,1))
            actual = db.img()
            expected = "\n".join(["000000",
                                  "010000",
                                  "001110",
                                  "001110"])
            
        
        
    def test_example1(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((5,3))
        db.rect((0,0),(2,2))
        actual = db.img()
        expected = "\n".join(["110000",
                              "110000",
                              "000000",
                              "000001"])
        self.assertEqual(expected, actual)
        
    def test_example2(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        db.pixel((2,2))
        db.pixel((5,3))
        db.rect((0,0),(6,1))
        db.rect((2, 2), (5, 4))
        actual = db.img()
        expected = "\n".join(["111111",
                              "010000",
                              "001110",
                              "001111"])
        self.assertEqual(expected, actual)
        
        
    def test_example3(self):
        db = MagicDrawingBoard(6, 4)
        db.pixel((1, 1))
        db.rect((0,0), (2,4))
        db.rect((0,3),(6,4))
        actual = db.img()
        expected = "\n".join(["110000",
                              "110000",
                              "110000",
                              "111111"])
        self.assertEqual(expected, actual)
        
        
    def test_example4(self):
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
        
        
    # def test_example(self):
    #     db = MagicDrawingBoard(6, 4)
    #     db.pixel((1, 1))
    #     db.rect((2, 2), (5, 4))
    #     actual = db.img()
    #     expected = "\n".join(["000000",
    #                           "010000",
    #                           "001110",
    #                           "001110"])
    #     self.assertEqual(expected, actual)
        
        
    

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
