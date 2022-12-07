#!/usr/bin/env python3

from public.combustion_car import CombustionCar
from public.electric_car import ElectricCar

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity: float, gas_per_100km: float, battery_size: float, battery_range_km: float):
        self.__COMBUSTION: int = 0
        self.__ELECTRIC: int = 1
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__mode: int = self.__ELECTRIC

    def switch_to_combustion(self) -> None:
        self.__mode = self.__COMBUSTION

    def switch_to_electric(self) -> None:
        self.__mode = self.__ELECTRIC

    def get_remaining_range(self) -> float:
        return CombustionCar.get_remaining_range(self) + ElectricCar.get_remaining_range(self)

    def drive(self, dist: float) -> None:
        current_remaining: float = self.__get_mode_remaining_range()
        try:
            if self.__mode == self.__COMBUSTION:
                CombustionCar.drive(self, dist)
            else:
                ElectricCar.drive(self, dist)
        except Warning:
            if self.__mode == self.__COMBUSTION:
                self.switch_to_electric()
                ElectricCar.drive(self, dist-current_remaining)
            else:
                self.switch_to_combustion()
                CombustionCar.drive(self, dist-current_remaining)

    def __get_mode_remaining_range(self) -> float:
        if self.__mode == self.__COMBUSTION:
            return CombustionCar.get_remaining_range(self)
        else:
            return ElectricCar.get_remaining_range(self)

