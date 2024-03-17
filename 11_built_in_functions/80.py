# all() & any()

is_connected: bool = True
has_electricity: bool = False
has_paid: bool = True

requirements: list = [is_connected, has_electricity, has_paid]

# all() returns True if all the elements in the iterable are True
has_internet: bool = all(requirements)

print("Internet:", has_internet)

# any() returns True if at least one of the elements in the iterable is True
has_internet: bool = any(requirements)
print("Has internet?: ", has_internet)
