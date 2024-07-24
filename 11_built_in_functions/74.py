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
    """
    Enumerate:
    - Iterates over an iterable and returns an enumerate object consisting of pairs of index and value.
    """
    print(i)

for i, name in enumerate(names, start=1):
    """
    Enumerate with start:
    - Enumerates over an iterable starting from a specified index.
    """
    print(i, ":", name)

# round
number: float = 3.14159265359
"""
Round:
- Rounds a number to a specified number of decimal places.
"""
print(round(number, 2))

# range()
# range(10) == range(0, 10, 1)
num: range = range(0, -10, -1)
"""
Range:
- Generates a sequence of numbers within a specified range.
"""
print(list(num))

print(sys.getsizeof(num))
print(sys.getsizeof(list(num)))
