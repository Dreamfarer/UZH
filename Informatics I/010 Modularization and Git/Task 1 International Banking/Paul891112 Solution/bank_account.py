#!/usr/bin/env python3
# add imports, if necessary

#before uploading to ACCESS, remember to add public.
from currency_converter import convert
from exchange_rates import EXCHANGE_RATES

class BankAccount:

    def __init__(self, currency="CHF"):
        self.__ALL_CURRENCY = EXCHANGE_RATES.keys()
        if not (currency in self.__ALL_CURRENCY):
            raise Warning("Constructing with invalid currency")
        self.__currency = currency
        self.__balance = 0

    def get_currency(self):
        return self.__currency

    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount, currency="CHF"):
        if not(isinstance(amount,int) or isinstance(amount,float)):
            raise Warning("Invalid input type to withdraw")
        if not(isinstance(currency,str)):
            raise Warning("Currency not a string")
        if not (currency in self.__ALL_CURRENCY):
            raise Warning("Deposits invalid currency")
        if amount <=0:
            raise Warning("Invalid amount to withdraw")
        if self.__currency == currency:
            self.__balance += amount
        else:
            self.__balance += convert(amount,currency,self.__currency)
        
    
    def withdraw(self, amount, currency="CHF"):
        if not(isinstance(amount,int) or isinstance(amount,float)):
            raise Warning("Invalid input type to withdraw")
        if not(isinstance(currency,str)):
            raise Warning("Currency not a string")
        if amount <=0:
            raise Warning("Invalid amount to withdraw")
        if not (currency in self.__ALL_CURRENCY):
            raise Warning("Withdraws invalid currency")
        
        if currency == self.__currency:
            if self.__balance<amount:
                raise Warning("Withdraw more than balance")
            else:
                self.__balance -= amount
        else:        
            converted = convert(amount,currency,self.__currency)
            if self.__balance<converted:
                raise Warning("Withdraw more than balance")
            else:
                self.__balance -= converted
        
        
        
