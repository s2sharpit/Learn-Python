# Description: Constructor in Python
# This is a constructor method in Python. It is called when an object is created. It is used to initialize the object's state. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.

class Fruit:
    def __init__(self, name: str) -> None:
        self.name = name
        self.letter_count = len(name)
        print("Constructor called!")


fruit: Fruit = Fruit("Banana")
print(fruit.name)
print(fruit.letter_count)
