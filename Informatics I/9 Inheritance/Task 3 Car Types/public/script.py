#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from public.combustion_car import CombustionCar
from public.electric_car import ElectricCar
from public.hybrid_car import HybridCar

c = CombustionCar(40.0, 8.0)
c.get_remaining_range() # 500
c.drive(25.0)
c.get_gas_tank_status() # (38.0, 40.0)
try:
    c.drive(1000.0)
except Warning:
    print("fuel is depleted")
else:
    raise Warning("Here should have been raised a warning!")

e = ElectricCar(25.0, 500.0)
e.drive(100.0)
e.charge(2.0)
e.get_battery_status() # (22.0, 25)

h = HybridCar(40.0, 8.0, 25.0, 500.0)
h.switch_to_combustion()
h.drive(600.0) # depletes fuel, auto-switch
h.get_gas_tank_status() # (0.0, 40.0)
h.get_battery_status() # (20.0, 25.0)