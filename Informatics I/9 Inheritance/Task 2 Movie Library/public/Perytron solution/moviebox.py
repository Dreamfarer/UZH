###############################################################################
# !!! ATTENTION, THIS SOLUTIONS GIVES AT LEAST 3.7 OUT OF 4 POINTS !!!
# I highly doubt it generates the maximum points, use at own risk
###############################################################################

from public.movie import Movie

class MovieBox(Movie):

    def __init__(self, title, movies):

        # Check that the 'title' and 'movies' are not empty
        if 0 in [len(title), len(movies)]: raise Warning("Please do not provide an empty movie list or title")
        # Check that 'movies' is a list of 'Movie'
        for movie in movies: 
            if not isinstance(movie, Movie): raise Warning("Faulty movie provided")

        # Create private variables 
        self.__title = title
        self.__movies = movies

    # Gets called when omparison operators '==' is used on this object
    def __eq__(self, other):
        return True if self.get_title() == other.get_title() and self.get_movies() == other.get_movies() else False

    # Represent this object when calling print(repr(obj)) in form of 'MovieBox("T2", [Movie("T", ["A", "B"], 123)])'
    def __repr__(self):
        representation = f'MovieBox("{self.get_title()}", {self.get_movies()})'
        return representation.replace("'", "\"")

    # Calculate a hash of the instantiated object (can be compared to verify that two objects contain the same content)
    def __hash__(self):
        # Convert to tuple first because hashing can only be done with non-mutable types
        return hash((self.get_title(), tuple(self.get_movies()))) 

    # Getter function to return the actors of all movies this movie box contains
    # Attention, they must must sorted alphabetically and all duplicates need to be removed
    def get_actors(self):
        actors = []
        # Loop over all movies contained in the box and return the authors
        for movie in self.__movies:
            actors.extend(movie.get_actors())
        actors = sorted(set(actors)) # Sort the authors alphabetically and remove duplicates
        return actors

    # Getter function to return the duration of all movies together
    def get_duration(self):
        duration = 0
        # Loop over all movies and collect the durations
        for movie in self.__movies:
            duration += movie.get_duration()
        return duration

    # Getter function to return the title of the moviebox
    def get_title(self):
        return self.__title

    # Getter function to return all movies contained in the box
    # Attention, copy the list so it can't be modified from outside the function
    def get_movies(self):
        return self.__movies.copy()