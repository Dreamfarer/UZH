#!/usr/bin/env python3

from typing import Union
from currency_converter import convert, validate_amount

class BankAccount:

    def __init__(self, currency: str = "CHF"):
        convert(1, currency, "CHF")
        self.__currency: str = currency
        self.__balance: float = 0

    def get_currency(self) -> str:
        return self.__currency

    def get_balance(self) -> float:
        return self.__balance
        
    def deposit(self, amount: Union[int, float], currency: str = "CHF") -> None:
        self.__balance += convert(amount, currency, self.__currency)
    
    def withdraw(self, amount: Union[int, float], currency: str = "CHF") -> None:
        convert_amount: float = convert(amount, currency, self.__currency)
        validate_amount((self.__balance - convert_amount,))
        self.__balance -= convert_amount

