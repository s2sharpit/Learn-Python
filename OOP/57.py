# Classes & Objects
# This is a constructor method in Python. It is called when an object is created. It is used to initialize the object's state. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.

class Lamp:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color

    def turn_on(self):
        print(self.model, "is turned on!")

    def turn_off(self):
        print(self.model, "is turned off!")

    def describe(self):
        print(f"Lamp: {self.model} ({self.color})")


red_lamp: Lamp = Lamp("Rx55", "Red")
red_lamp.turn_on()
red_lamp.turn_off()
red_lamp.describe()
red_lamp.color = "Green"
red_lamp.describe()

blue_lamp: Lamp = Lamp("Bx05", "Blue")
blue_lamp.turn_on()
blue_lamp.turn_off()
