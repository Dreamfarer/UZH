#!/usr/bin/env python3
from unittest import TestCase
from public.script import convert_roman_to_int

###############################################################################
# TESTING IN VS CODE
#   First off, you need to navigate your terminal to the current task's folder.
# Copy the following command into the terminal below:
# cd "Informatics I/7 Testing/Task 2 Roman Number Conversion/"
#   To run the unit tests, copy the following line into the terminal below:
# python -m unittest public/tests.py
###############################################################################

###############################################################################
# I went trough "Specification / Orientation for test driven iterations" and
# implemented every mentioned test case, nothing more
###############################################################################
class ConversionTestSuite(TestCase):

    def _assert(self, roman, expected):
        actual = convert_roman_to_int(roman)
        m = f"should be {expected} but was {actual}"
        self.assertEqual(expected, actual, m)

    # Basic roman numerals
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
    
    # These are the only roman numerals written in "subtractive notation"
    def test_simple_subtractive4(self):
        self._assert("IV", 4)
    def test_simple_subtractive40(self):
        self._assert("XL", 40)
    def test_simple_subtractive400(self):
        self._assert("CD", 400)
    def test_simple_subtractive9(self):
        self._assert("IX", 9)
    def test_simple_subtractive90(self):
        self._assert("XC", 90)
    def test_simple_subtractive900(self):
        self._assert("CM", 900)

    # Basic additive numerals
    def test_additiveXI(self):
        self._assert("XI", 11)
    def test_additiveVIII(self):
        self._assert("VIII", 8)
    def test_additiveMDC(self):
        self._assert("MDC", 1600)
    
    # Composite numerals including additive and subtractive
    def test_compositeXIV(self):
        self._assert("XIV", 14)
    def test_compositeXLI(self):
        self._assert("XLI", 41)
    def test_compositeCDXC(self):
        self._assert("CDXC", 490)
    def test_compositeXLIX(self):
        self._assert("XLIX", 49)

    # Speical cases
    def test_m_any_number(self):
        self._assert("MMMMMI", 5001)

    # Invalid numerals that should raise an error
    def test_invalid_numeral(self):
        self.assertRaises(Warning, convert_roman_to_int, "XLS")
    def test_invalid_small_before_large_IIMX(self):
        self.assertRaises(Warning, convert_roman_to_int, "IIMX")
    def test_invalid_small_before_large_LLX (self):
        self.assertRaises(Warning, convert_roman_to_int, "LLX")
    def test_invalid_multiple_IVIV(self):
        self.assertRaises(Warning, convert_roman_to_int, "IVIV")
    def test_invalid_multiple_IXIX(self):
        self.assertRaises(Warning, convert_roman_to_int, "IXIX")
    def test_invalid_multiple_DD(self):
        self.assertRaises(Warning, convert_roman_to_int, "DD")
    def test_invalid_multiple_VVV(self):
        self.assertRaises(Warning, convert_roman_to_int, "VV")
    def test_invalid_multiple_LLL(self):
        self.assertRaises(Warning, convert_roman_to_int, "LL")
    def test_invalid_too_many_multiples(self):
        self.assertRaises(Warning, convert_roman_to_int, "VIIII")

    # Catch cases where there is a subtractive and additive in the same range (e.g. both in range 1 to 10)
    def test_invalid_small_before_large_IVII(self):
        self.assertRaises(Warning, convert_roman_to_int, "IVII")
    def test_invalid_small_before_large_VIV(self):
        self.assertRaises(Warning, convert_roman_to_int, "VIV")