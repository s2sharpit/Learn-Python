# lambda functions

# def square(a: float) -> float:
#     return a ** 2

# sq = lambda a: a ** 2

# print(square(4))
# print(sq(5))


nums: list[int] = [1, 2, 3, 4, 5, 6, 7]
even: list[int] = list(filter(lambda a: a % 2 == 0, nums))
print(even)

func = lambda text, n: print(text * n)
func('Hello', 3)