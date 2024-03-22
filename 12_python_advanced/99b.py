from time import perf_counter
import sys
import functools


@functools.cache
def fibonacci(n) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    sys.setrecursionlimit(10_000)
    start_time: float = perf_counter()
    print(fibonacci(200))
    end_time: float = perf_counter()
    print(f"Total time: {end_time - start_time} seconds")
