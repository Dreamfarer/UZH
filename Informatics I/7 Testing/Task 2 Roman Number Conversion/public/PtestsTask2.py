#!/usr/bin/env python3
from unittest import TestCase
from script import convert_roman_to_int



# You are supposed to develop the functionality in a test-driven way.
# Think about relevant test cases and extend the following test suite
# until all requirements of the description are covered. The test suite
# will be run against various correct and incorrect implementations, so
# make sure that you only test the `move` function and stick strictly
# to its defined signature.
#
# Make sure that you define test methods and that each method
# _directly_ includes an assertion in the body, or -otherwise- the
# grading will mark the test suite as invalid.
class ConversionTestSuite(TestCase):

    def _assert(self, roman, expected):
        actual = convert_roman_to_int(roman)
        m = f"should be {expected} but was {actual}"
        self.assertEqual(expected, actual, m)
    
    # def _assertWarning(self, roman, expected):
    #     actual = convert_roman_to_int(roman)
    #     m = "Trying to assert warning"
    #     self.assertWarns(expected, convert_roman_to_int, roman)

    def test_simple_numeralI(self):
        self._assert("I", 1)

    def test_simple_numeralV(self):
        self._assert("V", 5)

    def test_simple_numeralX(self):
        self._assert("X", 10)

    def test_simple_numeralL(self):
        self._assert("L", 50)

    def test_simple_numeralC(self):
        self._assert("C", 100)

    def test_simple_numeralD(self):
        self._assert("D", 500)

    def test_simple_numeralM(self):
        self._assert("M", 1000)


    def test_simple_additive1(self):
        self._assert("XI", 11)

    def test_simple_additive2(self):
        self._assert("MD", 1500)
    
        
    #My implementation
    def test_simple_additive3(self):
        self._assert("XII", 12)
        
    def test_simple_additive4(self):
        self._assert("LXXX", 80)
        
    
    #Subtractions
    def test_simple_subtractive1(self):
        self._assert("IV", 4)
        
    def test_simple_subtractive2(self):
        self._assert("XL", 40)
        
    def test_simple_subtractive3(self):
        self._assert("IX", 9)
        
    def test_simple_subtractive4(self):
        self._assert("XC", 90)

    def test_simple_subtractive5(self):
        self._assert("CM", 900)
        
        
    #Long additions
    def test_simple_longadd1(self):
        self._assert("VIII", 8)
        
    def test_simple_longadd2(self):
        self._assert("XVII", 17)
        
    def test_simple_longadd3(self):
        self._assert("MDC", 1600)
        
    def test_simple_longadd4(self):
        self._assert("CLXXVIII", 178)

    def test_simple_longadd5(self):
        self._assert("DLI", 551)
    
        
    #Additions and Subtractions
    def test_simple_addsub1(self):
        self._assert("XIV",14)
        
    def test_simple_addsub2(self):
        self._assert("XLI",41)
        
    def test_simple_addsub3(self):
        self._assert("XCIX",99)
        
    def test_simple_addsub4(self):
        self._assert("CMIV",904)

    def test_simple_addsub5(self):
        self._assert("CDXLIV",444)
        
        
        
    #lasts cases:
    def test_simple_lastcase1(self):
        self._assert("MMMMMI",5001)
        
    def test_simple_lastcase2(self):
        self._assert("CDXC",490)
        
    def test_simple_last3(self):
        self._assert("XLIX",49)
        
    
        
        
    #Check if warning is thrown for invalid chars
    #Additions and Subtractions
    # def test_simple_invalidchars1(self):
    #     self._assertWarning(Warning, "XLS")
        
    # def test_simple_invalidchars2(self):
    #     self._assertWarning(Warning, "*jrIX")
    

   #check for warning when smaller-valued letters before larger-valued ones, like "IIMX", "IVII" etc)     
    # def test_simple_smalllarge1(self):
    #     self._assert("XIV",14)
        
    # def test_simple_smalllarge2(self):
    #     self._assert("XLI",41)
        
    # def test_simple_smalllarge3(self):
    #     self._assert("XCIX",99)
    
    
    #numerals of the pattern "IVIV", "IXIX" raise a warning.
    # def test_simple_pattern1(self):
    #     self._assert("XIV",14)
        
    # def test_simple_pattern2(self):
    #     self._assert("XLI",41)
        
    # def test_simple_pattern3(self):
    #     self._assert("XCIX",99)
        
        
    #numerals that should not be repeated (e.g. "VV", "DD", "LL") raise a warning.
    # def test_simple_repeated1(self):
    #     self._assert("XIV",14)
        
    # def test_simple_repeated2(self):
    #     self._assert("XLI",41)
        
    # def test_simple_repeated3(self):
    #     self._assert("XCIX",99)


    #Check that any number of "M"s are allowed, e.g. "MMMMMI".
    
    #Check that cases "CDXC" and "XLIX" are accepted,
    
    #Check that cases "VIV" or LLX are rejected with a Warning.
    

















