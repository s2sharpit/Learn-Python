# Decorators

from functools import wraps
from time import perf_counter, sleep


def get_time(func):
    """Times any function"""

    @wraps(func) # This is important to keep the original function name and docstring intact.
    def wrapper(*args, **kwargs):
        start_time: float = perf_counter()
        func(*args, **kwargs)
        end_time: float = perf_counter()

        total_time: float = round(end_time - start_time, 3)
        print(f"Total time: {total_time} seconds")

    return wrapper

@get_time
def do_something(param):
    """Do something important"""
    sleep(1)
    # for i in range(10**8):
    #     pass
    print(param)


if __name__ == "__main__":
    do_something("Hello")
    print('__name__', do_something.__name__)
    print('__doc__', do_something.__doc__)
