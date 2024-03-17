# "is" vs "=="

class Fruit:
    def __init__(self, name: str, calories: float) -> None:
        self.name = name
        self.calories = calories

    def __eq__(self, other) -> bool:
        return self.__dict__ == other.__dict__


if __name__ == "__main__":
    #     fruit_a: Fruit = Fruit("Banana", 10)
    #     fruit_b: Fruit = Fruit("Banana", 10)

    #     print(f"a: {id(fruit_a)}, b: {id(fruit_b)}")
    #     print(f"fruit_a is fruit_b = {fruit_a is fruit_b}")
    #     print(f"fruit_a == fruit_b = {fruit_a == fruit_b}")

    # _ = 500
    # a = _ + 500
    # b = 500

    a = 10
    b = 10
    # sometimes it give the same id if the value is same, it happens because of python optimizes the code

    print(f"a: {id(a)}, b: {id(b)}")
    print(f"a is b = {a is b}")
    print(f'a == b = {a == b}')
