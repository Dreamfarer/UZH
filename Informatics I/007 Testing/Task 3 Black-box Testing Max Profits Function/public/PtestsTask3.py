#!/usr/bin/env python3
from unittest import TestCase
from script import max_profit

# Implement this test suite. Make sure that you define test
# methods and that each method _directly_ includes an assertion
# in the body, or -otherwise- the grading will mark the test
# suite as invalid.
class MaxProfitTest(TestCase):
    
    
       
        
    def test_nonlistinput(self):
        self.assertEquals(max_profit("abc"), "Invalid Input Type")
        
    def test_nonlistinput2(self):
        self.assertEquals(max_profit({'a':2}), "Invalid Input Type")
        
        
        
    def test_emptylistinput(self):
        self.assertEquals(max_profit([]), "Empty Price List")
        
        
        
    def test_invalid_elem_in_list1(self):
        self.assertEquals(max_profit(['a']), "Invalid Data Type within List")
        
    def test_invalid_elem_in_list2(self):
        self.assertEquals(max_profit([4.3,4.1]), "Invalid Data Type within List")
        
    def test_invalid_elem_in_list3(self):
        self.assertEquals(max_profit([[2]]), "Invalid Data Type within List")
        
        
    
    def test_negative_ints1(self):
        self.assertEquals(max_profit([-1,2,3]), "Invalid Prices")
        
    def test_negative_ints2(self):
        self.assertEquals(max_profit([0,2,-3]), "Invalid Prices")
        
        
    def test_returns0_1(self):
        self.assertEquals(max_profit([3]), 0)
        
    def test_returns0_2(self):
        self.assertEquals(max_profit([5,3,1]), 0)
        
    def test_returns0_3(self):
        self.assertEquals(max_profit([10,5,2,0]), 0)
        
        
        
    #test for correct output when input is valid
    def test_correct_output1(self):
        self.assertEquals(max_profit([1,2,3,4,5]),4)
        
    def test_correct_output2(self):
        self.assertEquals(max_profit([1,9,3,8,4]), 8)
        
    def test_correct_output3(self):
        self.assertEquals(max_profit([0,5,2,9,11,2,14,17]), 17)
        
    def test_correct_output4(self):
        self.assertEquals(max_profit([9,3,1,21,13,19,1]), 20)
            
    def test_correct_output5(self):
        self.assertEquals(max_profit([2,4,61,12,34,2,1,39]), 59)
        
    def test_correct_output6(self):
        self.assertEquals(max_profit([11,2,432,432,35,10000,1]), 9998)
        
    
        
    
        
        
        
        
        

        
    
        
    
        
