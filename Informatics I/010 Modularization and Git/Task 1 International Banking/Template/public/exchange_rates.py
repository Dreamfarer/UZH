#!/usr/bin/env python3
# IMPORTANT: Do not change this file!

# List of exchange rates that follows two simple rules:
# - all valid currencies exist as keys on the first level
# - only one CURRENCY-CURRENCY combination is added (e.g., CAD-USD),
#   the inverse is omitted to avoid redundant information
EXCHANGE_RATES = {
    "CAD": {
        "USD": 0.753,
        "JPY": 82.463,
        "EUR": 0.684,
        "GBP": 0.583
    },
    "CHF" : {
        "USD": 1.001,
        "GBP": 0.776,
        "CAD": 1.330
    },
    "EUR": {
        "CHF": 1.100,
        "GBP": 0.853
    },
    "USD": {
        "EUR": 0.908,
        "GBP": 0.774,
        "JPY": 109.510
    },
    "GBP": {},
    "JPY": {
        "GBP": 0.707,
        "EUR": 0.829,
        "CHF": 0.912
    }
}

# ensure no entry is missing
for f in EXCHANGE_RATES.keys():
    for t in EXCHANGE_RATES.keys():
        a = t in EXCHANGE_RATES[f].keys()
        b = f in EXCHANGE_RATES[t].keys()
        if not (a or b) and f < t:
            print("missing rate: {} » {}".format(f, t))

# ensure that no duplication exists
for f in EXCHANGE_RATES.keys():
    for t in EXCHANGE_RATES[f].keys():
        if t in EXCHANGE_RATES.keys():
            if f in EXCHANGE_RATES[t].keys():
                if f > t: # only print once
                    print("Remove redundancy: {} » {}".format(f, t))
