#!/usr/bin/env python3

from typing import Tuple
from public.car import Car

class ElectricCar(Car):

    def __init__(self, battery_size: float, battery_range_km: float):
        self._input_test((battery_size, battery_range_km), lambda: self._zero_battery())
        self.__battery: float = battery_size
        self.__battery_size: float = battery_size
        self.__battery_efficiency: float = battery_range_km / battery_size

    def charge(self, kwh: float) -> None:
        self._input_test((kwh,), lambda: self._zero_battery())
        self.__battery += kwh
        if self.__battery > self.__battery_size:
            self._zero_battery()
            raise Warning("battery overcharge")

    def get_battery_status(self) -> Tuple[float, float]:
        return self.__battery, self.__battery_size

    def get_remaining_range(self) -> float:
        return self.__battery * self.__battery_efficiency

    def drive(self, dist: float) -> None:
        self._input_test((dist,), lambda: self._zero_battery())
        self.__battery -= dist / self.__battery_efficiency
        if self.__battery < 0.0:
            self._zero_battery()
            raise Warning("battery empty")

    def _zero_battery(self) -> None:
        self.__battery = 0.0

