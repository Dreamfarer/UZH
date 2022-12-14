'''
Abstract methods.
Define methods that the child classes need to have.
Don't really have to contain anything, as you here.
The signature has to be carried over tho, then overridden. 
'''
from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def get_remaining_range(self):
        pass

    @abstractmethod
    def drive(self, dist: float):
        self.__dist = dist
        pass

    def _input_valid(self, argument):
        if type(argument) != float:
            raise Warning("False data type")
        elif argument < 0:
            raise Warning("Too negative!")