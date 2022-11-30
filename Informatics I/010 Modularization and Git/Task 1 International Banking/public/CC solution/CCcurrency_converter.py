#!/usr/bin/env python3

from typing import Union
from exchange_rates import EXCHANGE_RATES

def convert(amount: Union[int, float], from_currency: str, to_currency: str) -> float:
    validate_amount((amount,))
    validate_currency((from_currency, to_currency))
    if from_currency == to_currency:
        return amount
    elif to_currency in EXCHANGE_RATES[from_currency].keys():
        return amount * EXCHANGE_RATES[from_currency][to_currency]
    elif from_currency in EXCHANGE_RATES[to_currency].keys():
        return amount * (1 / EXCHANGE_RATES[to_currency][from_currency])
    raise Warning("invalid input")

def validate_amount(testees: tuple) -> None:
    if not all((type(testee) == int or type(testee) == float) and testee >= 0 for testee in testees):
        raise Warning("invalid input")

def validate_currency(testees: tuple) -> None:
    if not all(type(testee) == str and testee in EXCHANGE_RATES.keys() for testee in testees):
        raise Warning("invalid input")