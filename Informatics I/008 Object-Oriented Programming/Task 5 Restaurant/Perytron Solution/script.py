# Provide this to ACCESS
from public.item import Item
from public.order import Order

# Use this in your IDE:
# from item import Item
# from order import Order

class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__name = restaurant_name
        self.__menu = menu_list
        self.__oders = []

    # Return a string carrying the name of the restaurant instance
    def get_restaurant_name(self):
        return self.__name

    # Return the menu (ie. the list of 'Item' objects) of the restaurant instance
    def get_menu_list(self):
        return self.__menu.copy()
    
    # Return the list of orders placed at the restaurant instance
    # Return "No order yet" if no orders have been placed in the restaurant instance yet
    def get_order_list(self):

        # Check wheather the order list is empty
        if not len(self.__oders) == 0: return self.__oders.copy()
        return "No order yet" 
    
    # Create an 'Order' object with the provided list of 'Item' objects and should update the order list of the restaurant instance. 
    # Only items that can be found in the restaurant menu can be added to an order. 
    # Other items provided by the customer should be discard by the function.
    def set_order(self, item_list):

        # Filter all unallowed items in the order
        filtered_order = []
        for item in item_list: filtered_order.append(item) if item in self.__menu else True

        # Make sure no 'Order' object is created when the list is empty
        if not filtered_order: return

        # Create an 'Order' object
        self.__oders.append(Order(filtered_order))

    # Return the revenue of the restaurant instance. 
    # It is the sum of all order bills placed in the restaurant. 
    # If no order has been placed yet, the function should return 0
    def get_revenue(self):
        
        # Loop over every order and call the 'Order' specific function 'get_bill_amount'
        revenue = 0
        for order in self.__oders: revenue += order.get_bill_amount()
        return revenue

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    # Create Item Objects with Name and Price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    # Create menu list
    menu_list = [steak, fish]
    # Create order list
    order_list = [salad]
    # Create restaurant object with name and menu list
    restaurant = Restaurant("Zurich_1", menu_list)
    # Create an order with the order list
    restaurant.set_order(order_list)
    # print(restaurant.get_order_list())
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())