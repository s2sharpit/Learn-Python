"""
@classmethod & @staticmethod

Description:
@classmethod and @staticmethod are decorators used to define methods inside a class in Python.
- @classmethod is used to define methods that operate on the class itself rather than on instances of the class. It takes a reference to the class (cls) as its first argument.
- @staticmethod is used to define methods that don't access the instance or the class itself. They behave like regular functions but are defined inside a class for better organization.

Usage:
- Use @classmethod when you need to define methods that operate on the class itself, such as alternate constructors or factory methods.
- Use @staticmethod when you need to define utility methods that don't rely on instance or class attributes.
"""


class Calculator:
    """Class: Represents a calculator."""

    def __init__(self, name: str):
        self.name = name

    def description(self):
        """Method: Print the description of the calculator."""
        print(f"{self.name} is a calculator!")

    @staticmethod
    def add_numbers(a: float, b: float):
        """Static Method: Add two numbers."""
        print(a + b)

    @classmethod
    def create_with_version(cls, name: str, version: int):
        """Class Method: Create a calculator with a specified version."""
        return cls(f"{name}: ({version})")


calc: Calculator = Calculator("Jeff")
calc.description()

calc1: Calculator = Calculator.create_with_version("Bob", 100)
calc1.description()

calc1.add_numbers(3, 4)  # Calling a static method on an instance
Calculator.add_numbers(10, 20)  # Calling a static method on the class
