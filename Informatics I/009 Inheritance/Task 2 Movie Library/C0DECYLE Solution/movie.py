#!/usr/bin/env python3

from __future__ import annotations
from typing import List

class Movie:

    def __init__(self, title: str, actors: List[str], duration: int):
        if len(title) == 0 or len(actors) == 0 or duration < 1:
            raise Warning("invalid input parameters")
        self.__title: str = title
        self.__actors: List[str] = actors
        self.__duration: int = duration

    def __repr__(self):
        actors: str = ", ".join([f"\"{actor}\"" for actor in self.__actors])
        return f"Movie(\"{self.__title}\", [{actors}], {self.__duration})"

    def __eq__(self, other: Movie):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(repr(self))

    def get_title(self) -> str:
        return self.__title

    def get_actors(self) -> List[str]:
        return list(self.__actors)

    def get_duration(self) -> int:
        return self.__duration

