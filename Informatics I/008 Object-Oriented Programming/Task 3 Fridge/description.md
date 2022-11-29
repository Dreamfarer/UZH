In this task, you will implement a fridge that can store grocery items. A grocery item has a name, e.g., "Butter", and a eat-by date, e.g., Nov 27, 2019. In this task, such an item will be represented as a tuple, e.g., (191127, "Butter"). This simple encoding has the useful property: the tuple is already sortable, e.g., (12345, "asd") > (01234, "asd") is True, and that all properties like immutability, hashability, or equality are already provided by default.

It is very straightforward to put items into the fridge. One can put an unlimited amount of items into the fridge, it should also be possible to put the same item multiple times (e.g., two pieces of butter with the same eat-by date).

     f = Fridge()
     f.store((191127, "Butter"))
     f.store((191117, "Milk"))

To provide access to the contents, make the fridge [iterable](https://docs.python.org/3.5/glossary.html#term-iterable), i.e., implement the [\__iter__](https://docs.python.org/3.5/reference/datamodel.html#object.__iter__) method that returns an [iterator](https://docs.python.org/3.5/glossary.html#term-iterator) object with a meaningful implementation for [\__next__](https://docs.python.org/3.5/library/stdtypes.html#iterator.__next__). The iterator should iterate over the contents ordered by eat-by date (things that go bad soon should be listed first). Also implement a [\__len__](https://docs.python.org/3.5/reference/datamodel.html#object.__len__) function, to make it easy to check how many items are in the fridge, right now.

With this simple abstraction, it is possible to use the fridge, for example.

     print("Items in the fridge:")
     for i in f:
         print("- {} ({})".format(i[1], i[0]))

Items can be `take`n out of the fridge by providing their names and eat-by dates. Such an invocation should *remove and return* the first matching item in the fridge. A `Warning` should be raised if no matching item can be found.

    f.take((191127, "Butter")) # ok
    f.take((191207, "Bread")) # fails

The fridge should provide two utility functions. The first function `find` takes a `name` and searches for the item tuple with the same name and the *earliest* eat-by date. Using `find` does not change the content of the fridge though, it just *identifies* the right item, but leaves it in the fridge. If it should be removed as well, an additional call to `take` is required, with the item as argument. If no matching item can be found, `None` should be returned. As a metaphor, think about a person that wants to know whether there is still milk in the fridge, e.g., while writing a grocery shopping list, this person would not take the item out.

The second function is `take_before`, which takes a date in the aforementioned format as argument. It should *identify and remove* all items from the fridge for which the eat-by date is *before* the provided date and return them in a list. Return an empty list if no items match. As a metaphor, think about cleaning out your fridge on the weekend, you want to take out all items that went bad during the week.

**Note:** All state must be contained within the class. Do not store information in global variables or in class variables. It has to be possible to use multiple instances of the classes in parallel without suffering from side effects.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.

**Note:** We strongly encourage you to add more tests to the public test suite.


