from combustion_car import CombustionCar
from electric_car import ElectricCar


class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__switchE = 1
        self.__switchC = 0
        self._input_valid(gas_capacity)
        self._input_valid(gas_per_100km)
        self._input_valid(battery_range_km)
        self._input_valid(battery_size)
        self.__EE = battery_range_km
        self.__CE = gas_capacity/(gas_per_100km*0.01)
        '''
        We have to work with distances once more to make the hybrid work.
        The difficult part is the auto-switch
        In attempt 1, I kept using the values from the other two classes
        Here, I introduce to constants and base the switch on those, so changes within
        other classes has no affect. If these constants fulfill a certain condition
        HybridCar executes the action, regardless of the other two classes.
        HybridCar executes auto-switch.
        '''

    def switch_to_combustion(self):
        self.__switchC = 1
        self.__switchE = 0

    def switch_to_electric(self):
        self.__switchE = 1
        self.__switchC = 0

    def get_remaining_range(self):
        return ElectricCar.get_remaining_range(self)+CombustionCar.get_remaining_range(self)

    def fuel(self, f):
        CombustionCar.fuel(self, f)
        self.__CE += CombustionCar.get_remaining_range(self)

    def charge(self, kwh):
        ElectricCar.charge(self, kwh)
        self.__EE += ElectricCar.get_remaining_range(self)

    def drive(self, dist):
        self._input_valid(dist)
        # if self.__EE+self.__CE-dist < 0:
        #     raise Warning("No Charge nor Fuel")

        if self.__switchE == 1:
            if self.__EE >= dist:
                ElectricCar.drive(self, dist)
                self.__EE -= dist
            else:
                ElectricCar.drive(self, self.__EE)
                new_dist = dist - self.__EE
                self.__EE = 0
                CombustionCar.drive(self, new_dist)
                self.__CE -= new_dist
                self.__switchE = 0
                self.__switchC = 1

        elif self.__switchC == 1:
            if self.__CE >= dist:
                CombustionCar.drive(self, dist)
                self.__CE -= dist
            else:
                CombustionCar.drive(self, self.__CE)
                new_dist = dist - self.__CE
                self.CE = 0
                ElectricCar.drive(self, new_dist)
                self.__EE -= new_dist
                self.__switchE = 1
                self.__switchC = 0

    # def get_Eenergy(self):
    #     return self.__EE

    # def get_Cenergy(self):
    #     return self.__CE
