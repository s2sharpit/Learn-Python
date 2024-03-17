# Private & Protected Variables in Python
# Private Variables: __variable_name
# Protected Variables: _variable_name
# Note: Python does not have a private/protected variable. It's just a convention that we use to tell other developers that these variables should not be accessed directly from outside the class. It's not a security feature.
# Note: We can access private/protected variables/methods from outside the class but it's not recommended to do so. 
# Note: We can access private/protected variables/methods from outside the class by using this syntax: object_name._class_name__variable_name

class Lamp:
    def __init__(self, name: str, model: str, version) -> None:
        self.name = name
        self.__model = model        # Private Variable
        self._version = version     # Protected Variable

    def description(self):
        # self.__self_maintenance()
        print(self.name, self.__model)

    def __self_maintenance(self):
        print(self.name, "is fixing itself.")


class ElectricLamp(Lamp):
    def __init__(self, name: str, model: str, version) -> None:
        super().__init__(name, model, version)

    def do_something(self):
        print(self._version)


if __name__ == "__main__":
    lamp: Lamp = Lamp("Lamp", 1010, 123455)
    lamp.description()
    # print(lamp._Lamp__model)      # Not recommended to use like this
    # lamp._Lamp__self_maintenance()  # Not recommended to use like this


    el_lamp: ElectricLamp = ElectricLamp("Electric Lamp", 1010, 123455)
    el_lamp.do_something()
    print(el_lamp._version)
