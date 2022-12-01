#!/usr/bin/env python3

from public.geometric_object import GeometricObject

class Cone(GeometricObject):

    def __init__(self, radius: float, vertical_height: float, slant_height: float, color: str, filled: bool):
        super().__init__(color, filled)
        self.__PI: float = 3.14
        self.__radius: float = radius
        self.__vertical_height: float = vertical_height
        self.__slant_height: float = slant_height

    def get_radius(self) -> float:
        return self.__radius

    def get_vertical_height(self) -> float:
        return self.__vertical_height

    def get_slant_height(self) -> float:
        return self.__slant_height

    def get_area(self) -> float:
        return self.__PI * self.__radius * (self.__radius + self.__slant_height)

    def get_volume(self) -> float:
        return (1 / 3) * self.__PI * (self.__radius ** 2) * self.__vertical_height
