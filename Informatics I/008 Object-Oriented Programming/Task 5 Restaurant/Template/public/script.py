from public.item import Item
from public.order import Order


class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        pass

    def get_restaurant_name(self):
        pass

    def get_menu_list(self):
        pass

    def get_order_list(self):
        pass

    def set_order(self, item_list):
        pass

    def get_revenue(self):
        pass


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
    restaurant.set_order(order_list)
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())
