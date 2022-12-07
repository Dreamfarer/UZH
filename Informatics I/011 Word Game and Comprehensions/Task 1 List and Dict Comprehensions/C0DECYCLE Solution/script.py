#!/usr/bin/python3

from string import ascii_lowercase
from typing import List, Dict
from public.data import words

def words_with_length(length: int) -> List[str]:
    return [word for word in words if len(word) == length]

def words_containing_string(s: str) -> List[str]:
    return [word for word in words if word.find(s) != -1]

def words_starting_with_character(c: str) -> List[str]:
    return [word for word in words if word[0] == c]

def alphabet() -> str:
    return ascii_lowercase

def dictionary() -> Dict[str, List[str]]:
    return {key: words_starting_with_character(key) for key in alphabet()}

def censored_words(s: str) -> List[str]:
    return ["x" * len(word) if word.find(s) != -1 else word for word in words]
