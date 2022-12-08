#!/usr/bin/env python3

from typing import List
from random import sample
from game_logic import GameLogic

class WordLogic(GameLogic):

    def _word_selection(self) -> List[str]:
        return sample(self.__find_words_with_right_size(), self.num_words)

    def _generate_feedback(self, guess: str) -> str:
        self.num_attempts -= 1
        matching: int = sum([1 if guess[i] == self.password[i] else 0 for i in range(self.len_words)])
        return f"{matching}/{self.len_words} correct"

    def __find_words_with_right_size(self) -> List[str]:
        with open("words.txt") as f:
            word_list: List[str] = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

