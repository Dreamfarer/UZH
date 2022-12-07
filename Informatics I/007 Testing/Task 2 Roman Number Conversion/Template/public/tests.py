#!/usr/bin/env python3
from unittest import TestCase
from public.script import convert_roman_to_int


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

    def test_numeralI(self):
        self._assert("I", 1)

    def test_numeralV(self):
        self._assert("V", 5)

    def test_numeralX(self):
        self._assert("X", 10)

    def test_numeralL(self):
        self._assert("L", 50)

    def test_numeralC(self):
        self._assert("C", 100)

    def test_numeralD(self):
        self._assert("D", 500)

    def test_numeralM(self):
        self._assert("M", 1000)

    def test_additive1(self):
        self._assert("XI", 11)

    def test_additive2(self):
        self._assert("MD", 1500)

    def test_subtractive1(self):
        self._assert("IV", 4)

    def test_subtractive2(self):
        self._assert("XL", 40)

    def test_subtractive3(self):
        self._assert("CD", 400)

    def test_subtractive4(self):
        self._assert("IX", 9)

    def test_subtractive5(self):
        self._assert("XC", 90)

    def test_subtractive6(self):
        self._assert("CM", 900)

    def test_longer1(self):
        self._assert("VIII", 8)

    def test_longer2(self):
        self._assert("MDC", 1600)

    def test_addsub1(self):
        self._assert("XIV", 14)

    def test_addsub2(self):
        self._assert("XLI", 41)

    def test_invalid_type(self):
        with self.assertRaises(Warning):
            convert_roman_to_int(3)

    def test_invalid_empty(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("")

    def test_invalid_numerals1(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("XLS")

    def test_invalid_numerals2(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("ABK")

    def test_invalid_small_before_large1(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("IIMX")

    def test_invalid_small_before_large2(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("IVII")

    def test_invalid_pattern1(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("IVIV")

    def test_invalid_pattern2(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("IXIX")

    def test_invalid_system(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("VIIII")

    def test_invalid_repeated1(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("VV")

    def test_invalid_repeated2(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("DD")

    def test_invalid_repeated3(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("LL")

    def test_any_m(self):
        self._assert("MMMMMI", 5001)

    def test_special1(self):
        self._assert("CDXC", 490)

    def test_special2(self):
        self._assert("XLIX", 49)

    def test_invalid_special1(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("VIV")

    def test_invalid_special2(self):
        with self.assertRaises(Warning):
            convert_roman_to_int("LLX")
