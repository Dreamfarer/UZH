#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

########################################################################################################################
# Disclaimer! Solution gave me 3.6/4 points with the hint:
# Driving a HybridCar until all resources are depleted should set the levels of the battery charge and the gas tank to 0
# I then added all of that throughout the code changing the lvl of the tank or battery to 0
# it should give max or very close to max points. If anybody submits this solution, please let me know how many points
# it gave.
########################################################################################################################

from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def get_remaining_range(self):
        pass

    @abstractmethod
    def drive(self, dist):
        pass
