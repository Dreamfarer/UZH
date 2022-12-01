#!/usr/bin/env python3

price_cone = 0.70
price_per_scoop_vanilla = 1.00
price_per_scoop_chocolate = 1.10

num_scoops_vanilla = 1
num_scoops_chocolate = 3

# Change the function below to calculate the total price this
# order. Note that your implementation should work with any
# specific value, so you can't just add up the raw numbers,
# you MUST use the VARIABLES defined above. Do not forget the
# cone!
def get_price():
    # You need to change the following line
    price = price_cone + price_per_scoop_chocolate * num_scoops_chocolate + price_per_scoop_vanilla * num_scoops_vanilla

    # You don't need to change the following line
    return price