# @decorators(args)

from functools import wraps
from typing import Callable


def repeat(times: int, message: str):
    """Repeat function call x amount of times"""

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                value = func(*args, **kwargs)

            print(message)

            return value

        return wrapper

    return decorator


@repeat(3, "Hello!")
def func1():
    print("hello")


@repeat(2, "Numbers!")
def func2(a: int, b: int):
    print(a, b)


if __name__ == "__main__":
    func1()
func2(1, 2)
