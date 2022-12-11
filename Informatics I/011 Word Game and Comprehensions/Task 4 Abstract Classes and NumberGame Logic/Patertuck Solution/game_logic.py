from random import choice
from abc import ABC, abstractmethod


class GameLogic(ABC):

    def __init__(self, num_words, len_words, num_attempts):
        self.num_words = num_words
        self.len_words = len_words
        self.num_attempts = num_attempts
        self.words = self._word_selection()
        self.password = choice(self.words)

    def check(self, guess):
        if self.num_attempts == 0:
            raise Warning("No attempts left")
        if len(guess) != self.len_words:
            return False, ["Wrong length"]
        if guess == self.password:
            return True, ["Access granted!"]
        else:
            return False, [
                self._generate_feedback(guess),
                "Access denied!"
            ]

    @abstractmethod
    def _word_selection(self):
        pass

    @abstractmethod
    def _generate_feedback(self, guess):
        pass
