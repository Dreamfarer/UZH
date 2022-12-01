#!/usr/bin/env python3

from typing import Tuple
from public.car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity: float, gas_per_100km: float):
        self._input_test((gas_capacity, gas_per_100km), lambda: self._zero_gas())
        self.__gas: float = gas_capacity
        self.__gas_capacity: float = gas_capacity
        self.__gas_efficiency: float = gas_per_100km

    def fuel(self, f: float) -> None:
        self._input_test((f,), lambda: self._zero_gas())
        self.__gas += f
        if self.__gas > self.__gas_capacity:
            self._zero_gas()
            raise Warning("gas overflow")

    def get_gas_tank_status(self) -> Tuple[float, float]:
        return self.__gas, self.__gas_capacity

    def get_remaining_range(self) -> float:
        return (self.__gas / self.__gas_efficiency) * 100.0

    def drive(self, dist: float) -> None:
        self._input_test((dist,), lambda: self._zero_gas())
        self.__gas -= (dist / 100.0) * self.__gas_efficiency
        if self.__gas < 0.0:
            self._zero_gas()
            raise Warning("gas tank empty")

    def _zero_gas(self) -> None:
        self.__gas = 0.0

