#!/usr/bin/env python3

from public.geometric_object import GeometricObject

class Cylinder(GeometricObject):

    def __init__(self, radius: float, height: float, color: str, filled: bool):
        super().__init__(color, filled)
        self.__PI: float = 3.14
        self.__radius: float = radius
        self.__height: float = height

    def get_radius(self) -> float:
        return self.__radius

    def get_height(self) -> float:
        return self.__height

    def get_area(self) -> float:
        return 2 * self.__PI * self.__radius * (self.__radius + self.__height)

    def get_volume(self) -> float:
        return self.__PI * (self.__radius ** 2) * self.__height
