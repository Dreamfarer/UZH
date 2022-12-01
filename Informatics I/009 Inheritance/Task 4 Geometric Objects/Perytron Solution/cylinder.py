from public.geometric_object import GeometricObject

###############################################################################
# Be aware that I've started to use explicity typing, you DO NOT have to do this:
# A prime example is the following function: "set_side_length(self, side_length: float) -> None:"
# You can safely leave it like "set_side_length(self, side_length):""
# The only thing that has changed is ": float" and "-> None"
###############################################################################

class Cylinder(GeometricObject):

    def __init__(self, radius: float, height: float, color: str, filled: bool):
        # Call init function of 'GeometricObject'
        # You have to do this because the init function of 'GeometricObject' will not be called automatically
        # Therefore, 'Cylinder' would not inherit 'self.__color' and 'self.__filled'
        super().__init__(color, filled)
        self.__PI: float = 3.14
        self.__radius: float = radius
        self.__height: float = height

    def get_radius(self) -> float:
        return self.__radius

    def get_height(self) -> float:
        return self.__height

    def get_area(self) -> float:
        return round(2 * self.__PI * pow(self.__radius, 2) + 2 * self.__PI * self.__radius * self.__height, 2)

    def get_volume(self) -> float:
        return round(self.__PI * pow(self.__radius, 2) * self.__height, 2)
