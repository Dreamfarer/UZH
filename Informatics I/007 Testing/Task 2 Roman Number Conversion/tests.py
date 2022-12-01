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
    def test_simple_numeralI_perytron(self):
        self._assert("I", 1)
    def test_simple_numeralV_perytron(self):
        self._assert("V", 5)
    def test_simple_numeralX_perytron(self):
        self._assert("X", 10)
    def test_simple_numeralL_perytron(self):
        self._assert("L", 50)
    def test_simple_numeralC_perytron(self):
        self._assert("C", 100)
    def test_simple_numeralD_perytron(self):
        self._assert("D", 500)
    def test_simple_numeralM_perytron(self):
        self._assert("M", 1000)
    
    # These are the only roman numerals written in "subtractive notation"
    def test_simple_subtractive4_perytron(self):
        self._assert("IV", 4)
    def test_simple_subtractive40_perytron(self):
        self._assert("XL", 40)
    def test_simple_subtractive400_perytron(self):
        self._assert("CD", 400)
    def test_simple_subtractive9_perytron(self):
        self._assert("IX", 9)
    def test_simple_subtractive90_perytron(self):
        self._assert("XC", 90)
    def test_simple_subtractive900_perytron(self):
        self._assert("CM", 900)

    # Basic additive numerals
    def test_additiveXI_perytron(self):
        self._assert("XI", 11)
    def test_additiveVIII_perytron(self):
        self._assert("VIII", 8)
    def test_additiveMDC_perytron(self):
        self._assert("MDC", 1600)
    
    # Composite numerals including additive and subtractive
    def test_compositeXIV_perytron(self):
        self._assert("XIV", 14)
    def test_compositeXLI_perytron(self):
        self._assert("XLI", 41)
    def test_compositeCDXC_perytron(self):
        self._assert("CDXC", 490)
    def test_compositeXLIX_perytron(self):
        self._assert("XLIX", 49)

    # Speical cases
    def test_m_any_number_perytron(self):
        self._assert("MMMMMI", 5001)

    # Invalid numerals that should raise an error
    def test_invalid_numeral_perytron(self):
        self.assertRaises(Warning, convert_roman_to_int, "XLS")
    def test_invalid_small_before_large_IIMX_perytron(self):
        self.assertRaises(Warning, convert_roman_to_int, "IIMX")
    def test_invalid_small_before_large_LLX_perytron(self):
        self.assertRaises(Warning, convert_roman_to_int, "LLX")
    def test_invalid_multiple_IVIV_perytron(self):
        self.assertRaises(Warning, convert_roman_to_int, "IVIV")
    def test_invalid_multiple_IXIX_perytron(self):
        self.assertRaises(Warning, convert_roman_to_int, "IXIX")
    def test_invalid_multiple_DD_perytron(self):
        self.assertRaises(Warning, convert_roman_to_int, "DD")
    def test_invalid_multiple_VVV_perytron(self):
        self.assertRaises(Warning, convert_roman_to_int, "VV")
    def test_invalid_multiple_LLL_perytron(self):
        self.assertRaises(Warning, convert_roman_to_int, "LL")
    def test_invalid_too_many_multiples_perytron(self):
        self.assertRaises(Warning, convert_roman_to_int, "VIIII")

    # Catch cases where there is a subtractive and additive in the same range (e.g. both in range 1 to 10)
    def test_invalid_small_before_large_IVII_perytron(self):
        self.assertRaises(Warning, convert_roman_to_int, "IVII")
    def test_invalid_small_before_large_VIV_perytron(self):
        self.assertRaises(Warning, convert_roman_to_int, "VIV")


    def test_simple_numeralI_paul(self):
        self._assert("I", 1)

    def test_simple_numeralV_paul(self):
        self._assert("V", 5)

    def test_simple_numeralX_paul(self):
        self._assert("X", 10)

    def test_simple_numeralL_paul(self):
        self._assert("L", 50)

    def test_simple_numeralC_paul(self):
        self._assert("C", 100)

    def test_simple_numeralD_paul(self):
        self._assert("D", 500)

    def test_simple_numeralM_paul(self):
        self._assert("M", 1000)

    def test_simple_additive1_paul(self):
        self._assert("XI", 11)

    def test_simple_additive2_paul(self):
        self._assert("MD", 1500)

    # My implementation
    def test_simple_additive3_paul(self):
        self._assert("XII", 12)

    def test_simple_additive4_paul(self):
        self._assert("LXXX", 80)

    # Subtractions
    def test_simple_subtractive1_paul(self):
        self._assert("IV", 4)

    def test_simple_subtractive2_paul(self):
        self._assert("XL", 40)

    def test_simple_subtractive3_paul(self):
        self._assert("IX", 9)

    def test_simple_subtractive4_paul(self):
        self._assert("XC", 90)

    def test_simple_subtractive5_paul(self):
        self._assert("CM", 900)

    # Long additions
    def test_simple_longadd1_paul(self):
        self._assert("VIII", 8)

    def test_simple_longadd2_paul(self):
        self._assert("XVII", 17)

    def test_simple_longadd3_paul(self):
        self._assert("MDC", 1600)

    def test_simple_longadd4_paul(self):
        self._assert("CLXXVIII", 178)

    def test_simple_longadd5_paul(self):
        self._assert("DLI", 551)

    # Additions and Subtractions
    def test_simple_addsub1_paul(self):
        self._assert("XIV", 14)

    def test_simple_addsub2_paul(self):
        self._assert("XLI", 41)

    def test_simple_addsub3_paul(self):
        self._assert("XCIX", 99)

    def test_simple_addsub4_paul(self):
        self._assert("CMIV", 904)

    def test_simple_addsub5_paul(self):
        self._assert("CDXLIV", 444)

    # lasts cases:
    def test_simple_lastcase1_paul(self):
        self._assert("MMMMMI", 5001)

    def test_simple_lastcase2_paul(self):
        self._assert("CDXC", 490)

    def test_simple_last3_paul(self):
        self._assert("XLIX", 49)

    # Check if warning is thrown for invalid chars
    # Additions and Subtractions
    # def test_simple_invalidchars1_paul(self):
    #     self._assertWarning(Warning, "XLS")

    # def test_simple_invalidchars2_paul(self):
    #     self._assertWarning(Warning, "*jrIX")

    # check for warning when smaller-valued letters before larger-valued ones, like "IIMX", "IVII" etc)
    # def test_simple_smalllarge1_paul(self):
    #     self._assert("XIV",14)

    # def test_simple_smalllarge2_paul(self):
    #     self._assert("XLI",41)

    # def test_simple_smalllarge3_paul(self):
    #     self._assert("XCIX",99)

    # numerals of the pattern "IVIV", "IXIX" raise a warning.
    # def test_simple_pattern1_paul(self):
    #     self._assert("XIV",14)

    # def test_simple_pattern2_paul(self):
    #     self._assert("XLI",41)

    # def test_simple_pattern3_paul(self):
    #     self._assert("XCIX",99)

    # numerals that should not be repeated (e.g. "VV", "DD", "LL") raise a warning.
    # def test_simple_repeated1_paul(self):
    #     self._assert("XIV",14)

    # def test_simple_repeated2_paul(self):
    #     self._assert("XLI",41)

    # def test_simple_repeated3_paul(self):
    #     self._assert("XCIX",99)

    # Check that any number of "M"s are allowed, e.g. "MMMMMI".

    # Check that cases "CDXC" and "XLIX" are accepted,

    # Check that cases "VIV" or LLX are rejected with a Warning.



    def test_simple_numeralI_patertuck(self):
        self._assert("I", 1)

    def test_simple_numeralV_patertuck(self):
        self._assert("V", 5)

    def test_simple_numeralX_patertuck(self):
        self._assert("X", 10)

    def test_simple_numeralL_patertuck(self):
        self._assert("L", 50)

    def test_simple_numeralC_patertuck(self):
        self._assert("C", 100)

    def test_simple_numeralD_patertuck(self):
        self._assert("D", 500)

    def test_simple_numeralM_patertuck(self):
        self._assert("M", 1000)

    # additive Tests
    def test_simple_additive1_patertuck(self):
        self._assert("XI", 11)

    def test_simple_additive2_patertuck(self):
        self._assert("MD", 1500)

    # Subtractive Tests
    def test_simple_subtractive1_patertuck(self):
        self._assert("IV", 4)

    def test_simple_subtractive2_patertuck(self):
        self._assert("XL", 40)

    def test_simple_subtractive3_patertuck(self):
        self._assert("CD", 400)

    def test_simple_subtractive4_patertuck(self):
        self._assert("IX", 9)

    def test_simple_subtractive5_patertuck(self):
        self._assert("XC", 90)

    def test_simple_subtractive6_patertuck(self):
        self._assert("CM", 900)

    # Longer additive numerals
    def test_longer_additive_numbers1_patertuck(self):
        self._assert("VIII", 8)

    def test_longer_additive_numbers2_patertuck(self):
        self._assert("MDC", 1600)

    # Additive and Subtractive numbers
    def test_additive_and_subtractive1_patertuck(self):
        self._assert("XIV", 14)

    def test_additive_and_subtractive2_patertuck(self):
        self._assert("XLI", 41)

    # If letter not roman number
    def test_not_roman_letter1_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("XVS")

    # Incorrect format: smaller-valued letter before larger-valued letter
    def test_smaller_valued_before1_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("IIMX")

    def test_smaller_valued_before2_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("IVII")

    # Pattern raise warning
    def test_pattern1_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("IVIV")

    def test_pattern2_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("IXIX")

    # not classic roman number system
    def test_pattern3_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("VIIII")

    # Numerals that shouldn't be repeated
    def test_numeral_not_repeated1_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("VV")

    def test_numeral_not_repeated2_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("DD")

    def test_numeral_not_repeated3_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("LL")

    # Any numbers of M allowed
    def test_any_amount_M1_patertuck(self):
        self._assert("MMMMMI", 5001)

    # specific cases accepted
    def test_specific_case1_patertuck(self):
        self._assert("CDXC", 490)

    def test_specific_case2_patertuck(self):
        self._assert("XLIX", 49)

    # specific cases that raise warning
    def test_specific_cases_warning1_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("VIV")

    def test_specific_cases_warning2_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("LLX")

    # input is empty
    def test_input_is_empty_patertuck(self):
        self._assert("", 0)

    # additional addition and subtraction

    def test_simple_addsub1_patertuck(self):
        self._assert("XIV", 14)

    def test_simple_addsub2_patertuck(self):
        self._assert("XLI", 41)

    def test_simple_addsub3_patertuck(self):
        self._assert("XCIX", 99)

    def test_simple_addsub4_patertuck(self):
        self._assert("CMIV", 904)

    def test_simple_addsub5_patertuck(self):
        self._assert("CDXLIV", 444)

    # double-digit is before a higher roman number
    def test_two_number_error1_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("IVCI")

    def test_two_number_error2_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("CMM")

    def test_two_number_error3_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("MCDCM")

    # too many of one
    def test_too_many_of_one_digit1_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("CLLLL")

    def test_too_many_of_one_digit2_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("XIIII")

    def test_too_many_of_one_digit3_patertuck(self):
        with self.assertRaises(Warning, msg="Invalid Input"):
            convert_roman_to_int("LXXXX")
