#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

########################################################################################################################
# Disclaimer! Solution gave me 3.6/4 points with the hint:
# Driving a HybridCar until all resources are depleted should set the levels of the battery charge and the gas tank to 0
# I then added all of that throughout the code changing the lvl of the tank or battery to 0
# it should give max or very close to max points. If anybody submits this solution, please let me know how many points
# it gave.
########################################################################################################################

from car import Car


class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        self.__battery_size = battery_size
        self.__battery_range_km = battery_range_km
        self.__c = battery_size

        if type(battery_size) != float or type(battery_range_km) != float or battery_size < 0 or battery_range_km < 0:
            raise Warning("Invalid input type")

    def charge(self, kwh):
        if type(kwh) != float or kwh < 0:
            raise Warning("Invalid input type for charge")
        self.__c += kwh
        if self.__c > self.__battery_size:
            self.__c = 0
            raise Warning("Battery overcharged")

    def get_battery_status(self):
        current_battery = self.__c
        max_battery = self.__battery_size
        return current_battery, max_battery

    def get_remaining_range(self):
        return self.__c / self.__battery_size * self.__battery_range_km

    def drive(self, dist):
        if type(dist) != float or dist < 0:
            raise Warning("Invalid input type")

        if self.get_remaining_range() < dist:
            self.__c = 0
            raise Warning("Battery empty")
        else:
            self.__c -= dist / self.__battery_range_km * self.__battery_size


