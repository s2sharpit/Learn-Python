"""
__init__ vs __new__

Description:
__new__ and __init__ are special methods in Python classes used for object creation and initialization, respectively.
- __new__ is responsible for creating a new instance of a class. It's a static method that takes the class itself (cls) as its first argument and returns a new instance of the class.
- __init__ is called after __new__ and is responsible for initializing the newly created object. It takes the newly created instance (self) along with any additional arguments and initializes its attributes.

Usage:
- Use __new__ when you need to customize how instances of a class are created, such as implementing a singleton pattern or managing object pooling.
- Use __init__ to initialize the attributes of a newly created instance. It's typically used to set up the initial state of the object.
"""


class Connection:
    """Class: Represents a connection to the internet."""

    __instance = None

    def __new__(cls, *args, **kwargs):
        """Method: Create a new instance of the class."""
        if cls.__instance is None:
            print("Connecting...")
            cls.__instance = super().__new__(cls)
        else:
            print("WARNING: There's already a connection!")
        return cls.__instance

    def __init__(self):
        """Method: Initialize the connection."""
        print("Connected to internet!")


connection = Connection()  # Creates a new connection
connection2 = Connection()  # Returns the existing connection (singleton)
