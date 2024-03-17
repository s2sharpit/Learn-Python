class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def __repr__(self) -> str:
        return f"{self.name}: {self.calories}"


fruits: list[Fruit] = [Fruit("Apple", 50), Fruit("Banana", 150), Fruit("Ananas", 100)]


sorted_fruits: list[Fruit] = sorted(fruits, key=lambda fruit: fruit.calories)
# sorted_fruits: list[Fruit] = sorted(fruits, key=str, reverse=True) # sorts the list ignoring the case of names and in descending order
print(sorted_fruits)
