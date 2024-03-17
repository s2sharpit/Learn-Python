# Methods vs Functions in python
# Methods are called by its name, but it is associated to an object (dependent).
# A function can be called without creating a class or object.
# A method is implicitly passed the object on which it is invoked.
# It may or may not return any data.


def greet(name):  # Function
    print(f"Hello, {name}!")


greet("John")


class Person:

    def __init__(self, name: str):
        self.name = name

    def greet(self, name):  # Method
        print(f"Hello, {self.name}  and {name}!")


p = Person("Tushar")
p.greet("John")
