#!/usr/bin/env python3

# TODO: Implement Me!
from abc import ABC, abstractmethod
from random import choice, shuffle

class GameLogic(ABC):
    
    #copy-pasted from word_logic.py
    def __init__(self, num_words, len_words, num_attempts):
        self.num_words = num_words
        self.len_words = len_words
        self.num_attempts = num_attempts
        #word_selection should be protected, not private
        self.words = self._word_selection()
        self.password = choice(self.words)
        
    #copy-pasted from word_logic.py  
    def check(self, guess):
        if self.num_attempts == 0:
            print("Answer is: {}".format(self.password))
            raise Warning("No attempts left")
        if len(guess) != self.len_words:
            return False, ["Wrong length"]
        if guess == self.password:
            return True, ["Access granted!"]
        else:
            return False, [
                #change access to protected
                self._generate_feedback(guess),
                "Access denied!"
            ]
        
    @abstractmethod
    def _word_selection():
        pass
    
    @abstractmethod
    def _generate_feedback():
        pass
    