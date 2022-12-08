#!/usr/bin/env python3

from typing import Tuple, List
from abc import ABC, abstractmethod
from random import choice

class GameLogic(ABC):

    def __init__(self, num_words: int, len_words: int, num_attempts: int):
        self.num_words: int = num_words
        self.len_words: int = len_words
        self.num_attempts: int = num_attempts
        self.words: List[str] = self._word_selection()
        self.password: str = choice(self.words)

    def check(self, guess: str) -> Tuple[bool, List[str]]:
        if self.num_attempts == 0:
            raise Warning("No attempts left")
        if len(guess) != self.len_words:
            return False, ["Wrong length"]
        if guess == self.password:
            return True, ["Access granted!"]
        return False, [self._generate_feedback(guess), "Access denied!"]

    @abstractmethod
    def _word_selection(self) -> List[str]:
        pass

    @abstractmethod
    def _generate_feedback(self, guess: str) -> str:
        pass

