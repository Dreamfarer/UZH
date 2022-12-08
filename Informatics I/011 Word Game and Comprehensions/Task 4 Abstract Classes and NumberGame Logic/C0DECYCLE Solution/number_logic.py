#!/usr/bin/env python3

from typing import Tuple, List
from game_logic import GameLogic
from random import sample

class NumberLogic(GameLogic):

    def check(self, guess: str) -> Tuple[bool, List[str]]:
        if len(guess) != self.len_words:
            raise Warning("Invalid input parameter")
        for c in guess:
            if guess.count(c) > 1:
                raise Warning("Invalid input parameter")
        return super().check(guess)

    def _word_selection(self) -> List[str]:
        seqs: List[str] = []
        while len(seqs) < self.num_words:
            seq: str = "".join(sample("0123456789", self.len_words))
            if seq not in seqs:
                seqs.append(seq)
        return seqs

    def _generate_feedback(self, guess: str) -> str:
        self.num_attempts -= 1
        matching: int = sum([1 if c in self.password else 0 for c in guess])
        return f"{matching}/{self.len_words} correct"
    
