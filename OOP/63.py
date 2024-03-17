# __str__ & __repr__ methods
# __str__ method is called when we use the print() function to print the object.
# __repr__ method is called when we use the object in the interpreter.
# __str__ is used for a more readable representation of the object, and __repr__ is used for debugging and development.
# If __str__ is not defined, __repr__ is used as a fallback.
# If __repr__ is not defined, the default implementation is used.

class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.model} ({self.color})"

    def __repr__(self) -> str:
        return f"Car (model={self.model}, color={self.color})"


if __name__ == "__main__":
    car: Car = Car("BMW", "Blue")
    print(car)
    print(car.__repr__())
