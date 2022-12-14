#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from combustion_car import CombustionCar
from electric_car import ElectricCar
from hybrid_car import HybridCar


print("H_ELEC")
HE = HybridCar(40.0, 8.0, 25.0, 500.0)
HE.drive(10.0)
print(HE.get_battery_status())
HE.charge(0.4)
print(HE.get_battery_status())
print("")
print("Elec")
E = ElectricCar(25.0, 500.0)
E.drive(10.0)
print(E.get_battery_status())
E.charge(0.4)
print(E.get_battery_status())
print("")


print("H_Comb")
HC = HybridCar(40.0, 8.0, 25.0, 500.0)
HC.switch_to_combustion()
HC.drive(10.0)
print(HC.get_gas_tank_status())
HC.fuel(0.5)
print(HC.get_gas_tank_status())


print("")
print("Comb")
C = CombustionCar(40.0,8.0)
C.drive(10.0)
print(C.get_gas_tank_status())
C.fuel(0.5)
print(C.get_gas_tank_status())

