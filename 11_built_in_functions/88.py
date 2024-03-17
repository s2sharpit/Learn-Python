# zip()

people: str = ["John", "Anna", "Peter"]
ages: list[int] = [25, 30, 35]

zipped = zip(people, ages)

# print(zipped)
# output: <zip object at 0x000002120D770B80>

# print(tuple(zipped))
# output: (('John', 25), ('Anna', 30), ('Peter', 35))

for item in zipped:
    print(item)
# output: ('John', 25)
#          ('Anna', 30)
#          ('Peter', 35)

for person, age in zip(people, ages):
    print(person, age, sep=": ")
# output: John: 25


# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

# strict
# The 'strict' parameter in the zip() function determines the behavior when the input iterables are of unequal length.
# By default, 'strict' is set to True, which means that zip() stops when the shortest iterable is exhausted and ignores the remaining elements.
# However, if 'strict' is set to False, zip() continues until the longest iterable is exhausted, filling in missing values with None.