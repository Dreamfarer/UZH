class Item:
    # Set Item ID, Type and Name in initialization
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # Return Item Name
    def get_item_name(self):
        return self.__name

    # Return Item Price
    def get_item_price(self):
        return self.__price

    def __repr__(self):
        return self.__name
