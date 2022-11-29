Imagine you own a restaurant. Your business starts to grow after a while and you want to open new branches. You need to develop a software system that will allow these branches to be managed from a single place. You decide to make a software for this and make a model in which you can see your new branches, make additions, see the orders and total revenue in the branches.

Your task is to use the required Object-Oriented principles for the above-mentioned purposes and implement the system.

There are 3 classes in this task: `Restaurant` ,`Order` and `Item`. You only have to implement the `Restaurant` class. The `Order` and `Item` classes are provided.

## Classes
- **Restaurant**

    The restaurant class is used to instantiate a restaurant object. A restaurant object holds its own name, menu and places orders. Functionally, it returns the total revenue of its orders and other attributes it holds, if requested. You can find the details of the requested functions below.

    The restaurant object takes two parameters: `name` and `menu_list` .
    * `name` is a string carrying the name of the restaurant
    * `menu_list` a list of `Item` objects that are available in the restaurant

    ```Python
        # A restaurant instance with name Zurich_1 and 1 item menu list of Hamburger at 20 CHF.
        Restaurant("Zurich_1", [Item("Hamburger", 20)])
    ```

    Functions:
    * `get_restaurant_name` function should return a string carrying the name of the restaurant instance
    * `get_menu_list` function should return the menu (ie. the list of `Item` objects) of the restaurant instance
    * `get_order_list` function should return the string `No order yet` if no orders have been placed in the restaurant instance yet. Otherwise it should return the list of orders placed at the restaurant instance.
    * `set_order` function should create an `Order` object with the provided list of `Item` objects and should update the order list of the restaurant instance. Only items that can be found in the restaurant menu can be added to an order. Other items provided by the customer should be discard by the function.
    * `get_revenue` function should return the revenue of the restaurant instance. It is the sum of all order bills placed in the restaurant. If no order has been placed yet, the function should return 0.

- **Order**

    Orders are represented by instances of the `Order` class, constructor of which accepts an `item_list` as an argument. `item_list` is a list containing the objects instantiated from the `Item` class. The Order object holds the total price of the given order and the list of products in the order. The function `get_bill_amount` returns the bill amount of that particular order instance. `__repr__` function is used to represent the object as string.

- **Item**

    Products are instantiated from the `Item` class with 2 parameters : `name` and `price`. The `name` attribute is a string holding the name of the product, and `price` attribute holds the price of the product. The object has functions to return it's attributes.

## Example
```Python
        hamburger = Item("Hamburger", 20)
        pizza = Item("Pizza", 35)
        steak = Item("Steak", 50)
        menu_list = [hamburger, pizza]
        restaurant_name = "Zurich_1"
        restaurant = Restaurant(restaurant_name,  menu_list)
        order_list = [pizza, pizza, hamburger, steak]
        restaurant.set_order(order_list)
        restaurant.get_revenue() # ==> Returns 90
```

Note: All state must be contained within the class. Do not store information in global variables or in class variables. It has to be possible to use multiple instances of the classes in parallel without suffering from side effects.

Note: The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.

Note: We strongly encourage you to add more tests to the public test suite.

Note: You shouldn't be concerned with the `Order` and `Item` classes. When necessary, just use the objects from these classes in your implementation of the `Restaurant` class.