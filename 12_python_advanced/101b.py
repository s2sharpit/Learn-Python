import timeit


def make_calulation(first: int, second: int):
    for i in range(10**3):
        pass

    return first + second


def do_something():
    for i in range(10):
        x: int = i**i


def get_time(func: str, repeat: int, number: int) -> float:
    speed: float = min(
        timeit.repeat(func, repeat=repeat, number=number, globals=globals())
    )
    print(f"{func} -> {speed:.4f} sec (ran {repeat * number:,} times)")

    return speed


if __name__ == "__main__":
    print(globals())
    a, b = 1, 2
    get_time("x = [i for i in range(100)]", 10, 10**5)
    get_time("do_something()", 10, 10**5)
    get_time("make_calulation(a, b)", 10, 10**5)
