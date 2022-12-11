from game_logic import GameLogic
from random import sample


class NumberLogic(GameLogic):

    def _word_selection(self):
        sequences = []

        while len(sequences) < self.num_words:
            sequence = "".join(sample("0123456789", self.len_words))

            if sequence not in sequences:
                sequences.append(sequence)

        return sequences

    def _generate_feedback(self, guess):
        matching = 0
        for number in guess:
            if number in self.password:
                matching += 1
        self.num_attempts -= 1
        return "%d/%d correct" % (matching, self.len_words)

    def check(self, guess):
        if len(guess) != self.len_words:
            raise Warning("Invalid input length!")
        for number in guess:
            if guess.count(number) != 1:
                raise Warning("Input can't have a number more than once!")
        return super().check(guess)
