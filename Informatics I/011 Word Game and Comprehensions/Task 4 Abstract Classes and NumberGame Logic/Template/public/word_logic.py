#!/usr/bin/env python3

from random import choice, shuffle

# This is the current version of WordLogic that needs to be adapted
class WordLogic:

    def __init__(self, num_words, len_words, num_attempts):
        self.num_words = num_words
        self.len_words = len_words
        self.num_attempts = num_attempts
        self.words = self.__word_selection()
        self.password = choice(self.words)

    def __word_selection(self):
        words = self.__find_words_with_right_size()
        shuffle(words)
        return words[0:self.num_words]

    def __find_words_with_right_size(self):
        with open("resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def check(self, guess):
        if self.num_attempts == 0:
            raise Warning("No attempts left")
        if len(guess) != self.len_words:
            return False, ["Wrong length"]
        if guess == self.password:
            return True, ["Access granted!"]
        else:
            return False, [
                self.generate_feedback(guess),
                "Access denied!"
            ]

    def __generate_feedback(self, guess):
        matching = 0
        for i in range(self.len_words):
            if guess[i] == self.password[i]: matching += 1
        self.num_attempts = self.num_attempts - 1
        return "%d/%d correct" % (matching, self.len_words)
