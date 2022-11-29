from public.item import Item
from public.order import Order


class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__restaurant_name = restaurant_name
        self.__menu_list = menu_list
        self.__Order = list()

    def get_restaurant_name(self):
        return self.__restaurant_name

    def get_menu_list(self):
        copy = list()
        for item in self.__menu_list:
            copy.append(item)
        return copy

    def get_order_list(self):
        if not self.__Order:
            return "No order yet"
        return self.__Order

    def set_order(self, item_list):
        valid_items = list()
        for item in item_list:
            if item in self.__menu_list:
                valid_items.append(item)

        # doesn't add an empty order if the list ov valid items is empty
        if not valid_items:
            return

        order = Order(valid_items)
        self.__Order.append(order)

    def get_revenue(self):
        x = int()
        for item in self.__Order:
            x += item.get_bill_amount()
        return x


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    # Create Item Objects with Name and Price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    # Create menu list
    menu_list = [steak, salad, fish]

    # Create order list
    order_list = [steak, steak, salad, pizza]
    # Create restaurant object with name and menu list
    restaurant = Restaurant("Zurich_1", menu_list)
    # Create an order with the order list
    print(restaurant.get_order_list())
    restaurant.set_order(order_list)
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())
