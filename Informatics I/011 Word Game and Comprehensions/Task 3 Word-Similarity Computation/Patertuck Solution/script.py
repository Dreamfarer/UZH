#!/usr/bin/env python3

from random import shuffle
from difflib import SequenceMatcher

class WordLogic(object):

    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def find_words_with_right_size(self):
        with open("words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def is_similar(self, a, b, threshold):
        return SequenceMatcher(None, a, b).ratio() > threshold

    def word_selection(self):
        words = self.find_words_with_right_size()
        shuffle(words)
        end_list = words[0:self.num_words // 3]
        pick_word = end_list[0]

        for new_word in words[self.num_words // 3:]:

            if len(end_list) == self.num_words:
                break

            if self.is_similar(new_word, pick_word, 0.4) and new_word not in end_list:
                end_list.append(new_word)

        return end_list


