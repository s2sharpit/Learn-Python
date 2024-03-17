# map()

numbers: list[int] = [1, 2, 3, 4, 5, 6]


def convert_to_str(element):
    element *= element
    return str(element)

converted_list: list[str] = list(map(convert_to_str, numbers))
print(converted_list)