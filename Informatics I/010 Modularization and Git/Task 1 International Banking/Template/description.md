In this task, you will build a collection of utils that can be used for international bank accounts. By splitting all functionalities into different files, it is possible for others to reuse parts of your solution. Make sure that you add the required `import` statements to all files.

You are supposed to implement the `BankAccount` class that has a specific currency. It can be checked for the currency (`get_currency`) and for its current balance (`get_balance`). It is possible to `deposit` money and to `withdraw` money from the account. Both methods use CHF by default, but they can be used with foreign currencies.

To handle foreign currencies properly, a utility function `convert` should be used for the conversion. The function takes an amount of money and converts it from the source currency to the target currency. Implement `convert` in the `currency_converter.py` file and import it in your `BankAccount`.

The file `exchange_rates.py` contains several exchange rates in the `EXCHANGE_RATES` dictionary.  Accessing `EXCHANGE_RATES["USD"]["EUR"]` would give you the current exchange rate for converting USD into EUR. You can assume that all supported currencies are used as a key in the dictionary, but -to avoid redundant information- the exchange rate is only stored in one direction (e.g., USD»EUR) and the other direction is omitted (i.e, EUR»USD), because it can be derived. This file must not be changed. Assume that in a real setting, it would be frequently updated with the current rates.

Your implementation also has to handle error cases. `BankAccounts` can only opened with a currency for which exchange rates are available. `deposit` and `withdraw` should only accept positive values and existing currencies. The converter should detect invalid amounts (i.e., not a number), invalid currencies (e.g., empty string), and unsupported currencies (i.e., no exchange rate available). A `BankAccount` should also never have a negative balance. Raise a `Warning` in all of these cases.

**Note:** You must not change the contents of `EXCHANGE_RATES`.

**Note:** All state of `BankAccount` must be contained within the class. Do not store information in global variables or in class variables. It must be possible to instantiate classes multiple times without suffering from side effects.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.

**Note:** You can freely extend the public test suite, which is not relevant for the grading. We strongly encourage you to add more tests!
