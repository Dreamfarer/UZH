#!/usr/bin/env python3

class Fridge:
    
    def __init__(self):
        self.__items = []
        self.__product_index = -1 # Start with -1 because in the first loop we will increment it to 0 before accessing

    # Add a product to fridge and sort it according to the earliest eat-by date
    def store(self, product):
        self.__items.append(product)
        self.__items.sort()

    # Remove given product from the fridge and return its name
    def take(self, product):
        try: 
            self.__items.remove(product)
            return product
        except: raise Warning("No such item in the fridge")

    # Remove products that are too old and return their names in a list
    def take_before(self, date):
        output_list = []
        # Identify items that are too old and need to be removed
        for product in self.__items:
            if product[0] < date: output_list.append(product)
        # Remove the before flagged products
        for to_remove_items in output_list: 
            self.__items.remove(to_remove_items)
        return output_list
    
    # Searches through the products currently in the fridge trying to find the earliest eat-by date product with given name
    def find(self, name):
        for product in self.__items: 
            if product[1] == name: return product
        return None

    # Return iterator
    def __iter__(self):
        return self

    # Return next product currently in fridge
    def __next__(self):
        self.__product_index += 1
        try: return self.__items[self.__product_index]
        except: raise StopIteration

    # Return how many items are still in the fridge
    def __len__(self):
        return len(self.__items)

# f = Fridge()
# f.store((191127, "Butter"))
# f.store((191117, "Milk"))

# print("Items in the fridge:")
# for i in f: print("- {} ({})".format(i[1], i[0]))

# f.take((191127, "Butter")) # ok
# f.take((191207, "Bread")) # fails

# print(f.take_before(191120))
# print(len(f))