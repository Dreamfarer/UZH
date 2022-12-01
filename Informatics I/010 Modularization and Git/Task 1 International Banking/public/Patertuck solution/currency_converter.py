#!/usr/bin/env python3
# add imports, if necessary
from exchange_rates import EXCHANGE_RATES


def convert(amount=float, from_currency=str, to_currency=str) -> float:

    # raising Warnings for wrong input types
    if type(amount) != float or amount < 0:
        raise Warning("Amount needs to be a number and positive")

    if type(from_currency) != str != type(to_currency) or from_currency == "" or from_currency == "":
        raise Warning("Input currency needs to be a string that is not empty")


    # check if the currency exchange is in the list from from_currency to to_currency
    if from_currency in EXCHANGE_RATES:

        # if the currencies are the same
        if from_currency == to_currency:
            return amount

        if to_currency in EXCHANGE_RATES[from_currency]:
            return amount * EXCHANGE_RATES[from_currency][to_currency]

    # check if the currency exchange is in the list from to_currency to from_currency
    if to_currency in EXCHANGE_RATES:
        if from_currency in EXCHANGE_RATES[to_currency]:

            return amount / EXCHANGE_RATES[to_currency][from_currency]

    raise Warning("Invalid input for currency")
