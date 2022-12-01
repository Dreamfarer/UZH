#!/usr/bin/env python3
# add imports, if necessary

#Before uploading to ACCESS, remember to add public.
from exchange_rates import EXCHANGE_RATES

def convert(amount, from_currency, to_currency):
    if isinstance(amount,int) or isinstance(amount,float):
        if not (isinstance(from_currency,str) and isinstance(to_currency,str)):
            raise Warning("Invalid currency type")
        if from_currency == "" or to_currency == "":
            raise Warning("Empty currency")
        
        all_currency = EXCHANGE_RATES.keys()
        
        if from_currency in all_currency and to_currency in all_currency:
            #try to change from from to to
            try: 
                converted = amount * EXCHANGE_RATES[from_currency][to_currency]
                return converted
            except:
                #try form to to from
                try:
                    converted = amount / EXCHANGE_RATES[to_currency][from_currency]            
                    return converted
                except:
                    raise Warning("Shouldn't happen, but one currency is invalid")
        else:
            raise Warning("Invalid currency to convert")
        
        
        
    else:
        raise Warning("convert currency amount NaN or negative number ")
