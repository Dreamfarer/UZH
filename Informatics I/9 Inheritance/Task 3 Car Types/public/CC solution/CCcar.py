#!/usr/bin/env python3

from typing import Callable
from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def get_remaining_range(self) -> float:
        pass

    @abstractmethod
    def drive(self, dist: float) -> None:
        pass

    def _input_test(self, test: tuple, callback: Callable[[], None]) -> None:
        if not all(type(i) == float and i >= 0.0 for i in test):
            callback()
            raise Warning("invalid parameter input")

