# When many classes must follow a common interface or method name, but implement it differently.

# Importing ABC (Abstract Base Class) and abstractmethod decorator from abc module
from abc import ABC, abstractmethod

# Creating an abstract class named 'transport'
# This class will act as a blueprint for all types of transports
class transport(ABC):


    # Defining an abstract method named 'make_move'
    # Abstract methods don't have a body here — child classes must implement this
    @abstractmethod
    def make_move(self):
        pass

# Creating a concrete class 'bus' that inherits from the abstract class 'transport'
class bus(transport):

    # Implementing the abstract method 'make_move'
    def make_move(self):
        print("East")

# Creating a concrete class 'car' that inherits from the abstract class 'transport'
class car(transport):

    # Implementing the abstract method 'make_move'
    def make_move(self):
        print("West")

# Creating a concrete class 'bike' that inherits from the abstract class 'transport'
class bike(transport):

    # Implementing the abstract method 'make_move'
    def make_move(self):
        print("North")

# Creating objects of the concrete classes
Bus = bus()
Car = car()
Bike = bike()

Bus.make_move()
Car.make_move()
Bike.make_move()