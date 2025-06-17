# When many classes must follow a common interface or method name, but implement it differently.
# When NOT to Use Abstraction
#You only need 1 class	Use a normal class
#You don’t plan on inheriting	Don’t use abstractmethod
#You don’t need strict structure	Use simple duck typing (Python is dynamic)
# Real-World Example Scenarios
#Scenario	Why Use Abstraction?
#Payment gateways (Bkash, Stripe, PayPal)	All must implement pay() differently
#Transport app (Car, Bike, Bus)	All must implement move() method
#Social media bots (FacebookBot, InstagramBot)	All must implement post_message()
#Game design (Enemy, Player, Boss)	All must have attack() or die() methods


# Importing ABC (Abstract Base Class) and abstractmethod decorator from abc module
from abc import ABC, abstractmethod

# Creating an abstract class named 'Animal'
# This class will act as a blueprint for all types of animals
class Animal(ABC):

    # Defining an abstract method named 'make_sound'
    # Abstract methods don't have a body here — child classes must implement this
    @abstractmethod
    def make_sound(self):
        pass  # This means "do nothing" — no implementation here

# Creating a concrete class 'Dog' that inherits from the abstract class 'Animal'
class Dog(Animal):

    # Implementing the abstract method 'make_sound'
    def make_sound(self):
        print("Bark")  # Specific behavior for Dog

# Creating another concrete class 'Cat' that also inherits from 'Animal'
class Cat(Animal):

    # Implementing the abstract method 'make_sound'
    def make_sound(self):
        print("Meow")  # Specific behavior for Cat

# Creating another concrete class 'Cow'
class Cow(Animal):

    # Implementing the abstract method 'make_sound'
    def make_sound(self):
        print("Moo")  # Specific behavior for Cow

# Creating objects of the concrete classes
dog = Dog()  # Object of Dog
cat = Cat()  # Object of Cat
cow = Cow()  # Object of Cow

# Calling the make_sound method for each object
# This demonstrates polymorphism — same method name, different behavior
dog.make_sound()  # Output: Bark
cat.make_sound()  # Output: Meow
cow.make_sound()  # Output: Moo

