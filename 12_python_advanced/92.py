# Dataclasses

from dataclasses import dataclass


@dataclass
class Fruit2:
    name: str
    calories: float

class Fruit:
    def __init__(self, name: str, calories: str) -> None:
        self.name = name
        self.calories = calories

    def __eq__(self, other: object) -> bool:
        # return self.name == other.name and self.calories == other.calories
        return self.__dict__ == other.__dict__

    # Not comparing the class in the way as we want it to compare without using the above method!


if __name__ == "__main__":
    apple: Fruit = Fruit("Apple", 10)
    apple2: Fruit = Fruit("Apple", 10)

    apple21: Fruit = Fruit2("Apple", 10)
    apple22: Fruit = Fruit2("Apple", 10)

    print(apple == apple2)
    print(apple21 == apple22)

    print(apple)
    print(apple21)
