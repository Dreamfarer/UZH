#!/usr/bin/env python3
import random
class GameRunner(object):

    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        li = []
        res = "0x"
        for j in range(0,self.columns * self.rows):
            for i in range(0,4):
                res += random.choice("0123456789ABCDEF")
            li.append(res)
            res = "0x"
        
        
        return li

