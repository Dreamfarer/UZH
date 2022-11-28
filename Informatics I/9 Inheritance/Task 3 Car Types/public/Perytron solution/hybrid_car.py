#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.combustion_car import CombustionCar
from public.electric_car import ElectricCar

class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        # Call the init functions of both car types. This enables us to use their variables and functions
        CombustionCar.__init__(self, gas_capacity, gas_per_100km) 
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__mode = "electric" # Store which mode is currently active

    def switch_to_combustion(self):
        self.__mode = "combustion"

    def switch_to_electric(self):
        self.__mode = "electric"

    # Get the range the hybrid car is able to drive (both gas and electrict)
    def get_remaining_range(self):
        return ElectricCar.get_remaining_range(self) + CombustionCar.get_remaining_range(self)

    # Drive the car!
    # This, agian, is a tad more complicate function. 
    # It is split into two parts for driving in electric and combustion respectively.
    # You should also know that it is recursive, that's why the strucutre might confuse you a little bit
    def drive(self, dist):

        # Algorithm for drving electric
        if self.__mode == "electric":
            
            ElectricCar.verifier(self, dist, float, ">=") # Check the input type and that is is greater or equal than zero
            
            # Calculate how much of the desired distance can be driven electric
            # On the first glance, it might come across as wired:
            # If you drive less than the maximum reachable distance, the following 'drive' function will go trough
            # without an error, boom, done. It does not matter that 'remaining' is negative, because it is never used.
            # However, if you try to travel more than the maximum, the variable will be positive and the 'drive' function 
            # will throw an error that we catch and then switch to combustion. In that case the vehicle has driven its 
            # maximum distance represented by the 'remaining' variable.
            remaining = dist - ElectricCar.get_remaining_range(self)
            
            try: ElectricCar.drive(self, dist)
            except: 
                # Check the state of the gas, if it is also empty, you can't drive the whole distance 
                # and the car throws an error.
                if self.get_gas_tank_status()[0] != 0: 
                    self.switch_to_combustion()
                    if remaining == 0: return # If it is exactely zero, you don't need to switch and drive again.
                    self.drive(remaining) # Call this function recursively with the adjusted distance
                else: raise Warning("Out of fuel and battery juice!")

        # Algorithm for drving combustion
        else:
            
            CombustionCar.verifier(self, dist, float, ">=") # Check the input type and that is is greater or equal than zero
            
            # Calculate how much of the desired distance can be driven with combustion
            # On the first glance, it might come across as wired:
            # If you drive less than the maximum reachable distance, the following 'drive' function will go trough
            # without an error, boom, done. It does not matter that 'remaining' is negative, because it is never used.
            # However, if you try to travel more than the maximum, the variable will be positive and the 'drive' function 
            # will throw an error that we catch and then switch to electic. In that case the vehicle has driven its 
            # maximum distance represented by the 'remaining' variable.
            remaining = dist - CombustionCar.get_remaining_range(self)
            
            try: CombustionCar.drive(self, dist)
            except: 
                # Check the state of the battery, if it is also empty, you can't drive the whole distance 
                # and the car throws an error.
                if self.get_battery_status()[0] != 0:
                    self.switch_to_electric()
                    if remaining == 0: return # If it is exactely zero, you don't need to switch and drive again.
                    self.drive(remaining) # Call this function recursively with the adjusted distance
                else: raise Warning("Out of fuel and battery juice!")

