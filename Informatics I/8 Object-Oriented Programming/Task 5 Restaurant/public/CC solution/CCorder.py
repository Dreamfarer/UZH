#!/usr/bin/env python3

from typing import List, Dict
from public.item import Item

class Order:

    def __init__(self, items: List[Item]):
        self.__items: Dict[Item, int] = self.__get_items(items)
        self.__bill_amount: int = self.__compute_bill_amount(items)

    def __repr__(self):
        return f"Order Items : {self.__items}, Order Bill Amount : {self.__bill_amount} "

    def get_bill_amount(self) -> int:
        return self.__bill_amount

    def __get_items(self, items: List[Item]) -> Dict[Item, int]:
        dict: Dict[Item, int] = {}
        for item in items:
            try:
                dict[item] += 1
            except KeyError:
                dict[item] = 1
        return dict

    def __compute_bill_amount(self, items: List[Item]) -> int:
        bill_amount: int = 0
        for item in items:
            bill_amount += item.get_item_price()
        return bill_amount

