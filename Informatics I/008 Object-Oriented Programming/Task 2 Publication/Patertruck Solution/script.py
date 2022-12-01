#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.

class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__title = title
        self.__year = year

    def is_valid_operand(self):
        return hasattr(self)

    def get_authors(self):
        copy = []
        for i in self.__authors:
            copy.append(i)
        return copy

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def __str__(self):
        author_list = "["
        for i, author in enumerate(self.get_authors()):
            author_list += f"\"{author}\""
            if i < len(self.get_authors()) - 1:
                author_list += ", "
        author_list += "]"
        return f"Publication({author_list}, \"{self.__title}\", {self.__year})"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.__authors) + 2

    def __eq__(self, other):
        if isinstance(other, Publication):
            return self.__authors == other.__authors and self.__year == other.__year and self.__title == other.__title
        return NotImplemented

    def __hash__(self):
        return hash((tuple(self.__authors), self.__title, self.__year))

    def __lt__(self, other):
        if not isinstance(other, Publication) or not isinstance(self, Publication):
            return NotImplemented
        if self.__authors != other.__authors:
            return self.__authors < other.__authors
        if self.__title != other.__title:
            return self.__title < other.__title
        if self.__year != other.__year:
            return self.__year < other.__year
        return False

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Publication) or not isinstance(self, Publication):
            return False
        if self.__authors != other.__authors:
            return self.__authors > other.__authors
        if self.__title != other.__title:
            return self.__title > other.__title
        if self.__year != other.__year:
            return self.__year > other.__year
        return False

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    # bonus implementation for iteration
    def __iter__(self):
        for item in self.__authors:
            yield item
        for item in (self.__title, self.__year):
            yield item
    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False

    sales = {
        p1: 273,
        p2: 398,
    }
