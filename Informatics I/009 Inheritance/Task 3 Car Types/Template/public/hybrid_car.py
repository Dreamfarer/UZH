#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.combustion_car import CombustionCar
from public.electric_car import ElectricCar

class HybridCar:

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        pass

    def switch_to_combustion(self):
        pass

    def switch_to_electric(self):
        pass

    def get_remaining_range(self):
        pass

    def drive(self, dist):
        pass
