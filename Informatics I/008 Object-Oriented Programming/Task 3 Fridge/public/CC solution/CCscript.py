#!/usr/bin/env python3
from typing import Optional, List, Tuple

class Fridge:

    def __init__(self):
        self.__groceries: List[Tuple[int, str]] = []

    def store(self, item: Tuple[int, str]) -> None:
        self.__groceries.append(item)
        self.__groceries.sort()

    def take(self, item: Tuple[int, str]) -> Tuple[int, str]:
        try:
            self.__groceries.remove(item)
            self.__groceries.sort()
            return item
        except ValueError:
            raise Warning("No matching grocery")

    def find(self, name: str) -> Optional[Tuple[int, str]]:
        try:
            return [item for item in self.__groceries if item[1] == name][0]
        except IndexError:
            return None

    def take_before(self, date: int) -> List[Tuple[int, str]]:
        bad: List[Tuple[int, str]] = [item for item in self.__groceries if item[0] < date]
        for item in bad:
            self.take(item)
        return bad

    def __iter__(self):
        self.__i: int = -1
        return self

    def __next__(self):
        self.__i += 1
        if self.__i >= len(self.__groceries):
            raise StopIteration
        return self.__groceries[self.__i]

    def __len__(self):
        return len(self.__groceries)

