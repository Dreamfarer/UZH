#!/usr/bin/env python3

class GameRunner(object):

    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        return ["0x0000"] * (self.columns * self.rows)

