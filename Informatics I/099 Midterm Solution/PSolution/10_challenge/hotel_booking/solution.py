#!/usr/bin/env

milton_hotel = {
    "standard":  120.00,
    "executive": 160.00,
    "suite":     320.00,
    "breakfast": 25.00,
    "parking":   30.00,
}

def booking(pricing, products):
    total = 0
    for product in products:
        total += pricing[product]
    executives = products.count("executive")
    suites = products.count("suite")
    rooms = executives + suites + products.count("standard")
    parkings = products.count("parking")
    breakfasts = products.count("breakfast")
    room_types = ["standard", "executive", "suite"]
    room_discount = 0
    if rooms > 2:
        for product in products:
            if product in room_types:
                room_discount += 0.1 * pricing[product]
    free_breakfasts = min(breakfasts, suites)
    free_parkings = min(parkings, suites + executives)
    discount = (
      free_breakfasts * pricing["breakfast"] +
      free_parkings * pricing["parking"] +
      room_discount)
    return total, discount, total - discount

# examples
print( booking(milton_hotel, [ # no discounts
    "executive", "breakfast"
]))
print( booking(milton_hotel, [ # one free parking
    "standard", "executive", "breakfast", "breakfast", "parking"
]))
print( booking(milton_hotel, [ # two free parking (one applied) and one free breakfast plus 10% off all rooms
    "standard", "executive", "suite", "parking",
    "breakfast", "breakfast", "breakfast"
]))

