#!/usr/bin/env python3

from __future__ import annotations
from typing import List, Union
from public.movie import Movie

class MovieBox(Movie):

    def __init__(self, title, movies: List[Union[Movie, MovieBox]]):
        if len(movies) == 0 or not all(isinstance(child, Movie) for child in movies):
            raise Warning("invalid input parameters")
        super().__init__(title, [""], 1)
        self.__children: List[Union[Movie, MovieBox]] = movies

    def __repr__(self):
        movies: str = ", ".join([repr(movie) for movie in self.get_movies()])
        return f"MovieBox(\"{self.get_title()}\", [{movies}])"

    def get_actors(self) -> List[str]:
        actors: List[str] = []
        for child in self.__children:
            actors += child.get_actors()
        return sorted(list(set(actors)), key=str.lower)

    def get_duration(self) -> int:
        duration: int = 0
        for child in self.__children:
            duration += child.get_duration()
        return duration

    def get_movies(self) -> List[Union[Movie, MovieBox]]:
        return list(self.__children)

