#!/usr/bin/env python3

class Publication:

    def __init__(self, authors: list, title: str, year: int):
        self.__authors: list = authors
        self.__title: str = title
        self.__year: int = year

    def get_authors(self) -> list:
        return list(self.__authors)

    def get_title(self) -> str:
        return self.__title

    def get_year(self) -> int:
        return self.__year

    def __repr__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

    def to_string(self) -> str:
        authors: str = ", ".join([f"\"{i}\"" for i in self.__authors])
        return f"Publication([{authors}], \"{self.__title}\", {self.__year})"

    def __eq__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return self.__is_equal(other)

    def __ne__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return not self.__is_equal(other)

    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return self.__is_less(other)

    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return self.__is_less(other) or self.__is_equal(other)

    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return not (self.__is_less(other) or self.__is_equal(other))

    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return not self.__is_less(other)

    def __is_equal(self, other) -> bool:
        return self.get_unique_hash() == other.get_unique_hash()

    def __is_less(self, other) -> bool:
        if self.get_authors() == other.get_authors():
            if self.get_title() == other.get_title():
                return self.get_year() < other.get_year()
            else:
                return self.get_title() < other.get_title()
        else:
            return self.get_authors() < other.get_authors()

    def __hash__(self):
        return self.get_unique_hash()

    def get_unique_hash(self) -> int:
        return hash(tuple(self.__authors) + (self.__title, str(self.__year)))
    
