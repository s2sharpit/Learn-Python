"""
Topic: Abstract Base Classes and @abstractmethod decorator

Description:
Abstract Base Classes (ABCs) in Python allow you to define abstract methods and properties that must be implemented by subclasses. They provide a way to enforce a contract for classes that inherit from them. The @abstractmethod decorator is used to denote abstract methods within an abstract class. 

Usage:
- Abstract Base Classes are useful when you want to define a common interface that multiple subclasses must adhere to.
- @abstractmethod decorator is used to declare abstract methods within abstract classes. Subclasses must implement these methods.
- When defining an ABC, you can use regular methods alongside abstract methods to provide default implementations for common behavior.
- Subclasses of an ABC must implement all abstract methods and properties defined by the ABC, ensuring that they adhere to the contract defined by the ABC.

"""

from abc import ABC, abstractmethod

class Phone(ABC):
    """
    Abstract class representing a generic phone.
    """
    def __init__(self, model: str):
        self.model = model

    @property
    @abstractmethod
    def power(self):
        """
        Abstract property representing the power status of the phone.
        """
        ...

    @abstractmethod
    def call_target(self, person: str):
        """
        Abstract method to call a target person.
        """
        ...


class iBanana(Phone):
    """
    Subclass representing an iBanana phone.
    """
    def __init__(self, model: str):
        super().__init__(model)

    @property
    def power(self):
        """
        Property representing the power status of the iBanana phone.
        """
        raise NotImplementedError("Not implemented yet!")

    def call_target(self, person: str):
        """
        Method to call a target person using the iBanana phone.
        """
        pass


phone = iBanana("iBanana")

print(phone.power)
