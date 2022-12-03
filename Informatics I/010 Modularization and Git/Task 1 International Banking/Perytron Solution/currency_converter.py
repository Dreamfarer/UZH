from typing import Union
from exchange_rates import EXCHANGE_RATES

def convert(amount: Union[int, float], from_currency: str, to_currency: str) -> float:

    # Check that correct type is provided
    if False in [isinstance(from_currency, str), isinstance(to_currency, str), (isinstance(amount, float) or isinstance(amount, int))]: raise Warning("You had one (...) job. Provide the right type you (...) (...)!")

    # Check that the amount is greater than 0
    if amount <= 0: raise Warning("Sigh... You clearly won't pass Mikro.")

    # If exchange rate exists without calculating it
    try: EXCHANGE_RATES[from_currency][to_currency]
    except: pass
    else: return amount * EXCHANGE_RATES[from_currency][to_currency]

    # Try calculating the exchange rate from_currency * exchange_rate = to_currency
    try: 
        exchange_rate = 1 / EXCHANGE_RATES[to_currency][from_currency]
    except: pass
    else: return amount * exchange_rate

    # Return if both currencies are the same, no converting required
    if from_currency == to_currency: return amount

    raise Warning("Exchange rates do not exist") # Raise warning if nothing of the above matched


    
