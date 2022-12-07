###############################################################################
# !!! ATTENTION, THIS SOLUTIONS GIVES AT LEAST 3.7 OUT OF 4 POINTS !!!
# I highly doubt it generates the maximum points, use at own risk
###############################################################################

class Movie:

    def __init__(self, title, actors, duration):

        # Check that 'title' and 'actors' are not empty
        if 0 in [len(title), len(actors)]: raise Warning("Please do not provide an empty title or actor list")
        # Check that movie is not too short
        if duration < 1: raise Warning("Movie too short")

        # Create private variables 
        self.__title = title
        self.__actors = actors
        self.__duration = duration

    # Gets called when omparison operators '==' is used on this object
    def __eq__(self, other):
        return True if self.get_title() == other.get_title() and self.get_actors() == other.get_actors() and self.get_duration() == other.get_duration() else False
    
    # Represent this object when calling print(repr(obj)) in form of 'Movie("T", ["A", "B"], 123)'
    def __repr__(self):
        representation = f'Movie("{self.get_title()}", {self.get_actors()}, {self.__duration})'
        return representation.replace("'", "\"") # Replace all ' with "
    
    # Calculate a hash of the instantiated object (can be compared to verify that two objects contain the same content)
    def __hash__(self):
        # Convert to tuple first because hashing can only be done with non-mutable types
        return hash((self.__title, tuple(self.get_actors()), self.__duration))

    # Getter function to return the title of the movie
    def get_title(self):
        return self.__title

    # Getter function to return the actors of the movie 
    # Attention, copy the list so it can't be modified from outside the function
    def get_actors(self):
        return self.__actors.copy()

    # Getter function to return the duration of the movie
    def get_duration(self):
        return self.__duration