#!/usr/bin/env python3
# TODO: Implement Me!
from game_logic import GameLogic
from random import choice, shuffle
from abc import ABC, abstractmethod


class NumberLogic(GameLogic):
    
        
    #tested in playground      
    def _word_selection(self):
        li=[] #list of number sequence
        nums = list("1234567890")
        while len(li)<self.num_words:
            temp=""
            shuffle(nums)
            temp = ''.join(nums[0:self.len_words])
            if temp in li:
                continue
            else:
                li.append(temp)
            
        return li
    
    #Override
    def check(self, guess):
        if len(guess) != self.len_words:
            raise Warning("Wrong input length")
        #from element 0 to second last element: raise warning if current 
        #element appears in trailing elements
        for i in range(0,self.len_words-1):
            if guess[i] in guess[i+1:]:
                raise Warning("Repeated number")
        return super().check(guess)    
        
        
    def _generate_feedback(self, guess):
        matching = 0
        self.num_attempts = self.num_attempts - 1
        for i in range(0,len(guess)):
            if guess[i] in self.password:
                matching += 1
        return "%d/%d correct" % (matching, self.len_words)
    
