#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from public.movie import Movie
from public.moviebox import MovieBox
from public.library import Library

a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
b = Movie("The Godfather", ["Brando", "Pacino"], 175)
c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
d = MovieBox("Top Movies", [b, c])

l = Library()
l.add_movie(a)
l.add_movie(d)
print(l.get_movies())
print(l.get_total_duration())
