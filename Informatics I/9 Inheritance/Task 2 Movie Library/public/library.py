###############################################################################
# !!! ATTENTION, THIS SOLUTIONS GIVES AT LEAST 3.7 OUT OF 4 POINTS !!!
# I highly doubt it generates the maximum points, use at own risk
###############################################################################

from public.movie import Movie
from public.moviebox import MovieBox

class Library(MovieBox):

    # Create private variables 
    def __init__(self):
        self.__movies = []

    # Add movies or movieboxes to the library
    # Make sure that the objects are not already contained
    def add_movie(self, movie):
        if not movie in self.__movies: self.__movies.append(movie)

    # Getter function to return all movies contained in the box
    def get_movies(self):

        # I will use a dictionary to make sorting of the movies easier afterwards
        movie_dictionary = {}
        output_movies = []

        # Loop over all movies and moviesboxes in the library
        for movie in self.__movies:
            # Dependent on the type, use a different method to get the movies
            if isinstance(movie, MovieBox): 
                for temporary_movie in movie.get_movies():
                    movie_dictionary[temporary_movie.get_title()] = temporary_movie
            else: movie_dictionary[movie.get_title()] = movie

        # Extract the movies from the dictionary, ordered by title
        for key in sorted(movie_dictionary):
            output_movies.append(movie_dictionary[key])
        return output_movies

    # Getter function to return the duration of all movies together
    def get_total_duration(self):
        duration = 0
        # Loop over all movies and collect the durations
        for movie in self.__movies:
            duration += movie.get_duration()
        return duration