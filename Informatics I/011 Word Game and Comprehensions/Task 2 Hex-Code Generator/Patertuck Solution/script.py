#!/usr/bin/env python3
from random import choice

class GameRunner(object):

    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        return [("0x" + "".join([choice("0123456789ABCDEF") for _ in range(4)]))for _ in range (self.columns * self.rows)]

x = GameRunner()
print(x.generate_hex_codes())



