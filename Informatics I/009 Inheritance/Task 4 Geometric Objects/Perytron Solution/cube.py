from public.geometric_object import GeometricObject

###############################################################################
# Be aware that I've started to use explicity typing, you DO NOT have to do this:
# A prime example is the following function: "set_side_length(self, side_length: float) -> None:"
# You can safely leave it like "set_side_length(self, side_length):""
# The only thing that has changed is ": float" and "-> None"
###############################################################################

class Cube(GeometricObject):

    def __init__(self, side_length: float, color: str, filled: bool):
        # Call init function of 'GeometricObject'
        # You have to do this because the init function of 'GeometricObject' will not be called automatically
        # Therefore, 'Cube' would not inherit 'self.__color' and 'self.__filled'
        super().__init__(color, filled)
        self.__side_length: float = side_length

    def get_side_length(self) -> float:
        return self.__side_length

    def set_side_length(self, side_length: float) -> None:
        self.__side_length = side_length

    def get_area(self) -> float:
        return round(6 * pow(self.__side_length, 2), 2)
        
    def get_volume(self) -> float:
        return round(pow(self.__side_length, 3), 2)
