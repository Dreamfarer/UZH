#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):

        # Call a user-made function that checks that the input is a float and that it is strictly greater than zero
        self.verifier(battery_size, float, ">")
        self.verifier(battery_range_km, float, ">")

        # Define private variables used later on
        self.__battery_size = battery_size
        self.__charge = battery_size
        self.__efficiency = battery_size / battery_range_km # How many kilo-watt hours are used up for 1 km

    # Charge the battery
    def charge(self, kwh):
        self.verifier(kwh, float, ">=") # Check the input type and that is is greater or equal than zero
        self.__charge += kwh # Charge the battery
        if self.__charge > self.__battery_size: self.verifier() # Throw warning if battery has been overcharged

    # Get the current gas level and its maximum capacity
    def get_battery_status(self):
        return (self.__charge, self.__battery_size)

    # Get how far this electric car can still drive
    def get_remaining_range(self):
        return self.__charge / self.__efficiency

    # Drive the car!
    # This function is very special because, you might have noticed that we explicitly call "ElectricCar.verifier()"
    # and not "self.verifier()", what we are be used to. It is rather complicated to explain but if we call this 'drive'
    # from the hybrid car, we pass the object (the hybrid car) with the 'self' keyword. And now comes the magic: If we were to
    # write "self.verifier()", it would not take the verifier from this class here, it rather takes the one defined in
    # 'hybrid_car'. However, we did not define a verifier function there, so it would take the newest function it can find 
    # with this name. Remember, we inhertied from two classes! By explicitly writting it like this we ensure that the 
    # verifier function of this class is used. However, we still pass on the object (the hybrid car) with 'self' because we 
    # will change its (the hybrid car's) __charge variable and not this class' variable. 
    # Contact me on Whatsapp if you need help! :)
    def drive(self, dist):
        ElectricCar.verifier(self, dist, float, ">=") # Check the input type and that is is greater or equal than zero
        self.__charge -= dist * self.__efficiency # Subtract the used-up battery
        if self.__charge <= 0: ElectricCar.verifier(self) # Throw warning if battery has run out of power

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
        self.__charge = 0 # Set battery to 0 (required by the excercise)
        raise Warning("Skill issue. Not my (...) problem.") # Raise warning