import sys

# print()

print(
    "String",
    "t",
    1,
    2.5,
    True,
    [1, 2, 3],
    (4, 5, 6),
    {"a": 1, "b": 2, "c": 3},
    sep=" | ",
    end="\n\n",
)

print("Mario")

# enumerate()

names: list[str] = ["Mario", "Luigi", "Peach", "Toad", "Yoshi"]

# for name in names:
#     print(names.index(name), ':', name)

for i in enumerate(names):
    print(i)

for i, name in enumerate(names, start=1):
    print(i, ":", name)

# round
number: float = 3.14159265359
print(round(number, 2))

# range()
# range(10) == range(0, 10, 1)
num: range = range(0, -10, -1)
print(list(num))

print(sys.getsizeof(num))
print(sys.getsizeof(list(num)))


# globals
