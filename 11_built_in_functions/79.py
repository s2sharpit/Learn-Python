# locals
import math

var: str = "text"


def hello():
    hello_str: str = "str"
    hello_int: str = "str"

    def inner():
        pass

    print(locals())
    # locals are the all in this function defined variables
    print(locals() == globals())  # False


hello()

print(locals())
print(locals() == globals())  # True
