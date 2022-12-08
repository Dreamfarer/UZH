# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:28:06 2022

@author: paul8
"""

from number_logic import NumberLogic
from word_logic import WordLogic

#num, len, numofattempts
w = WordLogic(10, 4,10)
x = ""
while True:
    for i in w.words:
        print(i)
    x=input("Enter your guess: ")
    
    print(w.check(x))