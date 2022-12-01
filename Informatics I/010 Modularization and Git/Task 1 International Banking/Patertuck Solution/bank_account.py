#!/usr/bin/env python3
# add imports, if necessary
from currency_converter import convert
from exchange_rates import EXCHANGE_RATES


class BankAccount:

    def __init__(self, currency: str = "CHF"):
        self.__currency = currency
        self.__balance = 0

        if type(currency) != str or currency not in EXCHANGE_RATES:
            raise Warning("Invalid Input currency for BankAccount")

    def get_currency(self) -> str:
        x = self.__currency
        return x

    def get_balance(self) -> float:
        x = self.__balance
        return x

    def deposit(self, amount=float, currency: str = "CHF") -> None:
        BankAccount.input_test(amount, currency)

        self.__balance += convert(amount, currency, self.__currency)

    def withdraw(self, amount=float, currency: str = "CHF"):
        BankAccount.input_test(amount, currency)

        self.__balance -= convert(amount, currency, self.__currency)

        if self.__balance < 0:
            raise Warning("There is not enough funds to withdraw")

    def input_test(amount: float, currency: str) -> None:
        if type(amount) != float or amount < 0 or type(currency) != str or\
                currency not in EXCHANGE_RATES or currency == "":
            raise Warning("Invalid Input")

