# __eq__
# __eq__ is a method that is used to compare two objects of a class. It returns True if the objects are equal and False if they are not.

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

    print(apple == apple2)
