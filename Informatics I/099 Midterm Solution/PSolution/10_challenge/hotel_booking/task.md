You have been tasked with programming a billing system for hotels. A hotel offers a variety of products (rooms and additional services), for which the prices are stored in a dictionary. A hotel booking can comprise an arbitrary positive number of products.

Implement a function `booking` according to these implementation instructions:

 * `booking` takes two parameters: the first is a dictionary containing the prices as shown in the example `milton_hotel`; the second is a list of products booked.
 * Depending on which products are booked together, various discounts are applied:
     * For each executive room, one parking space is offered for free
     * For each suite room, one parking space and one breakfast are offered for free
     * If at least 3 rooms of any type are booked, all room prices are reduced by 10%
 * The function should return three values: the total price of the booking before any discounts, the total discount, and the total price after subtracting the discount.
 * Of course, your function should work with arbitrary prices as specified in the dictionary, but you can assume that the keys given in the example will always be present in the dictionary.
 * Note that discounts are only applied if the free product has actually been booked. For example, if an executive room is booked without a parking space, then there is no discount on that booking.

**Note**: Do *not* lookup prices in `milton_hotel`! You need to look them up in the function paramter `pricing`!

**Note**: Make sure you return the correct number of return values. Partial points are awarded even if not all return values are correct, but only if all three values are present.

You may assume that your function will only be called with parameters that match the given description.
