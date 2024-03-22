if __name__ == "__main__":
    yield_comprehension = (i for i in range(10**100))

    print(next(yield_comprehension))
    print(next(yield_comprehension))
    print(next(yield_comprehension))
    print(next(yield_comprehension))
    print(next(yield_comprehension))
