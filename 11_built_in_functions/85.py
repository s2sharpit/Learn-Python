# sorted()

nums: list[int] = [1, 6, 2, 3, 4, 7, 5]
nums2: list[int] = [1, 6, 2, 3, 4, 7, 5]

# print(nums.sort()) # None
nums.sort()
print(nums)

# sorted_nums: list[int] = sorted(nums2) # returns a new list
sorted_nums: list[int] = sorted(
    nums2, reverse=True
)  # returns a new list and sorts in descending order
print(sorted_nums)


strings: list[str] = ["A", "b", "C", "d", "e", "F"]
sorted_str: list[str] = sorted(strings)
# sorted_str: list[str] = sorted(strings, key=str.lower)  # sorts the list ignoring the case
# sorted_str: list[str] = sorted(strings, key=str.upper)  # sorts the list ignoring the case
print(sorted_str)
