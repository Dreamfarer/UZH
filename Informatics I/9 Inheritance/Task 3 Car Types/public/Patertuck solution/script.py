#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

########################################################################################################################
# Disclaimer! Solution gave me 3.6/4 points with the hint:
# Driving a HybridCar until all resources are depleted should set the levels of the battery charge and the gas tank to 0
# I then added all of that throughout the code changing the lvl of the tank or battery to 0
# it should give max or very close to max points. If anybody submits this solution, please let me know how many points
# it gave.
########################################################################################################################

from combustion_car import CombustionCar
from electric_car import ElectricCar
from hybrid_car import HybridCar


c = CombustionCar(40.0, 8.0)
print(c.get_remaining_range()) # 500
c.drive(25.0)
print(c.get_gas_tank_status()) # (38.0, 40.0)
try:
    c.drive(1000.0)
except Warning:
    print("fuel is depleted")
else:
    raise Warning("Here should have been raised a warning!")

e = ElectricCar(25.0, 500.0)
e.drive(100.0)
e.charge(2.0)
print(e.get_battery_status()) # (22.0, 25)

h = HybridCar(40.0, 8.0, 25.0, 500.0)
#h.switch_to_combustion()
print(h.get_remaining_range())
h.drive(600.0) # depletes fuel, auto-switch
print(h.get_gas_tank_status()) # (0.0, 40.0)
print(h.get_battery_status()) # (20.0, 25.0)