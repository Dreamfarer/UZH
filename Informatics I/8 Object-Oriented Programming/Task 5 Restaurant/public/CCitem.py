#!/usr/bin/env python3

class Item:

    def __init__(self, name: str, price: int):
        self.__name: str = name
        self.__price: int = price

    def __repr__(self):
        return self.__name

    def get_item_name(self) -> str:
        return self.__name

    def get_item_price(self) -> int:
        return self.__price
        
