#!/usr/bin/env python3

from unittest import TestCase
from combustion_car import CombustionCar
from electric_car import ElectricCar
from hybrid_car import HybridCar

class TestCars(TestCase):

    def test_comb_remaining_range(self):
        c = CombustionCar(40.0, 8.0)
        self.assertAlmostEqual(500.0, c.get_remaining_range(), delta=0.001)

    def test_comb_drive(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        self.assertAlmostEqual(38.0, c.get_gas_tank_status()[0], delta=0.001)

    def test_comb_remaining_range(self):
        c = CombustionCar(40.0, 8.0)
        self.assertAlmostEqual(500.0, c.get_remaining_range(), delta=0.001)

    def test_comb_remaining_range_after_drive(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        self.assertAlmostEqual(475.0, c.get_remaining_range(), delta=0.001)

    def test_comb_drive(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        self.assertAlmostEqual(38.0, c.get_gas_tank_status()[0], delta=0.001)

    def test_elec_remaining_range(self):
        e = ElectricCar(40.0, 500.0)
        self.assertAlmostEqual(500.0, e.get_remaining_range(), delta=0.001)

    def test_elec_remaining_range_after_drive(self):
        e = ElectricCar(40.0, 500.0)
        e.drive(50.0)
        self.assertAlmostEqual(450.0, e.get_remaining_range(), delta=0.001)

    def test_comb_invalid_tank(self):
        with self.assertRaises(Warning, msg="Tank and range must be of type: float!"):
            c = CombustionCar("40.0", 8.0)

    def test_comb_invalid_neg_tank(self):
        with self.assertRaises(Warning, msg="Tank and range must be of type: float!"):
            c = CombustionCar(-50.0, 8.0)

    def test_comb_invalid_100km(self):
        with self.assertRaises(Warning, msg="Tank and range must be of type: float!"):
            c = CombustionCar(40.0, "8.0")

    def test_comb_invalid_neg_100km(self):
        with self.assertRaises(Warning, msg="Tank and range must be of type: float!"):
            c = CombustionCar(40.0, -5.0)

    def test_elec_invalid_battery(self):
        with self.assertRaises(Warning, msg="Battery and range must be of type: float!"):
            e = ElectricCar("40.0", 500.0)

    def test_elec_invalid_neg_battery(self):
        with self.assertRaises(Warning, msg="Battery and range must be of type: float!"):
            e = ElectricCar(-50.0, 500.0)

    def test_elec_invalid_range(self):
        with self.assertRaises(Warning, msg="Battery and range must be of type: float!"):
            e = ElectricCar(40.0, "500.0")

    def test_elec_invalid_neg_range(self):
        with self.assertRaises(Warning, msg="Battery and range must be of type: float!"):
            e = ElectricCar(40.0, -500.0)

    def test_comb_fuel_normal(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(100.0)
        c.fuel(4.0)
        self.assertAlmostEqual(36, c.get_gas_tank_status()[0], delta=0.001)

    def test_comb_fuel_overfill_error(self):
        with self.assertRaises(Warning, msg="Tank got overfilled!"):
            c = CombustionCar(40.0, 8.0)
            c.drive(100.0)
            c.fuel(10.0)

    def test_comb_fuel_invalid_fuel(self):
        with self.assertRaises(Warning, msg="Fuel amount must be of type: float!"):
            c = CombustionCar(40.0, 8.0)
            c.drive(100.0)
            c.fuel("10.0")

    def test_comb_fuel_neg_fuel(self):
        with self.assertRaises(Warning, msg="Fuel amount must be of type: float!"):
            c = CombustionCar(40.0, 8.0)
            c.drive(100.0)
            c.fuel(-10.0)

    def test_comb_fuel_overfill_reset(self):
        try:
            c = CombustionCar(40.0, 8.0)
            c.drive(100.0)
            c.fuel(10.0)
        except:
            self.assertAlmostEqual(0, c.get_gas_tank_status()[0], delta=0.001)

    def test_elec_fuel_normal(self):
        e = ElectricCar(40.0, 500.0)
        e.drive(50.0)
        e.charge(2.0)
        self.assertAlmostEqual(38, e.get_battery_status()[0], delta=0.001)

    def test_elec_fuel_overfill_error(self):
        with self.assertRaises(Warning, msg="Battery got over-charged!"):
            e = ElectricCar(40.0, 500.0)
            e.drive(50.0)
            e.charge(10.0)

    def test_elec_fuel_invalid_fill(self):
        with self.assertRaises(Warning, msg="Kwh amount must be of type: float!"):
            e = ElectricCar(40.0, 500.0)
            e.drive(50.0)
            e.charge("10.0")

    def test_elec_fuel_neg_fill(self):
        with self.assertRaises(Warning, msg="Kwh amount can't be negative!"):
            e = ElectricCar(40.0, 500.0)
            e.drive(50.0)
            e.charge(-10.0)

    def test_elec_fuel_overfill_reset(self):
        try:
            e = ElectricCar(40.0, 500.0)
            e.drive(50.0)
            e.charge(10.0)
        except:
            self.assertAlmostEqual(0, e.get_battery_status()[0], delta=0.001)

    def test_elec_drive_neg(self):
        with self.assertRaises(Warning, msg="Distance amount can't be negative!"):
            e = ElectricCar(40.0, 500.0)
            e.drive(-50.0)

    def test_elec_drive_invalid(self):
        with self.assertRaises(Warning, msg="Distance amount must be of type: float!"):
            e = ElectricCar(40.0, 500.0)
            e.drive("50.0")

    def test_elec_drive_far_error(self):
        with self.assertRaises(Warning, msg="Battery got depleted through driving!"):
            e = ElectricCar(40.0, 500.0)
            e.drive(550)

    def test_elec_drive_far_error_reset(self):
        try:
            e = ElectricCar(40.0, 500.0)
            e.drive(550.0)
        except:
            self.assertAlmostEqual(0, e.get_battery_status()[0], delta=0.001)

    def test_comb_drive_neg(self):
        with self.assertRaises(Warning, msg="Distance amount can't be negative!"):
            c = CombustionCar(40.0, 8.0)
            c.drive(-25.0)

    def test_comb_drive_invalid(self):
        with self.assertRaises(Warning, msg="Distance amount must be of type: float!"):
            c = CombustionCar(40.0, 8.0)
            c.drive("25.0")

    def test_comb_drive_far_error(self):
        with self.assertRaises(Warning, msg="Battery got depleted through driving!"):
            c = CombustionCar(40.0, 8.0)
            c.drive(600.0)

    def test_comb_drive_far_error_reset(self):
        try:
            c = CombustionCar(40.0, 8.0)
            c.drive(600.0)
        except:
            self.assertAlmostEqual(0, c.get_gas_tank_status()[0], delta=0.001)

    def test_comb_get_tank_status(self):
        c = CombustionCar(40.0, 8.0)
        c.drive(25.0)
        self.assertEqual((38.0, 40.0), c.get_gas_tank_status())

    def test_elec_get_tank_status(self):
        e = ElectricCar(40.0, 500.0)
        e.drive(50.0)
        self.assertEqual((36.0, 40.0), e.get_battery_status())

    def test_hybrid_drive_is_elec(self):
        h = HybridCar(40.0, 8.0, 25.0, 500.0)
        h.drive(100.0)
        self.assertAlmostEqual(20, h.get_battery_status()[0], delta=0.001)

    def test_hybrid_drive_far_error(self):
        with self.assertRaises(Warning, msg="Battery got depleted and gas fully consumed through driving!"):
            h = HybridCar(40.0, 8.0, 25.0, 500.0)
            h.drive(1001.0)

    def test_hybrid_drive_far_reset_battery(self):
        try:
            h = HybridCar(40.0, 8.0, 25.0, 500.0)
            h.drive(1001.0)
        except:
            self.assertAlmostEqual(
                0.0, h.get_battery_status()[0], delta=0.0001)

    def test_hybrid_drive_far_reset_tank(self):
        try:
            h = HybridCar(40.0, 8.0, 40.0, 500.0)
            h.drive(1001.0)
        except:
            self.assertAlmostEqual(
                0.0, h.get_gas_tank_status()[0], delta=0.0001)

    def test_hybrid_drive_switch_comb(self):
        h = HybridCar(40.0, 8.0, 25.0, 500.0)
        h.switch_to_combustion()
        h.drive(50.0)
        self.assertAlmostEqual(36, h.get_gas_tank_status()[0], delta=0.001)

    def test_hybrid_drive_auto_switch_comb(self):
        h = HybridCar(40.0, 8.0, 25.0, 500.0)
        h.drive(550.0)
        self.assertAlmostEqual(36, h.get_gas_tank_status()[0], delta=0.001)

    def test_hybrid_drive_azto_switch_elec(self):
        h = HybridCar(40.0, 8.0, 25.0, 500.0)
        h.switch_to_combustion()
        h.drive(600.0)
        self.assertAlmostEqual(20, h.get_battery_status()[0], delta=0.001)

    def test_hybrid_drive_invalid_dist(self):
        with self.assertRaises(Warning, msg="Distance amount must be of type: float!"):
            h = HybridCar(40.0, 8.0, 25.0, 500.0)
            h.drive("50.0")

    def test_hybrid_drive_neg_dist(self):
        with self.assertRaises(Warning, msg="Distance amount can't be negative!"):
            h = HybridCar(40.0, 8.0, 25.0, 500.0)
            h.drive(-50.0)
