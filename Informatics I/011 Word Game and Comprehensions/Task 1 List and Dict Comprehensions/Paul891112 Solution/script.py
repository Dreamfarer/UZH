#!/usr/bin/python3

from data import words

def words_with_length(length):
    '''this one just serves as an example'''
    return [word for word in words if len(word) == length]

def words_containing_string(s):
    return [word for word in words if s in word]

def words_starting_with_character(c):
    return [word for word in words if word[0]==c]

def alphabet():
    '''you don't have to solve this one using a comprehension.'''
    res = ""
    for i in range(0,26):
        res += chr(97+i)
    return res

def dictionary():
    return {char: words_starting_with_character(char) for char in alphabet()}

def censored_words(s):
    return [word if not (s in word) else "x"*len(word) for word in words]
