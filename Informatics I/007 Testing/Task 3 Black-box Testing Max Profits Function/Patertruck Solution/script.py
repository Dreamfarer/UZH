#!/usr/bin/env python3

# You can implement this function, but you do not have to.
# The grading will only depend on your test suite.
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def max_profit(prices):
	best_sell = 0

	# check for valid input type list
	if type(prices) != list:
		return "Invalid Input Type"

	# check for empty list
	if not prices:
		return "Empty Price List"

	smallest_price = prices[0]
	for price in prices:
		# checks for the individual elements in the list to be an integer
		if type(price) != int:
			return "Invalid Data Type within List"

		if price < 0:
			return "Invalid Prices"

		if price < smallest_price:
			smallest_price = price
			continue

		if price - smallest_price > best_sell:
			best_sell = price - smallest_price

	return best_sell




print(max_profit([4, 10, 3, 20, 3]))
