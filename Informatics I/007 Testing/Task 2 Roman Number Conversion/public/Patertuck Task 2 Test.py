#!/usr/bin/env python3
from unittest import TestCase
from Patertuck_Task_2_Roman_Number_Conversion import convert_roman_to_int


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

    # basic
    def _assert(self, roman, expected):
        actual = convert_roman_to_int(roman)
        m = f"should be {expected} but was {actual}"
        self.assertEqual(expected, actual, m)

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

    # additive Tests
    def test_simple_additive1(self):
        self._assert("XI", 11)

    def test_simple_additive2(self):
        self._assert("MD", 1500)

    # Subtractive Tests
    def test_simple_subtractive1(self):
        self._assert("IV", 4)

    def test_simple_subtractive2(self):
        self._assert("XL", 40)

    def test_simple_subtractive3(self):
        self._assert("CD", 400)

    def test_simple_subtractive4(self):
        self._assert("IX", 9)

    def test_simple_subtractive5(self):
        self._assert("XC", 90)

    def test_simple_subtractive6(self):
        self._assert("CM", 900)

    # Longer additive numerals
    def test_longer_additive_numbers1(self):
        self._assert("VIII", 8)

    def test_longer_additive_numbers2(self):
        self._assert("MDC", 1600)

    # Additive and Subtractive numbers
    def test_additive_and_subtractive1(self):
        self._assert("XIV", 14)

    def test_additive_and_subtractive2(self):
        self._assert("XLI", 41)

    # If letter not roman number
    def test_not_roman_letter1(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("XVS")

    # Incorrect format: smaller-valued letter before larger-valued letter
    def test_smaller_valued_before1(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("IIMX")

    def test_smaller_valued_before2(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("IVII")

    # Pattern raise warning
    def test_pattern1(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("IVIV")

    def test_pattern2(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("IXIX")

    # not classic roman number system
    def test_pattern3(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("VIIII")

    # Numerals that shouldn't be repeated
    def test_numeral_not_repeated1(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("VV")

    def test_numeral_not_repeated2(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("DD")

    def test_numeral_not_repeated3(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("LL")

    # Any numbers of M allowed
    def test_any_amount_M1(self):
        self._assert("MMMMMI", 5001)

    # specific cases accepted
    def test_specific_case1(self):
        self._assert("CDXC", 490)

    def test_specific_case2(self):
        self._assert("XLIX", 49)

    # specific cases that raise warning
    def test_specific_cases_warning1(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("VIV")

    def test_specific_cases_warning2(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("LLX")

    # input is empty
    def test_input_is_empty(self):
        self._assert("", 0)

    # additional addition and subtraction

    def test_simple_addsub1(self):
        self._assert("XIV", 14)

    def test_simple_addsub2(self):
        self._assert("XLI", 41)

    def test_simple_addsub3(self):
        self._assert("XCIX", 99)

    def test_simple_addsub4(self):
        self._assert("CMIV", 904)

    def test_simple_addsub5(self):
        self._assert("CDXLIV", 444)

    # double-digit is before a higher roman number
    def test_two_number_error1(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("IVCI")

    def test_two_number_error2(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("CMM")

    def test_two_number_error3(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("MCDCM")

    # too many of one
    def test_too_many_of_one_digit1(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("CLLLL")

    def test_too_many_of_one_digit2(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("XIIII")

    def test_too_many_of_one_digit3(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("LXXXX")