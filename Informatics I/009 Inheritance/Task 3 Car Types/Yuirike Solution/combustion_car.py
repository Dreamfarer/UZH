from car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        self._input_valid(gas_capacity)
        self._input_valid(gas_per_100km)
        self.__gas_capacity = gas_capacity
        self.__gas_per_100km = gas_per_100km*0.01
            
        '''
        Third value is needed. 
        Here: How far can CombCar drive with given cap and gas consumption?
        Their example: GC = 40.0, GP100 = 8.0 --> Remaining Distance = 500
        500 = (40.0/8.0)*100
        Or: 500 = 40.0 / (8.0/100)
        '''
        self.__rem_range = gas_capacity/(gas_per_100km*0.01)
        self.__rem_gas = self.__rem_range*self.__gas_per_100km


    def fuel(self, f):
        self._input_valid(f)
        f = f/self.__gas_per_100km
   
        self.__rem_range+=f
        self.__rem_gas = self.__rem_range*self.__gas_per_100km
        if self.__rem_gas > self.__gas_capacity:
            self.__rem_gas = 0
            raise Warning("G_Overload")
                
    def get_gas_tank_status(self):
        return (self.__rem_gas, self.__gas_capacity)

    def get_remaining_range(self):
        return self.__rem_range

    def drive(self, dist):
        self._input_valid(dist)
        self.__rem_range-=dist
        self.__rem_gas = self.__rem_range*self.__gas_per_100km
        if self.__rem_gas < 0:
            self.__rem_gas = 0
            raise Warning("Fuel depleted")
