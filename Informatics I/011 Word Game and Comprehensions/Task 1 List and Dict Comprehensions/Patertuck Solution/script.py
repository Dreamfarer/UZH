#!/usr/bin/python3

from data import words
import string

def words_with_length(length):
    '''this one just serves as an example'''
    return [word for word in words if len(word) == length]

def words_containing_string(s):
    return [s_word for s_word in words if s in s_word]

def words_starting_with_character(c):
    return [starting_word for starting_word in words if starting_word[0]==c]

def alphabet():
    '''you don't have to solve this one using a comprehension.'''
    return string.ascii_lowercase

def dictionary():
    return {key: [word for word in words_starting_with_character(key)] for key in alphabet()}

def censored_words(s):
    return [word if s not in word else len(word) * "x" for word in words]
