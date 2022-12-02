#!/usr/bin/env python3
from public.currency_converter import convert
from public.exchange_rates import EXCHANGE_RATES

class BankAccount:

    def __init__(self, currency: str="CHF"):
        self.__currency = self.__check_valid_currency(currency)
        self.__balance = 0

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount, currency="CHF"):
        self.__balance =  self.__check_zero(self.__balance + convert(amount, self.__check_valid_currency(currency), self.__currency))
    
    def withdraw(self, amount, currency="CHF"):
        self.__balance =  self.__check_zero(self.__balance - convert(amount, self.__check_valid_currency(currency), self.__currency))
    
    def __check_zero(self, amount):
        if amount < 0: raise Warning("Sigh... You clearly won't pass Mikro.")
        return amount

    def __check_valid_currency(self, currency):
        if currency in EXCHANGE_RATES.keys(): return currency
        if currency in EXCHANGE_RATES.values(): return currency
        raise Warning("LMAO, you can't (...) spell!")