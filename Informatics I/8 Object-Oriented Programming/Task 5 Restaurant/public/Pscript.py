from item import Item
from order import Order


class Restaurant:

    def __init__(self, restaurant_name, menu_list):
        self.__name = restaurant_name
        self.__menulist = menu_list #list of Items
        self.__orderlist = list()

    def get_restaurant_name(self):
        return self.__name

    def get_menu_list(self):
        copy = []
        for i in self.__menulist:
            copy.append(i)
        return copy
        

    def get_order_list(self):
        if self.__orderlist == list():
            return "No order yet"
        copy = []
        for i in self.__orderlist:
            copy.append(i)
        return copy

    def set_order(self, item_list):
        valid_items = list()
        for i in item_list:
            for j in self.__menulist:
                if i==j:
                    valid_items.append(i) #append what is ordered and in menu
        if valid_items == []:
            return            
        order = Order(valid_items)
        self.__orderlist.append(order)
        return #returns None
                    

    def get_revenue(self):
        revenue=0
        if self.__orderlist==[]:
            return revenue
        for i in self.__orderlist:
            revenue += i.get_bill_amount()
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
    menu_list = [steak, salad, fish]
    # Create order list
    order_list = []
    # Create restaurant object with name and menu list
    restaurant = Restaurant("Zurich_1", menu_list)
    # Create an order with the order list
    restaurant.set_order(order_list)
    print(restaurant.get_order_list())
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())

