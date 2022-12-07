#!/usr/bin/env python3

from typing import List
from random import shuffle, choice
from difflib import SequenceMatcher

class WordLogic(object):

    def __init__(self, num_words: int, len_words: int):
        self.num_words: int = num_words
        self.len_words: int = len_words

    def find_words_with_right_size(self) -> List[str]:
        with open("words.txt") as f:
            word_list: List[str] = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def is_similar(self, a: str, b: str, threshold: float) -> bool:
        return SequenceMatcher(None, a, b).ratio() > threshold

    def word_selection(self) -> List[str]:
        words: List[str] = self.find_words_with_right_size()
        shuffle(words)
        selection: List[str] = words[:self.num_words // 3]
        words = words[self.num_words // 3:]
        while len(selection) < self.num_words:
            pick: str = choice(words)
            if pick not in selection and self.is_similar(pick, choice(selection), 0.4):
                selection.append(pick)
        return selection

