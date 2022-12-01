A data structure can be used to bundle related attributes into a coherent entity. Such entities make the contained data completely transparent and can be used as first-class values. In turn, data structures do not provide any business logic or behavior that can break in the future.

In this task, you will write a data structure `Publication` that can be used to represent scientific articles. In a simplified form, such an article has a *list of authors* (assume that only last names are used), a *title*, and a *year* of publication. A `Publication` can then be used in your programs, for example:

    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

Several extensions are necessary to integrate a `Publication` value in Python as well as, for example, an `int`. First of all, it must be easy to explore such values, be it by printing or by looking at it in a debugger. To make this work, it is necessary to provide the two methods [\__repr__](https://docs.python.org/3.5/reference/datamodel.html#object.__repr__) and [\__str__](https://docs.python.org/3.5/reference/datamodel.html#object.__str__). For this task, the representation of both should be the same and should be the same as the string required for the instantiation. More specifically:

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    assert str(p) == s

The next important property of a data structure is that is is possible to identify equal values. To allow that, a data structure has to implement the special method [\__eq__](https://docs.python.org/3.5/reference/datamodel.html#object.\_\_eq\_\_) and, by extension, also [\__hash__](https://docs.python.org/3.5/reference/datamodel.html#object.__hash__). Please read the Python documentation and study their relation. Implement both methods and make sure that `__eq__` does not crash when compared with types that are not `Publication`.

Once these methods are implemented, it is possible to use the `==` operator, e.g., when asserting for the expected output in a test.

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2) # True
    print(p2 == p3) # False

Being hashable is required when objects should serve as dictionary keys. In addition, it is also required that such objects are immutable. This means that the different `Publication` attributes must not be stored in public instance variables. These could be changed from the outside, which would change their hash value uncontrollably. To solve this issue, store the attributes in private instance variables (e.g., `__title`) and only provide public *getter* methods that allow indirect, read-only access (i.e., `get_authors`, `get_title`, `get_year`). This can be more tricky than you might think on a first glance. For example, you need to make sure that you do not directly expose the list of authors, because it is mutable and could be changed by users!

Once you made `Publication` immutable, it can safely be used as a dictionary key:

    sales = {
    	p1: 273,
    	p3: 398,
    }

Last, but not least, data structures can implement various special methods that are used by the comparison operators (i.e., [<](https://docs.python.org/3.5/reference/datamodel.html#object.__lt__), [<=](https://docs.python.org/3.5/reference/datamodel.html#object.__le__), [>](https://docs.python.org/3.5/reference/datamodel.html#object.__gt__), [>=](https://docs.python.org/3.5/reference/datamodel.html#object.__ge__)). Implement these methods to make `Publication` comparable. The sorting should be performed according to the following rules:

* First compare the list of authors names, e.g., `["A"] < ["B"]` and `["A", "B"] < ["A", "C"]`, shorter lists are smaller, e.g., `["A"] < ["A", "B"]`. As a tip, figure out how list comparisons work.
* If the author list is identical, compare titles with standard string comparison.
* Otherwise, compare years with standard int comparison.

All *six* comparison operators should *return* boolean values or the `NotImplemented` *value* when called with a non-`Publication` object as the second parameter. Be smart and think about the relation of the various comparisons. A smart implementation only supports some base cases and delegates the remaining comparisons to these base cases. Once all methods are implemented, it is possible to use the comparison operators (e.g., `p1 < p3`) or to use other utilities like `sorted(references)`.

**Note:** We encourage you to play around with your data structure to understand the effect that providing the various methods has on the way in which you can use your data structure.

**Note:** All state must be contained within the class. Do not store information in global variables or in class variables. It has to be possible to use multiple instances of the classes in parallel without suffering from side effects.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.

**Note:** We strongly encourage you to add more tests to the public test suite.


