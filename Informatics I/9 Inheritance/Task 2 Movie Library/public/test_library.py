###############################################################################
# IRRELEVANT TO GRADING
# Might be useful as it contains more tests from our professor
###############################################################################

from unittest import TestCase
from public.movie import Movie
from public.moviebox import MovieBox
from public.library import Library

class LibraryTest(TestCase):

    def test_repr_movie(self):
        actual = repr(Movie("T", ["A", "B"], 123))
        expected = 'Movie("T", ["A", "B"], 123)'
        self.assertEqual(expected, actual)

    def test_repr_moviebox(self):
        actual = repr(MovieBox("T", [Movie("T2", ["A", "B"], 234)]))
        expected = 'MovieBox("T", [Movie("T2", ["A", "B"], 234)])'
        self.assertEqual(expected, actual)

    def test_repr_moviebox_2_movies(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [b, c])
        actual = repr(d)
        expected = 'MovieBox("Top Movies", [Movie("The Godfather", ["Brando", "Pacino"], 175), ' \
                   'Movie("12 Angry Men", ["Fonda", "Cobb"], 96)])'
        self.assertEqual(expected, actual)

    def test_duration_moviebox(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [b, c])
        e = MovieBox("Another MovieBox", [a, b, c])
        self.assertEqual(271, d.get_duration())
        self.assertEqual(413, e.get_duration())

    def test_get_actors_movie(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        self.assertEqual(["Robbins", "Freeman"], a.get_actors())
        self.assertEqual(["Brando", "Pacino"], b.get_actors())

    def test_get_actors_moviebox(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [b, c])
        e = MovieBox("Another MovieBox", [a, b, c])
        # remember: list must be sorted alphabetically!
        self.assertEqual(['Brando', 'Cobb', 'Fonda', 'Pacino'], d.get_actors())
        self.assertEqual(['Brando', 'Cobb', 'Fonda', 'Freeman', 'Pacino', 'Robbins'], e.get_actors())

    def test_get_actors_moviebox_duplicates(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino", "Robbins"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [a, b, c])
        # remember: list must be sorted alphabetically!
        self.assertEqual(['Brando', 'Cobb', 'Fonda', 'Freeman', 'Pacino', 'Robbins'], d.get_actors())

    def test_library(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        d = MovieBox("Top Movies", [b, c])
        l = Library()
        l.add_movie(a)
        l.add_movie(d)
        self.assertEqual(413, l.get_total_duration())

    def test_equal_movies(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        self.assertEqual(a == b, True)