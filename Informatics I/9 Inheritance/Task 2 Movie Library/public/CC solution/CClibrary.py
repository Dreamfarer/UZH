#!/usr/bin/env python3

from typing import List, Union
from public.movie import Movie
from public.moviebox import MovieBox

class Library:

    def __init__(self):
        self.__children: List[Union[Movie, MovieBox]] = []

    def add_movie(self, movie: Union[Movie, MovieBox]) -> None:
        if movie not in self.__children:
            self.__children.append(movie)

    def get_movies(self) -> List[Movie]:
        movies: List[Movie] = []
        for child in self.__children:
            if isinstance(child, MovieBox):
                movies += self.__get_unboxed_movies(child)
            else:
                movies.append(child)
        return sorted(list(set(movies)), key=lambda movie: movie.get_title())

    def get_total_duration(self) -> int:
        duration: int = 0
        for child in self.__children:
            duration += child.get_duration()
        return duration

    def __get_unboxed_movies(self, movie_box: MovieBox) -> List[Movie]:
        movies: List[Movie] = []
        for child in movie_box.get_movies():
            if isinstance(child, MovieBox):
                movies += self.__get_unboxed_movies(child)
            else:
                movies.append(child)
        return movies

