#!/usr/bin/env python3

from public.geometric_object import GeometricObject

class Cube(GeometricObject):

    def __init__(self, side_length: float, color: str, filled: bool):
        super().__init__(color, filled)
        self.__side_length: float = side_length

    def get_side_length(self) -> float:
        return self.__side_length

    def get_area(self) -> float:
        return 6 * (self.__side_length ** 2)

    def get_volume(self) -> float:
        return self.__side_length ** 3
