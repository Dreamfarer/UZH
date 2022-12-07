#!/usr/bin/python3

from typing import List
from random import choice

class GameRunner(object):

    def __init__(self):
        self.rows: int = 17
        self.columns: int = 2

    def generate_hex_codes(self) -> List[str]:
        return ["0x" + "".join([choice("0123456789ABCDEF") for j in range(4)]) for i in range(self.columns * self.rows)]

