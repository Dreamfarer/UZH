#!/usr/bin/env python3
from unittest import TestCase
from currency_converter import convert
from bank_account import BankAccount


class PrivateFunctionalTestSuite(TestCase):

    def test_invalid_input_bank_account1(self):
        with self.assertRaises(Warning):
            BankAccount("EURO")

    def test_invalid_input_bank_account2(self):
        with self.assertRaises(Warning):
            BankAccount(2)

    def test_invalid_input_currency_converter1(self):
        with self.assertRaises(Warning):
            convert("4", "CHF", "EUR")

    def test_invalid_input_currency_converter2(self):
        with self.assertRaises(Warning):
            convert(-3.0, "CHF", "EUR")

    def test_invalid_input_currency_converter3(self):
        with self.assertRaises(Warning):
            convert(3.0, 3, "EUR")

    def test_invalid_input_currency_converter4(self):
        with self.assertRaises(Warning):
            convert(3.0, "CHF", 4.3)

    def test_invalid_input_currency_converter5(self):
        with self.assertRaises(Warning):
            convert(3.0, "CHR", "EUR")

    def test_invalid_input_currency_converter6(self):
        with self.assertRaises(Warning):
            convert(3.0, "CHF", "EURO")

    def test_invalid_input_deposit1(self):
        with self.assertRaises(Warning):
            BankAccount.deposit("30", "EUR")

    def test_invalid_input_deposit2(self):
        with self.assertRaises(Warning):
            BankAccount.deposit(30, "EURO")

    def test_invalid_input_deposit3(self):
        with self.assertRaises(Warning):
            BankAccount.deposit(-30, "EURO")


    def test_0_convert1(self):
        actual = convert(1.0, "EUR", "CHF")
        expected = 1.10
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    def test_0_convert2(self):
        actual = convert(1.10, "CHF", "EUR")
        expected = 1.0
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    def test_0_convert3(self):
        actual = convert(1.0, "EUR", "EUR")
        expected = 1.0
        self.assertEqual(expected, actual)

    def test_deposit1(self):
        x = BankAccount("EUR")
        x.deposit(100.0, "CHF")
        actual = x.get_balance()
        expected = 90.909
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    def test_deposit2(self):
        x = BankAccount("EUR")
        x.deposit(100.0, "EUR")
        actual = x.get_balance()
        expected = 100
        self.assertEqual(expected, actual)

    def test_deposit3(self):
        x = BankAccount("CHF")
        x.deposit(100.0, "EUR")
        actual = x.get_balance()
        expected = 110.0
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    def test_withdraw1(self):
        x = BankAccount("CHF")
        x.deposit(100.0, "CHF")
        x.withdraw(100.0, "CAD")
        actual = x.get_balance()
        expected = 24.81203
        self.assertAlmostEqual(expected, actual, delta=0.0001)

    def test_withdraw2(self):
        with self.assertRaises(Warning):
            x = BankAccount("CHF")
            x.deposit(100.0, "CHF")
            x.withdraw(100.0, "EUR")

    # def test_1_basic_banking(self):
    #     sut = BankAccount("CHF")
    #     sut.deposit(100.0, "CHF")
    #     sut.withdraw(10.0, "EUR")
    #     actual = sut.get_balance()
    #     expected = 89.0
    #     self.assertAlmostEqual(expected, actual, delta=0.0001)

    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
