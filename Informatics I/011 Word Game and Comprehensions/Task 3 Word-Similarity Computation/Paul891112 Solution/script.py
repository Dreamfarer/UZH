#!/usr/bin/env python3

import random
from difflib import SequenceMatcher

class WordLogic(object):

    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def find_words_with_right_size(self):
        #changed my file path to public for simplicity
        with open("resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]
    
    #remember to from difflib import SequenceMatcher
    def is_similar(self,a,b,threshold):
        if SequenceMatcher(None, a, b).ratio() > threshold:
            return True
        return False
    
    def word_selection(self):
        words = self.find_words_with_right_size()
        temp = []
        #for 1/3 of num_words, choose random
        random.shuffle(words)
        temp.extend(words[0:self.num_words//3])
        
        #for the remaining ones:
        li = []
        li.extend(temp)
        
        while len(li)<self.num_words:
            #pick one from chosen 1/3
            picked_by_choice = random.choice(temp)
            #random pick from remaining words
            remaining_from_pool = random.choice(words[self.num_words//3:])
            
            #safety measure, if we picked the same as chosen, skip to next loop
            if remaining_from_pool in li:
                continue
            if WordLogic.is_similar(self,picked_by_choice,remaining_from_pool,0.4):
                li.append(remaining_from_pool)
            
        
            
            
        # TODO: instead of returning a random sample of words, use the strategy described in task 2
        return li
