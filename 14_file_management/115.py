import json

# with open("./14_file_management/data.json") as file:
#     # print(file.read())  # read the entire content of the file
#     data: str = file.read()
#     actual: dict = json.loads(data) # convert the string to a dictionary
#     print(actual)
#     print(actual['name'])


# The function get_json() reads the content of a JSON file and returns it as a dictionary.
def get_dict(file_path: str) -> dict:
    with open(file_path) as file:
        # return json.loads(file.read()) # convert the string to a dictionary
        return json.load(file)  # convert the json into a dictionary


print(get_dict("./14_file_management/data.json"))


sample: dict = {"name": "John Doe", "age": 30, "has_marks": None}
# sample_json = json.dumps(sample, indent=4)  # Convert the dictionary to a formatted JSON string and add indentation
# print(sample_json)


def write_json(file_path: str, data: dict) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)  # Convert the dictionary to a formatted JSON string and write it to the file

write_json("./14_file_management/sample1.json", sample)