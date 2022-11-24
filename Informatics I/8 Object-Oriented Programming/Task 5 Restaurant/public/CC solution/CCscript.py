#!/usr/bin/env python3

from typing import List, Union
from public.item import Item
from public.order import Order

class Restaurant:

    def __init__(self, name: str, menu: List[Item]):
        self.__name: str = name
        self.__menu: List[Item] = menu
        self.__orders: List[Order] = []

    def get_restaurant_name(self) -> str:
        return self.__name

    def get_menu_list(self) -> List[Item]:
        return self.__menu

    def get_order_list(self) -> Union[List[Order], str]:
        if len(self.__orders) == 0:
            return "No order yet"
        return self.__orders

    def set_order(self, items: List[Item]) -> None:
        valid_items: List[Item] = [item for item in items if item in self.__menu]
        if len(valid_items) > 0:
            self.__orders.append(Order(valid_items))

    def get_revenue(self) -> int:
        revenue: int = 0
        for order in self.__orders:
            revenue += order.get_bill_amount()
        return revenue
        
