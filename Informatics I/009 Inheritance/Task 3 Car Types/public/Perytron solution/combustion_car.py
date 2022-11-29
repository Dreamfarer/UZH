#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):

        # Call a user-made function that checks that the input is a float and that it is strictly greater than zero
        self.verifier(gas_capacity, float, ">")
        self.verifier(gas_per_100km, float, ">")

        # Define private variables used later on
        self.__gas_capacity = gas_capacity # in liters
        self.__gas = gas_capacity # in liters
        self.__gas_per_100km = gas_per_100km # fuel consumption in liters per 100 kilometers
    
    # Fill up the tank of the combustion car
    def fuel(self, f):
        self.verifier(f, float, ">=") # Check the input type and that is is greater or equal than zero
        self.__gas += f # Fill up the tank
        if self.__gas > self.__gas_capacity: self.verifier() # Throw warning if tank is overfilled

    # Get the current gas level and the maximum capacity
    def get_gas_tank_status(self):
        return (self.__gas, self.__gas_capacity)

    # Get how far this combustion car can still drive
    def get_remaining_range(self):
        return (self.__gas * 100) / self.__gas_per_100km

    # Drive the car!
    # This function is very special because, you might have noticed that we explicitly call "CombustionCar.verifier()"
    # and not "self.verifier()", what we are be used to. It is rather complicated to explain but if we call this 'drive'
    # from the hybrid car, we pass the object (the hybrid car) with the 'self' keyword. And now comes the magic: If we were to
    # write "self.verifier()", it would not take the verifier from this class here, it rather takes the one defined in
    # 'hybrid_car'. However, we did not define a verifier function there, so it would take the newest function it can find 
    # with this name. Remember, we inhertied from two classes! By explicitly writting it like this we ensure that the 
    # verifier function of this class is used. However, we still pass on the object (the hybrid car) with 'self' because we 
    # will change its (the hybrid car's) __gas variable and not this class' variable. 
    # Contact me on Whatsapp if you need help! :)
    def drive(self, dist):
        CombustionCar.verifier(self, dist, float, ">=") # Check the input type and that is is greater or equal than zero
        self.__gas -= (dist / 100.0) * self.__gas_per_100km # Subtract the used-up gas
        if self.__gas <= 0: CombustionCar.verifier(self) # Throw warning if gas tank has fully depleated
    
    # Function to check wheather the input type matches the desired one
    # and that numbers are greater (and equal) to zero
    def verifier(self, to_be_tested=None, should_be_this_type=int, check_type=""):

        # Convert 'int' to 'float' for easier comparison later on
        if isinstance(to_be_tested, int): to_be_tested = float(to_be_tested)
        if should_be_this_type == int: should_be_this_type = float

        # Check that numbers are larger than zero
        if isinstance(to_be_tested, float) and check_type == ">":
            if to_be_tested > 0: return

        # Check that numbers are larger or equal than zero
        elif isinstance(to_be_tested, float) and check_type == ">=":
            if to_be_tested >= 0: return

        # If the number has passed the tests or is not even a number, check its input type
        # Don't throw error if the type matches the desired one
        elif isinstance(to_be_tested, should_be_this_type): return
        self.__gas = 0 # Set battery to 0 (required by the excercise)
        raise Warning("Skill issue. Not my (...) problem.") # Raise warning
