from dataclasses import dataclass


@dataclass
class Fruit:
    name: str
    calories: float

apple: Fruit = Fruit('Apple', 30)
print(apple)
del apple
print(apple)