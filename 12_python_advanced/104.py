# Custom Exceptions
from typing import Any


class NegativeException(Exception):
    """Raised if a value i below 0"""

    def __init__(self, number: float, error_code: int):
        self.number = number
        self.error_code = error_code
        super().__init__(
            f"Number {self.number} is below 0. (Error code: {self.error_code})",
            self.number,
            self.error_code,
        )

    def __str__(self):
        return f"Number {self.number} is below 0. (Error code: {self.error_code})"

    # it is used to print the different message than the one in __init__ when we call str() on an object of this class

    def custom_method(self):
        print((self.number, self.error_code), "were used by the custom method")

    def __reduce__(self):
        return NegativeException, (self.number, self.error_code)


# raise NegativeException(-5, 999)
try:
    raise NegativeException(-5, 999)
except NegativeException as e:
    print(e)
    print(e.args)
    e.custom_method()
