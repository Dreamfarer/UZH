from typing import Union
from public.currency_converter import convert
from public.exchange_rates import EXCHANGE_RATES

class BankAccount:

    def __init__(self, currency: str="CHF"):
        self.__currency = self.__check_valid_currency(currency) # Check that currency exists
        self.__balance = 0

    def get_currency(self) -> str:
        return self.__currency

    def get_balance(self) -> Union[int, float]:
        return self.__balance
        
    def deposit(self, amount: Union[int, float], currency="CHF") -> None:
        # Add to the balance only if balance is positive afterwards and check that the amount and currency are actually provided in an allowed format.
        self.__balance =  self.__check_zero(self.__balance + convert(amount, self.__check_valid_currency(currency), self.__currency))
    
    def withdraw(self, amount: Union[int, float], currency="CHF") -> None:
        # Subtract from the balance only if balance is positive afterwards and check that the amount and currency are actually provided in an allowed format.
        self.__balance =  self.__check_zero(self.__balance - convert(amount, self.__check_valid_currency(currency), self.__currency))
    
    # Private function to check whether the amount is creater than 0
    def __check_zero(self, amount: Union[int, float]) -> Union[int, float]:
        if amount < 0: raise Warning("Sigh... You clearly won't pass Mikro.")
        return amount

    # Check if the provided currency is valid by checking if the EXCHANGE_RATES-dictionary contains it.
    def __check_valid_currency(self, currency: str) -> str:
        if currency in EXCHANGE_RATES.keys(): return currency
        if currency in EXCHANGE_RATES.values(): return currency
        raise Warning("LMAO, you can't (...) spell!")