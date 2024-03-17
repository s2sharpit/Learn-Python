class MyClass:
    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        # Creating an instance using the parent class's __new__ method
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("__init__ called")
        self.value = value


# Creating an instance of MyClass
obj = MyClass(5)
obj1 = MyClass(7)
