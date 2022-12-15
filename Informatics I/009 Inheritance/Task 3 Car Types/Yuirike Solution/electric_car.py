#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car


class ElectricCar(Car):
    def __init__(self, battery_size, battery_range_km):
        self.__battery_size = battery_size
        self.__battery_range_km = battery_range_km
        self._input_valid(battery_size)
        self._input_valid(battery_range_km)
        '''
        We mainly worked with the "distance" in CombCar
        We want to keep working with that, so we'll avoid issues with
        HybridCar, that inherits both and works with "distance" as well.
        The missing value is the battery consumption.
        According to them:
        BS = 25, BR = 500
        Drive 100
        B_Status with BS = 20
        Drive 100 consumed 5
        I assume the BConsumption = BR / BS = 500/25 = 20
        As: 100/20 = 5, 400/20 = 20
        '''
        self.__batt_consumption = battery_range_km/battery_size
        self.__rem_range = battery_range_km
        self.__rem_elec = self.__rem_range/self.__batt_consumption

    def charge(self, kwh):
        self._input_valid(kwh)
        self.__rem_elec += kwh
        if self.__rem_elec > self.__battery_size:
            self.__rem_elec = 0
            raise Warning("E_Overloard")

        kwh *= self.__batt_consumption
        self.__rem_range += kwh

    def get_battery_status(self):
        if self.__rem_elec != 0:
            return (self.__rem_range/self.__batt_consumption, self.__battery_size)
        return (self.__rem_elec, self.__battery_size)

    def get_remaining_range(self):
        return self.__rem_range

    def drive(self, dist):
        self._input_valid(dist)
        self.__rem_range -= dist
        self.__rem_elec = self.__rem_range/self.__batt_consumption
        if self.__rem_elec < 0:
            self.__rem_elec = 0
            raise Warning("Charged depleted")

