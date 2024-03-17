"""
__init__ vs __new__

Description:
__new__ and __init__ are special methods in Python classes used for object creation and initialization, respectively.
- __new__ is responsible for creating a new instance of a class. It's a static method that takes the class itself (cls) as its first argument and returns a new instance of the class.
- __init__ is called after __new__ and is responsible for initializing the newly created object. It takes the newly created instance (self) along with any additional arguments and initializes its attributes.

Usage:
- Use __new__ when you need to customize how instances of a class are created, such as choosing between different subclasses based on input parameters.
- Use __init__ to initialize the attributes of a newly created instance. It's typically used to set up the initial state of the object.
"""


class Vehicle:
    """Class: Represents a vehicle."""

    def __new__(cls, wheels: int):
        """Method: Create a new instance of the class."""
        if wheels == 2:
            return Motorbike()
        elif wheels == 4:
            return Car()
        else:
            return super().__new__(cls)

    def __init__(self, wheels: int):
        """Method: Initialize the vehicle."""
        self.wheels = wheels
        print(f"Initializing vehicle with {self.wheels} wheels!")


class Motorbike:
    """Class: Represents a motorbike."""

    def __init__(self) -> None:
        """Method: Initialize the motorbike."""
        print("Initializing motorbike!")


class Car:
    """Class: Represents a car."""

    def __init__(self) -> None:
        """Method: Initialize the car."""
        print("Initializing car!")


mb = Vehicle(2)  # Creates a motorbike instance
cr = Vehicle(4)  # Creates a car instance
tr = Vehicle(18)  # Creates a generic Vehicle instance
