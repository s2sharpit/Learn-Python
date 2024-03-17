# isinstance()

# isinstance() is used to check if an object is an instance of a class or a subclass of a class. It returns True if the object is an instance of the specified class, otherwise, it returns False.


class Fruit:
    def __init__(self, name: str):
        self.name = name


if __name__ == "__main__":
    apple: Fruit = Fruit("Apple")
    apple: str = 'apple'
    banana = Fruit("Banana")

    print(isinstance(apple, Fruit))
    print(isinstance(banana, Fruit))
    print(isinstance("string", str))
    print(isinstance(10, str))

    if isinstance(apple, Fruit):
        print("Apple is a fruit")
    else:
        print("This string is crazy")
