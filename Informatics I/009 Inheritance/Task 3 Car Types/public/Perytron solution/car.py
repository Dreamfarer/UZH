#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from abc import ABC, abstractmethod

# Set the following class to be abstract, meaning only subclasses can be instantiated
# Nothing is actually happening, is is only used to create the structure
class Car(ABC):

    @abstractmethod # Set the following function to be abstract (subclasses must implement this method)
    def get_remaining_range(self):
        pass

    @abstractmethod # Set the following function to be abstract (subclasses must implement this method)
    def drive(self, dist):
        pass
