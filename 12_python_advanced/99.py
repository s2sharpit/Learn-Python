# Memoization

from functools import wraps
from time import perf_counter
import sys


def memoize(func):
    cache: dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


@memoize
def fibonacci(n) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    sys.setrecursionlimit(10_000) # Set the maximum depth of the Python interpreter stack to the required limit
    start_time: float = perf_counter()
    print(fibonacci(2_000))
    end_time: float = perf_counter()
    print(f"Total time: {end_time - start_time} seconds")
