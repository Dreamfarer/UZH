from abc import ABC, abstractmethod


class GeometricObject(ABC):

    def __init__(self, color=str, filled=bool):
        self.__color = color
        self.__filled = filled

        if type(color) != str or type(filled) != bool:
            raise Warning("Invalid input type!")

    def get_color(self):
        color = str()
        color = self.__color
        return color

    def set_color(self, color):
        if type(color) != str:
            raise Warning("Invalid input type for color!")
        self.__color = color

    def get_filled(self):
        filled = bool()
        filled = self.__filled
        return filled

    def set_filled(self, filled):
        if type(filled) != bool:
            raise Warning("Invalid input type needs to be boolean!")
        self.__filled = filled

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass
