# Initializer
# __init__ is a special method in Python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.

class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color
        print(f'{self.model} ({self.color})')

    def drive(self):
        print(f'{self.model} is now driving.')


if __name__ == '__main__':
    car: Car = Car('BMW', 'Blue')
    car2: Car = Car('Ferrari', 'Red')

    # car.drive()
    car2.drive()