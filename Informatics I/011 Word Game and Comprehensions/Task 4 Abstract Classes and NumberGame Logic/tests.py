#!/usr/bin/env python3

from unittest import TestCase
from word_logic import WordLogic
from number_logic import NumberLogic
from abc import ABC, abstractmethod

class PublicTestSuite(TestCase):

    def test_example(self):
        w = WordLogic(10, 7, 5)
        self.assertEqual(10, w.num_words)
        self.assertEqual(7, w.len_words)
        self.assertEqual(5, w.num_attempts)
        self.assertEqual(len(w.words), w.num_words)
        self.assertEqual(w.password in w.words, True)
        
        
    def test_word1(self):
        w = WordLogic(4, 4, 3)
        self.assertEqual(4, w.num_words)
        self.assertEqual(4, w.len_words)
        self.assertEqual(3, w.num_attempts)
        self.assertEqual(len(w.words), w.num_words)
        self.assertEqual(w.password in w.words, True)
        
    
        
    def test_number1(self):
        w = NumberLogic(5,5,5)
        self.assertEqual(5, w.num_words)
        self.assertEqual(5, w.len_words)
        self.assertEqual(5, w.num_attempts)
        self.assertEqual(len(w.words), w.num_words)
        self.assertEqual(w.password in w.words, True)
        
    def test_number2(self):
        w = NumberLogic(4, 4, 5)
        
        self.assertRaises(Warning,w.check,"2344")    
        self.assertRaises(Warning,w.check,"1234567")    

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.

