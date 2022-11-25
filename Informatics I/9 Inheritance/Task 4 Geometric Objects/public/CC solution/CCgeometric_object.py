#!/usr/bin/env python3

from abc import ABC, abstractmethod

class GeometricObject(ABC):

    def __init__(self, color: str, filled: bool):
        self.__color: str = color
        self.__filled: bool = filled

    def get_color(self) -> str:
        return self.__color

    def set_color(self, color: str) -> None:
        self.__color = color

    def get_filled(self) -> bool:
        return self.__filled

    def set_filled(self, filled: bool) -> None:
        self.__filled = filled

    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_volume(self) -> float:
        pass
