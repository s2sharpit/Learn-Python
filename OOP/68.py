# super()
# super() is a built-in function that returns a proxy object that allows you to refer parent class by 'super' keyword.
# It's useful in multiple inheritance as it resolves the correct method or attribute to be called.
# Syntax:
# super().method_name
# super().attribute_name

class Lamp:
    def __init__(self, name: str):
        self.name = name

    def turnOn(self):
        print(f"Turning on: {self.name}")

    def turnOff(self):
        print(f"Turning off: {self.name}")


class ElectricLamp(Lamp):
    def __init__(self, name: str):
        super().__init__(name)

    def turnOn(self):
        print("Using Electricity...")
        super().turnOn()


el_lamp: ElectricLamp = ElectricLamp("Bob")
el_lamp.turnOn()
